
from flask import Flask,request,jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCypher
from cipher.transposition import TranspositionCipher
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
    cipher_text = data ['cipher_text']
    key = int(data['key'])
    decrypt_text = caesar_cipher.decrypt_text(cipher_text,key)
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
    cipher_text = data['cipher_text']
    key = data ['key']
    decrypt_text = vigenere_cipher.vigenere_decrypt(cipher_text,key)
    return jsonify({'giai ma': decrypt_text})
raile = RailFenceCipher()

@app.route("/api/railfence/encrypt",methods =["POST"])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = raile.rail_fence_encrypt(plain_text,key)
    return jsonify({'ma hoa': encrypt_text})

@app.route("/api/railfence/decrypt",methods =["POST"])    
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = raile.rail_fence_decrypt(cipher_text,key)
    return jsonify({'giai ma': decrypt_text})

playfair = PlayFairCypher()
@app.route("/api/playfair/taomatran",methods =["POST"])
def playfair_taomatran():
    data = request.json
    key = data['key']
    playfair_matran = playfair.create_playfair_matrix(key)
    return jsonify({'ma hoa': playfair_matran})

@app.route("/api/playfair/encrypt",methods =["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matran = playfair.create_playfair_matrix(key)
    encrypt_text = playfair.playfair_encrypt(plain_text,playfair_matran)
    return jsonify({'ma hoa': encrypt_text})

@app.route("/api/playfair/decrypt",methods =["POST"])    
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matran = playfair.create_playfair_matrix(key)
    decrypt_text = playfair.playfair_decrypt(cipher_text,playfair_matran)
    return jsonify({'giai ma': decrypt_text})
trans = TranspositionCipher()

@app.route("/api/transposition/encrypt",methods =["POST"])
def transposition_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = trans.transposition_encrypt(plain_text,key)
    return jsonify({'ma hoa': encrypt_text})
@app.route("/api/transposition/dencrypt",methods =["POST"])
def transposition_decrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    decrypt_text = trans.transposition_decrypt(plain_text,key)
    return jsonify({'giai ma': decrypt_text})
#mai function
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port = 5000,debug=True)