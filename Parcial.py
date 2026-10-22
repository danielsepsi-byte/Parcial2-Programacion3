import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class VentanaConsultoria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard de Inventario - Sucursales")
        self.setGeometry(100, 100, 800, 600)

        # Cargar los datos generados
        self.df = pd.read_csv('inventario_sucursales_elsalvador.csv')

        # Configurar el widget central y el layout
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)

        # Configurar Matplotlib dentro de PyQt5
        self.figura, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figura)
        layout.addWidget(self.canvas)

        self.graficar_inventario()

    def graficar_inventario(self):
        # Agrupar por sucursal y sumar las cantidades
        datos_agrupados = self.df.groupby('Sucursal')['Cantidad_Stock'].sum()
        datos_agrupados.plot(kind='bar', ax=self.ax, color='#1f77b4', edgecolor='black')
        
        self.ax.set_title('Volumen Total de Productos por Sucursal')
        self.ax.set_ylabel('Cantidad de Unidades')
        self.ax.set_xlabel('Sucursal')
        self.ax.tick_params(axis='x', rotation=0)
        self.figura.tight_layout()
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaConsultoria()
    ventana.show()
    sys.exit(app.exec_())