from flask import Flask,request,jsonify
from cipher.rsa.rsa_cipher import RSACipher
from cipher.ecc.ecc_cipher import ECCCpiher
app = Flask(__name__)

rsaC = RSACipher()
eCC = ECCCpiher()
@app.route('/api/rsa/generate_keys',methods=['GET'])
def rsa_generate_keys():
    rsaC.generate_keys()
    return jsonify({'message': 'tao khoa thanh cong'})
@app.route('/api/rsa/encrypt',methods=['POST'])
def rsa_encrypt():
    data = request.json
    message = data['message']
    key_type = data['key_type']
    private_key, public_key = rsaC.load_keys()
    if key_type == 'public':
        key=public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error':'Loi!!'})
    encrypted_message= rsaC.encrypt(message,key)
    encrypted_hex=encrypted_message.hex()
    return jsonify ({'encrypted_message':encrypted_hex})
@app.route('/api/rsa/decrypt',methods=['POST'])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data['ciphertexthex']
    key_type = data['key_type']
    private_key, public_key = rsaC.load_keys()
    if key_type == 'public':
        key=public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error':'Loi!!'})
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message= rsaC.decrypt(ciphertext,key)
    return jsonify ({'decrypted_message':decrypted_message})
@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = rsaC.load_keys()
    signature = rsaC.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = rsaC.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = rsaC.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

## ECC cipher
@app.route('/api/ecc/generate_keys',methods=['GET'])
def ecc_generate_keys():
    eCC.generate_keys()
    return jsonify({'message': 'tao khoa thanh cong'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = eCC.load_keys()
    signature = eCC.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})
@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = eCC.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = eCC.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)