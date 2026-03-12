"""
Author: Miguel Molina Galán
Date: 12 March 2026

main.py file for project OpenTag Editor
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QAction
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Window Title
        self.setWindowTitle("OpenTag Editor")

        #Window Size
        self.setGeometry(100, 100, 800, 800)



        # SUPERIOR BAR MENU---------------------------------------------------------

        menu_bar = self.menuBar()

        # MAIN MENU
        file_menu = menu_bar.addMenu("Fichero")

        # OPEN FILE
        open_action = QAction("Abrir pista", self)
        open_action.triggered.connect(self.open_music)
        file_menu.addAction(open_action)

        # CLOSE APPLICATION
        exit_action = QAction("Salir de la aplicación", self)
        exit_action.triggered.connect(self.close_app)
        file_menu.addAction(exit_action)

        #SUPERIOR BAR MENU----------------------------------------------------------



        #LAYOUT MainWindow----------------------------------------------------------

        #LAYOUT MainWindow----------------------------------------------------------



        # Crear layout principal
        layout = QVBoxLayout()

        # Contenedor central
        container = QWidget()
        container.setLayout(layout)

        # Asignar contenedor al QMainWindow
        self.setCentralWidget(container)

    def open_music(self):
        print("llamada a abrir pista, OpenTag Editor")

    def close_app(self):
        self.close() #cerramos el programa


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())