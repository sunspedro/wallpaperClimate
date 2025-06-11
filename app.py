# app.py
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt

class VelocidadeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuração de Velocidade")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label_boas_vindas = QLabel("Seja bem-vindo")
        self.label_boas_vindas.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_boas_vindas)

        self.label_pergunta = QLabel("Qual velocidade de troca você gostaria? (em segundos)")
        self.label_pergunta.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_pergunta)

        self.input_velocidade = QLineEdit()
        self.input_velocidade.setPlaceholderText("Digite a velocidade em segundos")
        layout.addWidget(self.input_velocidade)

        self.botao_submit = QPushButton("Confirmar")
        self.botao_submit.clicked.connect(self.submit_velocidade)
        layout.addWidget(self.botao_submit)

        self.setStyleSheet("""
            QWidget {
                background: #D6EFFF;
            }

            QLabel {
                font-size: 16px;
                color: #2C3E50;
            }

            QLineEdit {
                background-color: transparent;
                padding: 5px;
                color: #2C3E50;
                border: 1px solid #2C3E50;
                border-radius: 8px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #FFA69E;
                color: white;
                padding: 6px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #FF8C7A;
            }
        """)

        self.setLayout(layout)

    def submit_velocidade(self):
        valor = self.input_velocidade.text()
        try:
            segundos = float(valor)
            with open("delay.cfg", "w") as f:
                f.write(str(segundos))
            QMessageBox.information(
                self, "Velocidade Confirmada",
                f"Velocidade escolhida: {segundos} segundos."
            )
            print(f"Velocidade definida: {segundos} segundos")
        except ValueError:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, digite um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = VelocidadeApp()
    janela.show()
    sys.exit(app.exec_())
