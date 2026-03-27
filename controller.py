"""
Author: Miguel Molina Galán
Date: 12 March 2026

controller.py file for project OpenTag Editor
"""

class Controller:

    def __init__(self): #CONSTRUCTOR
        self.view = None
        self.model = None
        self.current_file_path = None
    

    def open_music_controller(self, file_path):

        print("Llamada a open_music_controller recibida, La ruta recibida donde se encuentra el fichero es: " + file_path)

        self.current_file_path = file_path #guardamos el file path para poder usarlo cuando sea necesario

        metadata = self.model.read_metadata(file_path) #aqui llamamos a la funcion de read_metadata de model.py que se encargara de abrir el fichero de audio y devolver los metadatos

        self.view.load_metadata(metadata)

    def save_data_controller(self, metadata):

        print("Llamada a save_data_controller recibida")

        if metadata and self.current_file_path:

            self.model.save_data_model(metadata, self.current_file_path) #pasamos donde se encuentra el fichero cuyos datos van a ser modificados y pasamos los nuevos datos
        
        