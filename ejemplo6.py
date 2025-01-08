import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QComboBox, QLabel, QPushButton)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráficas Matemáticas")

        self.layout = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["Función Seno", "Función Coseno", "Función Exponencial"])
        self.combo.currentIndexChanged.connect(self.plot_function)
        self.layout.addWidget(self.combo)

        # Matplotlib Canvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)


        self.setLayout(self.layout)

    def plot_function(self, index):
      self.figure.clear() # Limpiar la figura anterior
      ax = self.figure.add_subplot(111)

      if index == 0:
          x = np.linspace(0, 10, 100)
          y = np.sin(x)
          ax.plot(x, y)
          ax.set_title("Función Seno")

      elif index == 1:
          x = np.linspace(0, 10, 100)
          y = np.cos(x)
          ax.plot(x, y)
          ax.set_title("Función Coseno")

      elif index == 2:
          x = np.linspace(0, 5, 100)
          y = np.exp(x)
          ax.plot(x, y)
          ax.set_title("Función Exponencial")

      self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())