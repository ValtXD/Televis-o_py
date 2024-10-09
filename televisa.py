class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 10

    def ligar(self):
        if not self.ligada:
            self.ligada = True
            print("TV ligada.")
        else:
            print("A TV já está ligada.")

    def desligar(self):
        if self.ligada:
            self.ligada = False
            print("TV desligada.")
        else:
            print("A TV já está desligada.")

    def mudar_canal(self, novo_canal):
        if self.ligada:
            self.canal = novo_canal
            print(f"Canal mudado para {self.canal}.")
        else:
            print("A TV está desligada. Não é possível mudar de canal.")

    def aumentar_volume(self):
        if self.ligada:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}.")
        else:
            print("A TV está desligada. Não é possível ajustar o volume.")

    def diminuir_volume(self):
        if self.ligada:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}.")
        else:
            print("A TV está desligada. Não é possível ajustar o volume.")

# Exemplo de uso
    #if __name__ == "__main__":
    #tv = Televisao()

    #tv.ligar()
    #tv.mudar_canal(5)
    #tv.aumentar_volume()
    #tv.diminuir_volume()
    #tv.desligar()

