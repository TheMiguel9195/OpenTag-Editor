"""
Author: Miguel Molina Galán
Date: 12 March 2026

main.py file for project OpenTag Editor
"""

import sys
from PyQt5.QtWidgets import QApplication
from view import MainWindow
from controller import Controller
from model import Model

if __name__ == "__main__":

    app = QApplication(sys.argv) #inicializamos PyQt5

    view = MainWindow() #creamos instancia de la ventana que se encuentra en view.py
    controller = Controller() #instancia de Controller
    model = Model() #instancia de Model

    view.controller = controller #permitimos el acceso del view al controller para llamar funciones
    controller.model = model #acceso del controller para llamar funciones del model
    controller.view = view #acceso del controller para llamar funciones del view

    view.show() #mostramos la ventana
    
    sys.exit(app.exec())