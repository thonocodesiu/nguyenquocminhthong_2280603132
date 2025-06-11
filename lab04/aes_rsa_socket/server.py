from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Khởi tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SỬA LỖI: Gói địa chỉ và cổng vào một tuple
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Tạo cặp khóa RSA cho server
server_key = RSA.generate(2048)

# Danh sách các client đã kết nối
clients = []

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

        # Thêm client vào danh sách
        clients.append((client_socket, aes_key))

        while True:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message: # Nếu không nhận được dữ liệu, client có thể đã ngắt kết nối
                print(f"Client {client_address} đã ngắt kết nối.")
                break
            
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"Nhận từ {client_address}: {decrypted_message}")

            # Nếu tin nhắn là "exit", ngắt kết nối
            if decrypted_message == "exit":
                break

            # Gửi tin nhắn nhận được đến tất cả các client khác
            for client, key in clients:
                if client != client_socket: # Không gửi lại cho chính client gửi đi
                    encrypted = encrypt_message(key, decrypted_message)
                    client.send(encrypted)
    except Exception as e:
        print(f"Lỗi khi xử lý client {client_address}: {e}")
    finally:
        # Xóa client khỏi danh sách và đóng socket
        if (client_socket, aes_key) in clients:
            clients.remove((client_socket, aes_key))
        client_socket.close()
        print(f"Kết nối với {client_address} đã đóng")

# Chấp nhận và xử lý các kết nối client
print("Server đang lắng nghe các kết nối...")
while True:
    client_socket, client_address = server_socket.accept()
    # Tạo một luồng mới để xử lý mỗi client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
