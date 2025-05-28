class PlayFairCypher:
    def __init__(self) -> None:
        pass
    def __init__(self):
        pass
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        seen = set()
        matrix = []
        # Chỉ thêm ký tự mới vào ma trận
        for ch in key:
            if ch not in seen and ch.isalpha():
                seen.add(ch)
                matrix.append(ch)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for ch in alphabet:
            if ch not in seen:
                matrix.append(ch)
                if len(matrix) == 25:
                    break

        # Chia thành 5×5
        return [matrix[i:i+5] for i in range(0,25,5)]
    def find_letter_coords(self,matrix, letter):
        for row in range (len(matrix)):
            for col in range(len(matrix)):
                if matrix [row][col]==letter:
                    return row,col
    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()

        # Tiền xử lý để chèn 'X' khi 2 ký tự liền nhau giống nhau
        processed_text = ""
        i = 0
        while i < len(plain_text):
            processed_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i + 1]:
                    processed_text += 'X'
                    i += 1
                else:
                    processed_text += plain_text[i + 1]
                    i += 2
            else:
                i += 1

        # Nếu độ dài lẻ thì thêm 'X' cuối
        if len(processed_text) % 2 != 0:
            processed_text += 'X'

        encrypted_text = ""
        for i in range(0, len(processed_text), 2):
            pair = processed_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] +  matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] +  matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] +  matrix[row2][col1]

        banro = ""
        for i in range(0, len(decrypted_text) - 2, 2):
            if decrypted_text[i] ==  decrypted_text[i+2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] +""+ decrypted_text[i+1]

        if decrypted_text[-1] == "X":
    # Nếu ký tự cuối là 'X', thêm ký tự đứng trước nó
            banro += decrypted_text[-2]
        else:
    # Nếu không phải 'X', thêm cả 2 ký tự cuối cùng
            banro += decrypted_text[-2] + decrypted_text[-1]        
        return banro