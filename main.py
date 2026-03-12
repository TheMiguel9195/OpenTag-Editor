"""
Author: Miguel Molina Galán
Date: 12 March 2026

main.py file for project OpenTag Editor
"""

import sys
from PyQt5.QtWidgets import QApplication
from view import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv) #inicializamos PyQt5
    window = MainWindow() #creamos instancia de la ventana que se encuentra en view.py
    window.show() #mostramos la ventana
    sys.exit(app.exec())