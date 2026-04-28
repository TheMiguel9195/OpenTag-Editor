"""
Author: Miguel Molina Galán
Date: 12 March 2026

view.py file for project OpenTag Editor
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QAction, QLineEdit, QGridLayout, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Window Title
        self.setWindowTitle("OpenTag Editor")

        #Window Size
        self.setGeometry(100, 100, 800, 800)

        #Application Icon
        self.setWindowIcon(QIcon("./assets/AppIcon.png"))

        #inicializar controller
        self.controller = None

        #bytes de el cover de la cancion abierta
        self.raw_cover_data = None



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

        date_label = QLabel("Fecha:")
        self.date_input = QLineEdit()
        date_label.setAlignment(Qt.AlignCenter)

        genre_label = QLabel("Género:")
        self.genre_input = QLineEdit()
        genre_label.setAlignment(Qt.AlignCenter)

        comment_label = QLabel("Comentario:")
        self.comment_input = QLineEdit()
        comment_label.setAlignment(Qt.AlignCenter)

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

        grid.addWidget(date_label, 4, 0)
        grid.addWidget(self.date_input, 4, 1)

        grid.addWidget(genre_label, 5, 0)
        grid.addWidget(self.genre_input, 5, 1)

        grid.addWidget(comment_label, 6, 0)
        grid.addWidget(self.comment_input, 6, 1)

        grid.addWidget(self.cover_button, 7, 0)

        grid.addWidget(self.save_button, 8, 0)


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
        self.date_input.setEnabled(False)
        self.genre_input.setEnabled(False)
        self.comment_input.setEnabled(False)

        self.cover_button.setEnabled(False)
        self.save_button.setEnabled(False)

        #INPUTS------------------------------


    def open_music(self):

        #print("llamada a abrir pista, OpenTag Editor")

        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Pista", "", "Audio format (*.mp3 *.flac)")

        if file_path and self.controller: #comprobamos que se tenga acceso al controller desde el view, deberiamos tenerlo porque se realiza en el main en la ejecucion del programa
            self.controller.open_music_controller(file_path) #Llamada a open_music_controller

    def load_metadata(self, metadata):

        #mostramos la informacion en la vista

        self.artist_input.setText(metadata["artist"])
        self.title_input.setText(metadata["title"])
        self.album_input.setText(metadata["album"])
        self.track_input.setText(metadata["track"])
        self.date_input.setText(metadata["date"])
        self.genre_input.setText(metadata["genre"])
        self.comment_input.setText(metadata["comment"])

        #mostramos caratula si la tiene

        if metadata["cover"]:

            self.raw_cover_data = metadata["cover"] #guardamos raw bytes de la imagen

            pixmap = QPixmap()
            pixmap.loadFromData(metadata["cover"])
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.cover_preview.setPixmap(pixmap)

        else:

            self.cover_preview.setText("No cover loaded")

        #habilitamos los campos para poder editar los metadatos ahora que ya estan cargados

        self.artist_input.setEnabled(True)
        self.title_input.setEnabled(True)
        self.album_input.setEnabled(True)
        self.track_input.setEnabled(True)
        self.date_input.setEnabled(True)
        self.genre_input.setEnabled(True)
        self.comment_input.setEnabled(True)

        self.cover_button.setEnabled(True)
        self.save_button.setEnabled(True)


    def close_app(self):
        self.close() #cerramos el programa

    def save_data(self):

        #print("llamada a guardar datos")

        metadata = { #estructura metadata que contiene los campos que queremos guardar para llevarlo al model y guardar en el respectivo fichero

            "title": "",
            "artist": "",
            "album": "",
            "track": "",
            "cover": None, #bytes de la imagen
            "date": "",
            "genre": "",
            "comment": ""

        }

        metadata["title"] = self.title_input.text()
        metadata["artist"] = self.artist_input.text()
        metadata["album"] = self.album_input.text()
        metadata["track"] = self.track_input.text()
        metadata["date"] = self.date_input.text()
        metadata["genre"] = self.genre_input.text()
        metadata["comment"] = self.comment_input.text()
        
        if self.cover_preview.text() != "No cover loaded":
            metadata["cover"] = self.raw_cover_data #en caso de haber cambiado imagen seran los bytes de la nueva imagen y no la caratula original // en caso contrario se guarda exactamente los datos de la caratula original

        bool ; correcto = False#variable para comprobar si se guardo correctamente

        correcto = self.controller.save_data_controller(metadata) #pasamos toda la info al controller

        if correcto == True:

            messageBox_exito()

        else:

            messageBox_error()




    def modify_cover(self):

        #print("llamada a cambiar carátula")

        new_cover_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Carátula", "", "Image format (*.jpg *.jpeg *.png)") #seleccionamos la imagen nueva para carátula

        #abrimos la imagen
        if new_cover_path:

            with open(new_cover_path, "rb") as f:

                self.raw_cover_data = f.read() #guardamos los bytes de la nueva imagen en nuestra variable raw_cover_data

            pixmap = QPixmap() #creamos pixmap de la nueva imagen y lo mostramos en cover_preview para enseñar la nueva caratula antes de guardar
            pixmap.loadFromData(self.raw_cover_data)
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.cover_preview.setPixmap(pixmap)


def messageBox_exito():

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Éxito")
    msg.setText("Los metadatos se han almacenado correctamente")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

def messageBox_error():

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle("Error")
    msg.setText("Se ha producido un error al guardar los metadatos del fichero")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())