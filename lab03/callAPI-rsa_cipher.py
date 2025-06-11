import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnGenkey.clicked.connect(self.call_api_genkey)
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btnSign.clicked.connect(self.call_api_sign)
        self.ui.btnVerifiy.clicked.connect(self.call_api_verify)
    #tao khoa
    def call_api_genkey(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)  # Changed to requests.get
            if response.status_code == 200:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Gen Key Successfully")
                msg.exec_()
            else:
                print("Error while calling API: %s" % response.status_code) # More informative error
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e) # e.message is deprecated, use e directly
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.textEdit.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtCiphertext.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertexthex": self.ui.txtCiphertext.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txtIn4.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtSign.setText(data["signature"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Gen sign Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
    def call_api_verify(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txtIn4.toPlainText(),
            "signature": self.ui.txtSign.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data['is_verified']:
                     msg.setText("true")
                else:
                    msg.setText("false")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())