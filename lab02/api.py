
from flask import Flask,request,jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
app = Flask(__name__)
caesar_cipher = CaesarCipher()
@app.route("/api/caesar/encrypt",methods =["POST"])
def caesar_encrypt():
    data= request.json
    plain_text = data ['plain_text']
    key = int(data['key'])
    encrypt_text = caesar_cipher.encrypt_text(plain_text,key)
    return jsonify({'ma hoa': encrypt_text})
@app.route("/api/caesar/decrypt",methods =["POST"])
def caesar_decrypt():
    data= request.json
    plain_text = data ['plain_text']
    key = int(data['key'])
    decrypt_text = caesar_cipher.decrypt_text(plain_text,key)
    return jsonify({'giai ma': decrypt_text})
vigenere_cipher = VigenereCipher()
@app.route("/api/vigenere/encrypt",methods =["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data ['key']
    encrypt_text = vigenere_cipher.vigenere_encrypt(plain_text,key)
    return jsonify({'ma hoa': encrypt_text})
@app.route("/api/vigenere/decrypt",methods =["POST"])    
def vigenere_decrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data ['key']
    decrypt_text = vigenere_cipher.vigenere_decrypt(plain_text,key)
    return jsonify({'giai ma': decrypt_text})
#mai function
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port = 5000,debug=True)