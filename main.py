"""
Author: Miguel Molina Galán
Date: 12 March 2026

main.py file for project OpenTag Editor
"""

import sys
from PyQt5.QtWidgets import QApplication
from view import MainWindow
from controller import Controller

if __name__ == "__main__":

    app = QApplication(sys.argv) #inicializamos PyQt5

    view = MainWindow() #creamos instancia de la ventana que se encuentra en view.py
    view.show() #mostramos la ventana

    controller = Controller(view) #inicializamos el controller
    view.controller = controller #instancia del controller en el view para poder realizar llamadas

    sys.exit(app.exec())