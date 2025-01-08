import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFileDialog, QComboBox)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
import os


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análisis de Datos CSV")
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # Botón para cargar el archivo CSV
        hbox_load = QHBoxLayout()
        self.load_button = QPushButton("Cargar Archivo CSV")
        self.load_button.clicked.connect(self.load_csv)
        hbox_load.addWidget(self.load_button)
        vbox.addLayout(hbox_load)

        # Área para mostrar los histogramas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        vbox.addWidget(self.canvas)

        # Área para mostrar estadísticas
        self.stats_label = QLabel("")
        vbox.addWidget(self.stats_label)

        # Botón para guardar la gráfica
        hbox_save_plot = QHBoxLayout()
        self.save_plot_button = QPushButton("Guardar Gráfica")
        self.save_plot_button.clicked.connect(self.save_plot)
        self.save_plot_button.setEnabled(False) # Deshabilitado hasta cargar datos
        hbox_save_plot.addWidget(self.save_plot_button)
        vbox.addLayout(hbox_save_plot)

        # Botón para exportar a Excel
        hbox_export = QHBoxLayout()
        self.export_button = QPushButton("Exportar a Excel")
        self.export_button.clicked.connect(self.export_excel)
        self.export_button.setEnabled(False) # Deshabilitado hasta cargar datos
        hbox_export.addWidget(self.export_button)
        vbox.addLayout(hbox_export)


        self.setLayout(vbox)

    def load_csv(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo CSV", "",
                                                  "Archivos CSV (*.csv);;Todos los archivos (*)", options=options)
        if file_name:
            try:
                self.df = pd.read_csv(file_name)
                self.plot_data()
                self.show_stats()

                # Habilitar botones
                self.save_plot_button.setEnabled(True)
                self.export_button.setEnabled(True)

            except pd.errors.ParserError:
                print("Error al analizar el archivo CSV.")
            except Exception as e:
                print(f"Error: {e}")
    
    def plot_data(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        try:
            ax.hist(self.df['ActivePower'], alpha=0.5, label='ActivePower')
            ax.hist(self.df['WindSpeed'], alpha=0.5, label='WindSpeed')
            ax.hist(self.df['AmbientTemperatue'], alpha=0.5, label='AmbientTemperatue')
        except KeyError as e:
            print(f"Error: La columna '{e}' no existe en el archivo CSV.")
            return

        ax.legend()
        ax.set_title('Histogramas de Datos')
        self.canvas.draw()


    def show_stats(self):
        try:
            stats = {}
            for col in ['ActivePower', 'WindSpeed', 'AmbientTemperatue']:
                stats[col] = {
                    'Max': self.df[col].max(),
                    'Min': self.df[col].min(),
                    'Promedio': self.df[col].mean(),
                    'Desviación Estándar': self.df[col].std()
                }
            stats_text = ""
            for col, values in stats.items():
                stats_text += f"{col}:\n"
                for stat_name, stat_value in values.items():
                    stats_text += f"  {stat_name}: {stat_value:.2f}\n"
            self.stats_label.setText(stats_text)
        except KeyError as e:
              print(f"Error: La columna '{e}' no se encontró en el DataFrame.")  


    def save_plot(self):
      options = QFileDialog.Options()
      file_name, _ = QFileDialog.getSaveFileName(self, "Guardar Gráfica", "",
                                              "Archivos PNG (*.png);;Todos los archivos (*)", options=options)
      if file_name:
          self.figure.savefig(file_name)

    def export_excel(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Exportar a Excel", "",
                                                  "Archivos Excel (*.xlsx);;Todos los archivos (*)", options=options)
        if file_name:
            try:
                # Ordena el DataFrame por 'ActivePower' de mayor a menor
                sorted_df = self.df.sort_values(by='ActivePower', ascending=False)
                sorted_df.to_excel(file_name, index=False)  # Guarda sin el índice
            except KeyError:
                print("Error: La columna 'ActivePower' no se encontró en el DataFrame.")
            except Exception as e:
                print(f"Error al exportar a Excel: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())