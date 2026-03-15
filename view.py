"""
Author: Miguel Molina Galán
Date: 12 March 2026

view.py file for project OpenTag Editor
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QAction, QLineEdit, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
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



        #LAYOUT---------------------------------------------------------------------
        # Crear layout principal
        main_layout = QVBoxLayout()

        # Contenedor central
        container = QWidget()
        container.setLayout(main_layout)

        # Asignar contenedor al QMainWindow
        self.setCentralWidget(container)

        #Crear layout de cuadricula para los pares de informacion
        grid = QGridLayout()


        #CAMPOS DEL GRID
        artist_label = QLabel("Artista:")
        self.artist_input = QLineEdit()
        artist_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Título:")
        self.title_input = QLineEdit()
        title_label.setAlignment(Qt.AlignCenter)

        album_label = QLabel("Álbum:")
        self.album_input = QLineEdit()
        album_label.setAlignment(Qt.AlignCenter)

        track_label = QLabel("Track:")
        self.track_input = QLineEdit()
        track_label.setAlignment(Qt.AlignCenter)

        self.cover_button = QPushButton("Cambiar carátula")
        self.cover_button.clicked.connect(self.modify_cover)

        self.save_button = QPushButton("Guardar cambios")
        self.save_button.clicked.connect(self.save_data)

        #OTROS CAMPOS
        self.cover_preview = QLabel("No cover loaded")
        self.cover_preview.setAlignment(Qt.AlignCenter)
        self.cover_preview.setFixedSize(250, 250)
        self.cover_preview.setStyleSheet("border: 1px solid gray;")


        #POSICIONES
        grid.addWidget(artist_label, 0, 0)
        grid.addWidget(self.artist_input, 0, 1)

        grid.addWidget(title_label, 1, 0)
        grid.addWidget(self.title_input, 1, 1)

        grid.addWidget(album_label, 2, 0)
        grid.addWidget(self.album_input, 2, 1)

        grid.addWidget(track_label, 3, 0)
        grid.addWidget(self.track_input, 3, 1)

        grid.addWidget(self.cover_button, 4, 0)

        grid.addWidget(self.save_button, 5, 0)


        grid.setVerticalSpacing(20)


        main_layout.addLayout(grid)
        main_layout.addWidget(self.cover_preview, alignment = Qt.AlignCenter)
        main_layout.addStretch()


        #LAYOUT---------------------------------------------------------------------

        #INPUTS------------------------------

        self.artist_input.setEnabled(False)
        self.title_input.setEnabled(False)
        self.album_input.setEnabled(False)
        self.track_input.setEnabled(False)

        self.cover_button.setEnabled(False)
        self.save_button.setEnabled(False)

        #INPUTS------------------------------


    def open_music(self):
        print("llamada a abrir pista, OpenTag Editor")

    def close_app(self):
        self.close() #cerramos el programa

    def save_data(self):
        print("llamada a guardar datos")

    def modify_cover(self):
        print("llamada a cambiar carátula")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())