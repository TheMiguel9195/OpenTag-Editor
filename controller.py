"""
Author: Miguel Molina Galán
Date: 12 March 2026

controller.py file for project OpenTag Editor
"""

class Controller:

    def __init__(self): #CONSTRUCTOR
        self.view = None
        self.model = None
        self.current_file = None
    

    def open_music_controller(self, file_path):

        print("Llamada a open_music_controller recibida, La ruta recibida donde se encuentra el fichero es: " + file_path)

        metadata = self.model.read_metadata(file_path) #aqui llamamos a la funcion de read_metadata de model.py que se encargara de abrir el fichero de audio y devolver los metadatos

        self.view.load_metadata(metadata)