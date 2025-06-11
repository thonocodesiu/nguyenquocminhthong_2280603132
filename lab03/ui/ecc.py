# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QPushButton, QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow, QMenuBar, QStatusBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700) # Tăng kích thước để có không gian cho bố cục mới

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Bố cục chính cho central widget
        main_layout = QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Tiêu đề (label từ mã gốc)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter) # Căn giữa tiêu đề
        self.label.setObjectName("titleLabel") # Sử dụng titleLabel cho QSS
        main_layout.addWidget(self.label)

        # Bố cục ngang cho phần SIGN và VERIFY
        content_layout = QHBoxLayout()
        content_layout.setSpacing(30) # Tăng khoảng cách giữa các phần

        # Phần SIGN (bên trái)
        sign_section_layout = QVBoxLayout()
        sign_section_layout.setAlignment(QtCore.Qt.AlignTop) # Căn chỉnh nội dung lên trên

        self.label_2 = QtWidgets.QLabel(self.centralwidget) # Nhãn "SIGN"
        self.label_2.setObjectName("sectionLabel") # Sử dụng sectionLabel cho QSS
        sign_section_layout.addWidget(self.label_2)

        self.txtSign = QtWidgets.QTextEdit(self.centralwidget) # Nhập/Xuất cho Sign
        self.txtSign.setPlaceholderText("Nhập tin nhắn để ký hoặc hiển thị chữ ký...") # Văn bản gợi ý
        self.txtSign.setMinimumHeight(200) # Làm cho chiều cao lớn hơn
        self.txtSign.setObjectName("textInputOutput") # Tên thống nhất cho QSS
        sign_section_layout.addWidget(self.txtSign)

        self.btnSign = QtWidgets.QPushButton(self.centralwidget) # Nút Sign
        self.btnSign.setObjectName("actionButton") # Sử dụng actionButton cho QSS
        sign_section_layout.addWidget(self.btnSign, alignment=QtCore.Qt.AlignCenter) # Căn giữa nút

        content_layout.addLayout(sign_section_layout, 1) # Chiếm 1 phần không gian

        # Nút "Tao khoa" ở giữa
        center_button_layout = QVBoxLayout()
        center_button_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.btnTaokhoa = QtWidgets.QPushButton(self.centralwidget)
        self.btnTaokhoa.setObjectName("createKeyButton") # Sử dụng createKeyButton cho QSS
        self.btnTaokhoa.setFixedSize(120, 40) # Cố định kích thước nút
        center_button_layout.addWidget(self.btnTaokhoa)
        content_layout.addLayout(center_button_layout, 0) # Chiếm không gian tối thiểu

        # Phần VERIFY (bên phải)
        verify_section_layout = QVBoxLayout()
        verify_section_layout.setAlignment(QtCore.Qt.AlignTop) # Căn chỉnh nội dung lên trên

        self.label_3 = QtWidgets.QLabel(self.centralwidget) # Nhãn "VERIFY"
        self.label_3.setObjectName("sectionLabel") # Sử dụng sectionLabel cho QSS
        verify_section_layout.addWidget(self.label_3)

        self.txtVerify = QtWidgets.QTextEdit(self.centralwidget) # Nhập/Xuất cho Verify
        self.txtVerify.setPlaceholderText("Nhập tin nhắn hoặc chữ ký để xác minh...") # Văn bản gợi ý
        self.txtVerify.setMinimumHeight(200) # Làm cho chiều cao lớn hơn
        self.txtVerify.setObjectName("textInputOutput") # Tên thống nhất cho QSS
        verify_section_layout.addWidget(self.txtVerify)

        self.btnVerify = QtWidgets.QPushButton(self.centralwidget) # Nút Verify
        self.btnVerify.setObjectName("actionButton") # Sử dụng actionButton cho QSS
        verify_section_layout.addWidget(self.btnVerify, alignment=QtCore.Qt.AlignCenter) # Căn giữa nút

        content_layout.addLayout(verify_section_layout, 1) # Chiếm 1 phần không gian

        main_layout.addLayout(content_layout)

        # Menubar và Statusbar (từ mã gốc, chỉ thiết lập đối tượng)
        MainWindow.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21)) # Điều chỉnh chiều rộng
        MainWindow.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(MainWindow.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Áp dụng QSS
        self.apply_qss(MainWindow)
        
        # retranslateUi (theo cấu trúc mã gốc)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def apply_qss(self, MainWindow):
        qss = """
        QMainWindow {
            background-color: #1a1a1a;
            color: #00ff00;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 14px;
        }

        #titleLabel {
            color: #00ffff;
            font-size: 48px;
            font-weight: bold;
            padding-bottom: 20px;
            border-bottom: 2px solid #005f5f;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
        }

        #sectionLabel {
            color: #00ff00;
            font-size: 24px;
            font-weight: bold;
            padding-bottom: 5px;
            margin-top: 15px;
            margin-bottom: 10px;
            border-bottom: 1px dashed #003300;
        }

        #textInputOutput {
            background-color: #0d0d0d;
            color: #00ff00;
            border: 1px solid #005f5f;
            border-radius: 5px;
            padding: 10px;
            selection-background-color: #003300;
            selection-color: #00ff00;
        }
        
        #actionButton {
            background-color: #007777;
            color: #ffffff;
            border: 1px solid #00ffff;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
            min-height: 40px;
        }
        #actionButton:hover {
            background-color: #009999;
            border: 1px solid #00ffff;
            box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
        }
        #actionButton:pressed {
            background-color: #005555;
            border: 1px solid #00ffff;
            box-shadow: none;
        }

        #createKeyButton {
            background-color: #800080;
            color: #ffffff;
            border: 1px solid #ff00ff;
            border-radius: 8px;
            padding: 10px 15px;
            font-size: 16px;
            font-weight: bold;
            min-height: 40px;
        }
        #createKeyButton:hover {
            background-color: #a000a0;
            border: 1px solid #ff00ff;
            box-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff;
        }
        #createKeyButton:pressed {
            background-color: #600060;
            border: 1px solid #ff00ff;
            box-shadow: none;
        }

        QStatusBar {
            background-color: #0d0d0d;
            color: #00ffff;
            font-size: 12px;
            padding: 5px;
            border-top: 1px solid #005f5f;
        }
        """
        MainWindow.setStyleSheet(qss)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ECC Cipher"))
        self.label.setText(_translate("MainWindow", "ECC Cipher"))
        self.label_2.setText(_translate("MainWindow", "SIGN"))
        self.label_3.setText(_translate("MainWindow", "VERIFY"))
        self.btnTaokhoa.setText(_translate("MainWindow", "Tao khoa"))
        self.btnSign.setText(_translate("MainWindow", "Sign"))
        self.btnVerify.setText(_translate("MainWindow", "Verify"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
