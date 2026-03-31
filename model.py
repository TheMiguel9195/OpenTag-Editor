"""
Author: Miguel Molina Galán
Date: 12 March 2026

model.py file for project OpenTag Editor
"""

from mutagen.mp3 import MP3
from mutagen.flac import FLAC, Picture
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TRCK, TDRC, TCON, COMM

class Model:

    def __init__(self):

        self.comment_key = None #Guarda exactamente en cual COMM:xxx esta el comentario para poder reescribir el mismo comentario (esto es solo para ficheros .mp3)

    def read_metadata(self, file_path): #funcion que obtendra los metadatos del fichero del file_path

        print("Llamada a read_metadata con file_path: " + file_path)

        metadata = { #estructura metadata que contiene los campos que queremos obtener

            "title": "",
            "artist": "",
            "album": "",
            "track": "",
            "cover": None, #bytes de la imagen
            "date": "",
            "genre": "",
            "comment": ""

        }

        if file_path.endswith(".mp3"):
            
            audio = MP3(file_path, ID3 = ID3)
            tags = audio.tags

            if tags:

                metadata["title"] = str(tags.get("TIT2", ""))
                metadata["artist"] = str(tags.get("TPE1", ""))
                metadata["album"] = str(tags.get("TALB", ""))
                metadata["track"] = str(tags.get("TRCK", ""))
                metadata["date"] = str(tags.get("TDRC", ""))
                metadata["genre"] = str(tags.get("TCON", ""))
                
                for tag, value in tags.items(): #el tag COMM distingue idioma ej(COMM:eng, COMM:esp, COMM:xxx) esto escoge aquel que ya contega informacion ya que normalmente solo se usa alguno de ellos

                    if tag.startswith("COMM") and value.text[0]:

                        self.comment_key = tag #guardamos el codigo COMM:xxx para poder reescribir el mismo al guardar los cambios

                        metadata["comment"] = value.text[0] #si no se encuentra ningun value entonces todos los COMM:xxx son cadena vacia porque la estructura metadata inicializa el campo como cadena vacia
                        break

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
            metadata["date"] = audio.get("date", [""])[0]
            metadata["genre"] = audio.get("genre", [""])[0]
            metadata["comment"] = audio.get("comment", [""])[0]

            if audio.pictures:

                metadata["cover"] = audio.pictures[0].data

        return metadata
    
    def save_data_model(self, metadata, current_file_path):

        print("Llamada recibida a save_data_model con " + current_file_path)

        #identificamos segun el path si el fichero es .mp3 o .flac para distinguir su guardado y finalmente guardamos la informacion

        if current_file_path.endswith(".mp3"):
            
            audio = MP3(current_file_path, ID3=ID3)

            if audio.tags is None:
                audio.add_tags()
            
            audio.tags["TIT2"] = TIT2(encoding = 3, text = metadata["title"])
            audio.tags["TPE1"] = TPE1(encoding = 3, text = metadata["artist"])
            audio.tags["TALB"] = TALB(encoding = 3, text = metadata["album"])
            audio.tags["TRCK"] = TRCK(encoding = 3, text = metadata["track"])
            audio.tags["TDRC"] = TDRC(encoding = 3, text = metadata["date"])
            audio.tags["TCON"] = TCON(encoding = 3, text = metadata["genre"])

            if self.comment_key: #FORMATO DE LA comment_key COMM:desc:lang

                parts = self.comment_key.split(":")

                if len(parts) == 3:

                    lang = parts[2]
                    desc = parts[1]

                else:

                    lang = "eng"
                    desc = ""
            
            audio.tags["COMM"] = COMM(encoding = 3, lang = lang, desc = desc, text = metadata["comment"])

            if metadata["cover"]: #guardamos los bytes de la imagen de la caratula

                audio.tags.delall("APIC") #borramos carátulas existentes

                mime = self.get_mime_type(metadata["cover"])

                audio.tags["APIC:Cover"] = APIC(encoding = 3, mime = mime, type = 3, desc = "Cover", data = metadata["cover"])
            
            audio.save()

        elif current_file_path.endswith(".flac"):

            audio = FLAC(current_file_path)
        
            audio["title"] = metadata["title"]
            audio["artist"] = metadata["artist"]
            audio["album"] = metadata["album"]
            audio["tracknumber"] = metadata["track"]
            audio["date"] = metadata["date"]
            audio["genre"] = metadata["genre"]
            audio["comment"] = metadata["comment"]

            if metadata["cover"]: #para añadir la caratula

                pic = Picture()
                pic.type = 3
                pic.mime = self.get_mime_type(metadata["cover"])
                pic.data = metadata["cover"]

                audio.clear_pictures()
                audio.add_picture(pic)

            audio.save()

    def get_mime_type(self, image_bytes): #detecta si la caratula a guardar es JPEG, JPG o PNG

        if image_bytes[:3] == b'\xff\xd8\xff':  # cabecera JPEG/JPG

            return "image/jpeg"
        
        elif image_bytes[:8] == b'\x89PNG\r\n\x1a\n':  # cabecera PNG

            return "image/png"
        
        else:

            return "image/jpeg"
