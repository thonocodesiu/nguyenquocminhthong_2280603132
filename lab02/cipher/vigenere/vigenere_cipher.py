class VigenereCipher:
    def __init__(self):
        pass
    def vigenere_encrypt(self, plain_text,key):
        encrypt_text=""
        key_index=0
        for char in plain_text:
            if char.isalpha():
                key_shilf=ord(key[key_index%len(key)].upper())-ord('A')
                if char.isupper():
                    encrypt_text+= chr((ord(char)-ord('A')+key_shilf)%26 +ord('A'))
                else:
                    encrypt_text += chr((ord(char)-ord('a')+key_shilf)%26+ord('a'))
                key_index+=1
            else:
                encrypt_text+=char
        return encrypt_text

    def vigenere_decrypt(self,encrypt_text,key):
        decrypt_text =""
        key_index = 0
        for char in encrypt_text:
            if char.isalpha():
                key_shilf = ord(key[key_index%len(key)].upper())-ord('A')
                if char.isupper():
                    decrypt_text+= chr((ord(char)-ord('A')-key_shilf)%26+ord('A'))
                else:
                    decrypt_text+= chr((ord(char)-ord('a')-key_shilf)%26+ord('a'))
                key_index +=1
            else:
                decrypt_text+= char
        return decrypt_text