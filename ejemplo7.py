import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFileDialog)
from PyQt5.QtGui import QPixmap, QImage
import numpy as np

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Transformation")
        self.initUI()

    def initUI(self):
        vbox = QHBoxLayout()

        hbox1 = QHBoxLayout()
        self.original_label = QLabel("Original Image")
        hbox1.addWidget(self.original_label)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        self.transformed_label = QLabel("Transformed Image")
        hbox2.addWidget(self.transformed_label)
        vbox.addLayout(hbox2)


        hbox3 = QHBoxLayout()
        open_button = QPushButton("Open Image")
        open_button.clicked.connect(self.open_image)
        hbox3.addWidget(open_button)
        save_button = QPushButton("Save Image")
        save_button.clicked.connect(self.save_image)
        hbox3.addWidget(save_button)
        vbox.addLayout(hbox3)
        self.setLayout(vbox)

    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                  "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.original_image = QPixmap(file_name)
            self.original_label.setPixmap(self.original_image.scaled(400, 400))  # Escala la imagen

            # Convertir QPixmap a formato utilizable para la transformacion
            image = self.original_image.toImage()
            width = image.width()
            height = image.height()
            self.image_data = np.zeros((height, width, 3), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = image.pixelColor(x,y)
                    self.image_data[y, x] = [color.red(), color.green(), color.blue()]


            # Transformar imagen
            self.transformed_image_data = self.transform_image(self.image_data)

            # Convertir de nuevo a QPixmap
            transformed_image = QImage(self.transformed_image_data.data, width, height, 3*width, QImage.Format_RGB888)
            self.transformed_pixmap = QPixmap(transformed_image)
            self.transformed_label.setPixmap(self.transformed_pixmap.scaled(400, 400)) # Escala la imagen

    def transform_image(self, image_data):
        # Ejemplo de transformación: invertir los colores
        transformed_data = 255 - image_data
        return transformed_data


    def save_image(self):
        if hasattr(self, 'transformed_image_data'):
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self,"Save Image","","PNG Files (*.png);;JPG Files (*.jpg);;All Files (*)", options=options)
            if file_name:
                height, width, channel = self.transformed_image_data.shape
                image = QImage(self.transformed_image_data.data, width, height, 3 * width, QImage.Format_RGB888)
                image.save(file_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())