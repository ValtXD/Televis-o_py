import tkinter as tk

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 10

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

# Funções de controle
def ligar_tv():
    resultado = tv.ligar()
    atualizar_status(resultado)

def desligar_tv():
    resultado = tv.desligar()
    atualizar_status(resultado)

def mudar_canal():
    try:
        novo_canal = int(entry_canal.get())
        resultado = tv.mudar_canal(novo_canal)
        atualizar_status(resultado)
    except ValueError:
        atualizar_status("Canal inválido. Digite um número.")

def aumentar_volume():
    resultado = tv.aumentar_volume()
    atualizar_status(resultado)

def diminuir_volume():
    resultado = tv.diminuir_volume()
    atualizar_status(resultado)

def atualizar_status(mensagem):
    label_status.config(text=mensagem)

# Inicializando a televisão
tv = Televisao()

# Criando a interface gráfica
root = tk.Tk()
root.title("Controle da Televisão")

# Layout de Controle Remoto
frame_controle = tk.Frame(root, padx=20, pady=20)
frame_controle.grid(row=0, column=0)

# Botões de controle
btn_ligar = tk.Button(frame_controle, text="Ligar TV", command=ligar_tv, width=10)
btn_ligar.grid(row=0, column=0, columnspan=2, pady=5)

btn_desligar = tk.Button(frame_controle, text="Desligar TV", command=desligar_tv, width=10)
btn_desligar.grid(row=0, column=2, columnspan=2, pady=5)

label_canal = tk.Label(frame_controle, text="Canal:")
label_canal.grid(row=1, column=0, pady=5)

entry_canal = tk.Entry(frame_controle, width=5)
entry_canal.grid(row=1, column=1, pady=5)

btn_mudar_canal = tk.Button(frame_controle, text="Mudar Canal", command=mudar_canal)
btn_mudar_canal.grid(row=1, column=2, columnspan=2, pady=5)

btn_aumentar_volume = tk.Button(frame_controle, text="Volume +", command=aumentar_volume, width=10)
btn_aumentar_volume.grid(row=2, column=0, columnspan=4, pady=5)

btn_diminuir_volume = tk.Button(frame_controle, text="Volume -", command=diminuir_volume, width=10)
btn_diminuir_volume.grid(row=3, column=0, columnspan=4, pady=5)

# Label de status
label_status = tk.Label(root, text="Status: TV Desligada", pady=10)
label_status.grid(row=1, column=0, pady=5)

# Executando a interface
root.mainloop()
