from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib
import sys # Import sys để có thể exit ứng dụng

# Khởi tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Tạo cặp khóa RSA cho server
server_key = RSA.generate(2048)

# Danh sách các client đã kết nối
clients = []

# Biến cờ để kiểm soát việc server có đang chạy hay không
SERVER_RUNNING = True

# Hàm mã hóa tin nhắn
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Hàm giải mã tin nhắn
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Hàm xử lý kết nối client
def handle_client(client_socket, client_address):
    print(f"Đã kết nối với {client_address}")

    # Khóa AES sẽ được tạo trong quá trình bắt tay
    aes_key = None 
    try:
        # Gửi khóa công khai của server cho client
        client_socket.send(server_key.publickey().export_key(format='PEM'))

        # Nhận khóa công khai của client
        client_received_key = RSA.import_key(client_socket.recv(2048))

        # Tạo khóa AES cho mã hóa tin nhắn
        aes_key = get_random_bytes(16)

        # Mã hóa khóa AES bằng khóa công khai của client
        cipher_rsa = PKCS1_OAEP.new(client_received_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)
        client_socket.send(encrypted_aes_key)

        # Thêm client vào danh sách (chỉ khi bắt tay thành công)
        clients.append((client_socket, aes_key))

        while True:
            # Nếu server không còn chạy, thoát vòng lặp xử lý client
            if not SERVER_RUNNING:
                print(f"Server đang tắt, đóng kết nối với {client_address}.")
                break

            encrypted_message = client_socket.recv(1024)
            if not encrypted_message: # Nếu không nhận được dữ liệu, client có thể đã ngắt kết nối
                print(f"Client {client_address} đã ngắt kết nối.")
                break
            
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"Nhận từ {client_address}: {decrypted_message}")

            # Nếu tin nhắn là "exit" từ client, ngắt kết nối client đó
            if decrypted_message == "exit":
                break

            # Gửi tin nhắn nhận được đến tất cả các client khác
            # Duyệt qua một bản sao của danh sách clients để tránh lỗi khi danh sách thay đổi trong quá trình duyệt
            for client_item, key_item in list(clients): 
                if client_item != client_socket: # Không gửi lại cho chính client gửi đi
                    try:
                        encrypted = encrypt_message(key_item, decrypted_message)
                        client_item.send(encrypted)
                    except Exception as broadcast_e:
                        print(f"Lỗi khi gửi tin nhắn tới một client khác: {broadcast_e}")
                        # Có thể cần xử lý client lỗi ở đây (ví dụ: xóa khỏi danh sách)
                        if (client_item, key_item) in clients:
                            clients.remove((client_item, key_item))
                            client_item.close()

    except Exception as e:
        print(f"Lỗi khi xử lý client {client_address}: {e}")
    finally:
        # Xóa client khỏi danh sách và đóng socket
        if (client_socket, aes_key) in clients:
            clients.remove((client_socket, aes_key))
        client_socket.close()
        print(f"Kết nối với {client_address} đã đóng")

# Hàm chấp nhận các kết nối client
def accept_connections():
    global SERVER_RUNNING
    print("Server đang lắng nghe các kết nối...")
    server_socket.settimeout(1.0) # Đặt timeout để không bị chặn vô thời hạn bởi accept()

    while SERVER_RUNNING:
        try:
            client_socket, client_address = server_socket.accept()
            # Tạo một luồng mới để xử lý mỗi client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True # Đặt luồng là daemon để nó tự tắt khi luồng chính tắt
            client_thread.start()
        except socket.timeout:
            continue # Tiếp tục vòng lặp nếu hết thời gian chờ
        except Exception as e:
            if SERVER_RUNNING: # Chỉ in lỗi nếu server đang chạy bình thường, không phải đang tắt
                print(f"Lỗi khi chấp nhận kết nối: {e}")
            break # Thoát vòng lặp chấp nhận kết nối nếu có lỗi nghiêm trọng

# --- Hàm "hủy diệt" server ---
def destroy_server():
    global SERVER_RUNNING
    print("\n--- Yêu cầu hủy diệt server đã nhận ---")
    SERVER_RUNNING = False
    
    # Đóng server socket để ngắt vòng lặp accept_connections
    try:
        server_socket.shutdown(socket.SHUT_RDWR) # Đóng cả gửi và nhận
        server_socket.close()
        print("Đã đóng socket server.")
    except Exception as e:
        print(f"Lỗi khi đóng server socket: {e}")

    # Đóng tất cả các kết nối client còn lại
    print("Đang đóng các kết nối client còn lại...")
    for client_socket, _ in list(clients): # Duyệt qua bản sao để tránh lỗi khi sửa đổi danh sách
        try:
            client_socket.close()
        except Exception as e:
            print(f"Lỗi khi đóng client socket: {e}")
    clients.clear() # Xóa tất cả client khỏi danh sách
    print("Tất cả các client đã được đóng.")

    print("Server đã dừng hoạt động.")
    sys.exit(0) # Thoát ứng dụng một cách an toàn


# Bắt đầu luồng chấp nhận kết nối client
accept_thread = threading.Thread(target=accept_connections)
accept_thread.daemon = True # Đặt luồng là daemon
accept_thread.start()

# Vòng lặp chính để lắng nghe lệnh từ console
print("Nhập 'exit_server' để tắt server.")
while True:
    command = input("") # Lắng nghe input từ người dùng
    if command.lower() == "exit_server":
        destroy_server()
        break # Thoát vòng lặp chính
    elif not SERVER_RUNNING: # Nếu server đã bị tắt bởi lý do khác
        break
