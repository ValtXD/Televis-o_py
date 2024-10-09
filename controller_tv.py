# televisao.py

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 1

    def ligar(self):
        if not self.ligada:
            self.ligada = True
            return "TV ligada."
        else:
            return "A TV já está ligada."

    def desligar(self):
        if self.ligada:
            self.ligada = False
            return "TV desligada."
        else:
            return "A TV já está desligada."

    def mudar_canal(self, novo_canal):
        if self.ligada:
            self.canal = novo_canal
            return f"Canal mudado para {self.canal}."
        else:
            return "A TV está desligada. Não é possível mudar de canal."

    def aumentar_volume(self):
        if self.ligada:
            self.volume += 1
            return f"Volume aumentado para {self.volume}."
        else:
            return "A TV está desligada. Não é possível ajustar o volume."

    def diminuir_volume(self):
        if self.ligada:
            self.volume -= 1
            return f"Volume diminuído para {self.volume}."
        else:
            return "A TV está desligada. Não é possível ajustar o volume."
