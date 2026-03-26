"""
Author: Miguel Molina Galán
Date: 12 March 2026

controller.py file for project OpenTag Editor
"""

class Controller:

    def __init__(self, view):
        self.view = view #Referencia a la interfaz para poder actualizarla
        self.current_file = None #Guardamos fichero actual
    

    def open_music_controller(self):
        print("Llamada a open_music_controller recibida")