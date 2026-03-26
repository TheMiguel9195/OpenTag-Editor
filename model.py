"""
Author: Miguel Molina Galán
Date: 12 March 2026

model.py file for project OpenTag Editor
"""

from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, APIC

class Model:

    def __init__(self): #CONSTRUCTOR VACIO

        pass

    def read_metadata(self, file_path): #funcion que obtendra los metadatos del fichero del file_path

        print("Llamada a read_metadata con file_path: " + file_path)

        metadata = { #estructura metadata que contiene los campos que queremos obtener

            "title": "",
            "artist": "",
            "album": "",
            "track": "",
            "cover": None #bytes de la imagen

        }

        if file_path.endswith(".mp3"):
            
            audio = MP3(file_path, ID3 = ID3)
            tags = audio.tags

            if tags:

                metadata["title"] = str(tags.get("TIT2", ""))
                metadata["artist"] = str(tags.get("TPE1", ""))
                metadata["album"] = str(tags.get("TALB", ""))
                metadata["track"] = str(tags.get("TRCK", ""))

                for tag in tags.values():

                    if isinstance(tag, APIC):
                        metadata["cover"] = tag.data
                        break

        elif file_path.endswith(".flac"):

            audio = FLAC(file_path)

            metadata["title"] = audio.get("title", [""])[0]
            metadata["artist"] = audio.get("artist", [""])[0]
            metadata["album"] = audio.get("album", [""])[0]
            metadata["track"] = audio.get("tracknumber", [""])[0]

            if audio.pictures:

                metadata["cover"] = audio.pictures[0].data

        return metadata