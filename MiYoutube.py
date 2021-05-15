import pytchat


class MiYoutube(object):
    def __init__(self):
        self.conectado = False
        self.Chat = None

    def Conectar(self, ID_Youtube):
        if(ID_Youtube != ''):
            print(f"Intentando Conectar a https://youtu.be/{ID_Youtube}")
            self.conectado = True
            self.ID_Youtube = ID_Youtube
            # TODO: Agregar try
            self.chat = pytchat.create(video_id=self.ID_Youtube)
        else:
            self.conectado = False

    def Actualizar(self):
        pass
