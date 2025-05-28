class RailFenceCipher:
    def __init__(self):
        pass
    def rail_fence_encrypt(self,plain_text,num_rails):
        rails=[[]for _ in range(num_rails)]
        rail_index=0
        dic =1
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index ==0:
                dic =1
            elif rail_index == num_rails -1:
                dic = -1
            rail_index += dic
        cipher_text = ''.join(''.join(rail)for rail in rails)
        return cipher_text
    def rail_fence_decrypt(self, cipher_text, num_rails):
        rail_len = [0] * num_rails
        rail_index = 0
        dic = 1

        # Đếm số kí tự trên từng rail
        for _ in range(len(cipher_text)):
            rail_len[rail_index] += 1
            if rail_index == 0:
                dic = 1
            elif rail_index == num_rails - 1:
                dic = -1
            rail_index += dic

        rails = []
        start = 0  # Sửa biến start

        # Lấy từng phần tương ứng độ dài rail
        for dodai in rail_len:
            rails.append(cipher_text[start:start + dodai])
            start += dodai

        plain_text = ""
        rail_index = 0
        dic = 1

        # Đọc theo zigzag để giải mã
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]  # Bỏ ký tự vừa lấy

            if rail_index == 0:
                dic = 1
            elif rail_index == num_rails - 1:
                dic = -1
            rail_index += dic

        return plain_text
