from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, \
    QPushButton, QApplication
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot")

        self.setMinimumSize(700, 500)
        # add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(60, 30, 480, 320)
        self.chat_area.setReadOnly(True)
        # add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(60, 370, 480, 60)

        # add button
        self.button = QPushButton("send", self)
        self.button.setGeometry(560, 370, 60, 60)


        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())

