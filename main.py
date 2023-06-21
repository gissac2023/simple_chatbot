from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, \
    QPushButton, QApplication
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        self.chatbot = Chatbot()
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
        self.input_field.returnPressed.connect(self.send_message)

        # add button
        self.button = QPushButton("send", self)
        self.button.setGeometry(560, 370, 60, 60)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'> Me: {user_input}</p>")
        self.input_field.clear()
        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()


    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style=#333333; background-color:#E9E9E9'> BOT: {response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
