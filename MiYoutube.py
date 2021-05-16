import pytchat
import threading

LineaSuper = '-super-'
LineaMiembro = '-mienbro-'
LineaNormal = '-normal-'


class MiYoutube(object):
    def __init__(self, Ventana):
        self.conectado = False
        self.Chat = None
        self.Ventana = Ventana

    def Conectar(self, ID_Youtube):
        if(ID_Youtube != ''):
            print(f"Intentando Conectar a https://youtu.be/{ID_Youtube}")

            self.ID_Youtube = ID_Youtube
            # TODO: Agregar try
            try:
                self.chat = pytchat.create(video_id=self.ID_Youtube)
                self.conectado = True
                self.HiloChat = threading.Thread(target=self.Actualizar, daemon=True)
                self.HiloChat.start()
                print("Conectado ChatYoutube")
            except:
                print("No se puedo conectar Chat de Youtube")
                self.conectado = False
        else:
            self.conectado = False

    def EscucharChat(self):
        pass

    def Actualizar(self):
        if self.conectado:
            while self.chat.is_alive():
                for c in self.chat.get().sync_items():
                    Nivel = LineaNormal
                    if(c.author.isChatSponsor):
                        Nivel = LineaMiembro
                    if(c.type == "superChat"):
                        Nivel = LineaNormal
                    print(f"{c.datetime} - [{c.type}] [{c.author.name}]- {c.message}")

                    self.Ventana[Nivel].print(f"{c.datetime} [{c.author.name}] {c.message}")
