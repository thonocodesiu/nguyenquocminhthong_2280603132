from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCypher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)

 #router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

 #router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()

    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template("caesar.html", outputCipherText=encrypted_text)

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    render_template("caesar.html", outputPlainText=decrypted_text)

##vigenere
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vige = VigenereCipher()

    encrypted_text = vige.vigenere_encrypt(text, key)
    return render_template("vigenere.html", outputCipherText=encrypted_text)

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vige = VigenereCipher()
    decrypted_text = vige.vigenere_decrypt(text, key)
    return render_template("vigenere.html", outputPlainText=decrypted_text)
###playfair
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    play = PlayFairCypher()
    matric = play.create_playfair_matrix(key)
    encrypted_text = play.playfair_encrypt(text, matric)
    return render_template("playfair.html", outputCipherText=encrypted_text)
@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    play = PlayFairCypher()
    matric = play.create_playfair_matrix(key)
    decrypted_text = play.playfair_decrypt(text, matric)
    return render_template("playfair.html", outputPlainText=decrypted_text, playfairMatrix=matric)
##railfence
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return render_template("railfence.html", outputCipherText=encrypted_text)

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return render_template("railfence.html", outputPlainText=decrypted_text)

##Transposition
@app.route("/Transposition")
def transposition():
    return render_template('transposition.html')
@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transposition = TranspositionCipher()

    encrypted_text = transposition.transposition_encrypt(text, key)
    return render_template("transposition.html", outputCipherText=encrypted_text)

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transposition = TranspositionCipher()
    decrypted_text = transposition.transposition_decrypt(text, key)
    return render_template("transposition.html", outputPlainText=decrypted_text)
# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)