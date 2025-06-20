# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QByteArray, QRect
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main vertical layout
        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setSpacing(15)
        self.verticalLayout_main.setContentsMargins(20, 20, 20, 20)

        # RSA CIPHER Label - ANIMATIONS REMOVED
        self.lblRSA = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        self.lblRSA.setFont(font)
        self.lblRSA.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRSA.setObjectName("lblRSA")
        self.verticalLayout_main.addWidget(self.lblRSA)

        # Removed: self.lblRSA.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(self.lblRSA))
        # Removed: self.lblRSA.graphicsEffect().setOpacity(0)
        # Removed: self.animation_lbl_fade = QPropertyAnimation(...)
        # Removed: self.animation_lbl_bounce = QPropertyAnimation(...)


        # Flexible space
        self.verticalSpacer_top = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addItem(self.verticalSpacer_top)

        # Layout containing 2 main columns (Encrypt/Decrypt and Sign/Verify)
        self.horizontalLayout_sections = QtWidgets.QHBoxLayout()
        self.horizontalLayout_sections.setSpacing(30)

        # Left column: Encrypt/Decrypt
        self.verticalLayout_encrypt_decrypt = QtWidgets.QVBoxLayout()
        self.verticalLayout_encrypt_decrypt.setSpacing(10)

        # Label PLAIN TEXT
        self.txtPlaintext_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.txtPlaintext_label.setFont(font)
        self.txtPlaintext_label.setObjectName("txtPlaintext_label")
        self.verticalLayout_encrypt_decrypt.addWidget(self.txtPlaintext_label)

        # QTextEdit for Plaintext
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 120))
        self.textEdit.setPlaceholderText("Nhập văn bản để mã hóa...")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_encrypt_decrypt.addWidget(self.textEdit)

        # Button GENERATE KEYS
        self.btnGenkey = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenkey.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnGenkey.setFont(font)
        self.btnGenkey.setObjectName("btnGenkey")
        self.verticalLayout_encrypt_decrypt.addWidget(self.btnGenkey)
        self.btnGenkey.setStyleSheet("QPushButton { background-color: lightblue; border-radius: 5px; } QPushButton:hover { background-color: skyblue; }") # Basic style

        # Layout for ENCRYPT and DECRYPT buttons
        self.horizontalLayout_encrypt_decrypt_buttons = QtWidgets.QHBoxLayout()
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEncrypt.setFont(font)
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.horizontalLayout_encrypt_decrypt_buttons.addWidget(self.btnEncrypt)
        self.btnEncrypt.setStyleSheet("QPushButton { background-color: lightgreen; border-radius: 5px; } QPushButton:hover { background-color: mediumseagreen; }") # Basic style


        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDecrypt.setFont(font)
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.horizontalLayout_encrypt_decrypt_buttons.addWidget(self.btnDecrypt)
        self.btnDecrypt.setStyleSheet("QPushButton { background-color: lightcoral; border-radius: 5px; } QPushButton:hover { background-color: indianred; }") # Basic style

        self.verticalLayout_encrypt_decrypt.addLayout(self.horizontalLayout_encrypt_decrypt_buttons)

        # Label CIPHERTEXT
        self.lblCiphertext = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblCiphertext.setFont(font)
        self.lblCiphertext.setObjectName("lblCiphertext")
        self.verticalLayout_encrypt_decrypt.addWidget(self.lblCiphertext)

        # QTextEdit for Ciphertext
        self.txtCiphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCiphertext.setMinimumSize(QtCore.QSize(0, 80))
        self.txtCiphertext.setReadOnly(True)
        self.txtCiphertext.setPlaceholderText("Văn bản đã mã hóa sẽ hiển thị ở đây...")
        self.txtCiphertext.setObjectName("txtCiphertext")
        self.verticalLayout_encrypt_decrypt.addWidget(self.txtCiphertext)

        self.horizontalLayout_sections.addLayout(self.verticalLayout_encrypt_decrypt)

        # Right column: Sign/Verify
        self.verticalLayout_sign_verify = QtWidgets.QVBoxLayout()
        self.verticalLayout_sign_verify.setSpacing(10)

        # Label IN4
        self.lblIn4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblIn4.setFont(font)
        self.lblIn4.setObjectName("lblIn4")
        self.verticalLayout_sign_verify.addWidget(self.lblIn4)

        # QTextEdit for Message to Sign/Verify
        self.txtIn4 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtIn4.setMinimumSize(QtCore.QSize(0, 120))
        self.txtIn4.setPlaceholderText("Nhập tin nhắn để ký hoặc xác minh...")
        self.txtIn4.setObjectName("txtIn4")
        self.verticalLayout_sign_verify.addWidget(self.txtIn4)

        # Layout for SIGN and VERIFY buttons
        self.horizontalLayout_sign_verify_buttons = QtWidgets.QHBoxLayout()
        self.btnSign = QtWidgets.QPushButton(self.centralwidget)
        self.btnSign.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSign.setFont(font)
        self.btnSign.setObjectName("btnSign")
        self.horizontalLayout_sign_verify_buttons.addWidget(self.btnSign)
        self.btnSign.setStyleSheet("QPushButton { background-color: lightblue; border-radius: 5px; } QPushButton:hover { background-color: skyblue; }") # Basic style


        self.btnVerifiy = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerifiy.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnVerifiy.setFont(font)
        self.btnVerifiy.setObjectName("btnVerifiy")
        self.horizontalLayout_sign_verify_buttons.addWidget(self.btnVerifiy)
        self.btnVerifiy.setStyleSheet("QPushButton { background-color: orange; border-radius: 5px; } QPushButton:hover { background-color: darkorange; }") # Basic style


        self.verticalLayout_sign_verify.addLayout(self.horizontalLayout_sign_verify_buttons)

        # Label SIGNATURE
        self.lblSignature = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblSignature.setFont(font)
        self.lblSignature.setObjectName("lblSignature")
        self.verticalLayout_sign_verify.addWidget(self.lblSignature)

        # QTextEdit for Signature
        self.txtSign = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSign.setMinimumSize(QtCore.QSize(0, 80))
        self.txtSign.setPlaceholderText("Chữ ký sẽ hiển thị ở đây hoặc được nhập để xác minh...")
        self.txtSign.setObjectName("txtSign")
        self.verticalLayout_sign_verify.addWidget(self.txtSign)

        self.horizontalLayout_sections.addLayout(self.verticalLayout_sign_verify)

        self.verticalLayout_main.addLayout(self.horizontalLayout_sections)

        # Flexible space at the bottom
        self.verticalSpacer_bottom = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addItem(self.verticalSpacer_bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Removed the initial animation connection for lblRSA
        # MainWindow.showEvent = lambda event: self.start_initial_animations() and super(type(MainWindow), MainWindow).showEvent(event)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ứng dụng mã hóa RSA"))
        self.lblRSA.setText(_translate("MainWindow", "RSA CIPHER"))
        self.txtPlaintext_label.setText(_translate("MainWindow", "PLAIN TEXT"))
        self.lblCiphertext.setText(_translate("MainWindow", "CIPHERTEXT"))
        self.lblIn4.setText(_translate("MainWindow", "THÔNG TIN/TIN NHẮN"))
        self.lblSignature.setText(_translate("MainWindow", "CHỮ KÝ"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnGenkey.setText(_translate("MainWindow", "TẠO KHÓA"))
        self.btnEncrypt.setText(_translate("MainWindow", "MÃ HÓA"))
        self.btnDecrypt.setText(_translate("MainWindow", "GIẢI MÃ"))
        self.btnSign.setText(_translate("MainWindow", "KÝ"))
        self.btnVerifiy.setText(_translate("MainWindow", "XÁC MINH"))

    # --- New Animation Methods (kept as they might be useful for other elements) ---

    def start_initial_animations(self):
        """
        This method was for the lblRSA animation, now it's empty as per request.
        You can remove it entirely if no other initial animations are needed.
        """
        pass # No animations for lblRSA anymore

    def animate_button_click(self, button):
        """Animates a button's background color on click."""
        # Save original stylesheet to restore later
        original_style = button.styleSheet()

        # Define animation for background color (using QPropertyAnimation and stylesheet)
        self.button_animation = QPropertyAnimation(button, QByteArray(b"styleSheet"))
        self.button_animation.setDuration(300) # Quick flash
        self.button_animation.setStartValue(original_style)
        self.button_animation.setEndValue(f"QPushButton {{ background-color: yellow; border-radius: 5px; }}") # Flash yellow
        self.button_animation.setEasingCurve(QEasingCurve.OutQuad)

        # Restore original style after animation
        self.button_animation.finished.connect(lambda: button.setStyleSheet(original_style))
        self.button_animation.start()

    def animate_text_edit_highlight(self, text_edit):
        """Briefly highlights a QTextEdit by changing its background color."""
        # Save original stylesheet
        original_style = text_edit.styleSheet()

        # Define animation for background color
        self.text_edit_animation = QPropertyAnimation(text_edit, QByteArray(b"styleSheet"))
        self.text_edit_animation.setDuration(500) # Half second highlight
        self.text_edit_animation.setStartValue("QTextEdit { background-color: white; }") # Start with white
        self.text_edit_animation.setKeyValueAt(0.5, "QTextEdit { background-color: lightyellow; }") # Go to yellow
        self.text_edit_animation.setEndValue("QTextEdit { background-color: white; }") # End with white
        self.text_edit_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.text_edit_animation.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())