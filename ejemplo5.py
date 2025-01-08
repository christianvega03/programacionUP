import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mi Primera Aplicación PyQt')
        self.button = QPushButton('Haz clic aquí', self)
        self.button.setGeometry(100, 50, 100, 30) 
        self.button.clicked.connect(self.mostrar_mensaje)
        self.label = QLabel('Mensaje', self)
        self.setGeometry(300, 300, 300, 200)

    def mostrar_mensaje(self):
        self.label.setText('Hecho!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())