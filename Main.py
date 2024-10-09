from televisa import Televisao


def main():
    tv = Televisao()

    while True:
        print("\n--- Controle da Televisão ---")
        print("1. Ligar TV")
        print("2. Desligar TV")
        print("3. Mudar Canal")
        print("4. Aumentar Volume")
        print("5. Diminuir Volume")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tv.ligar()
        elif escolha == '2':
            tv.desligar()
        elif escolha == '3':
            novo_canal = int(input("Digite o número do canal: "))
            tv.mudar_canal(novo_canal)
        elif escolha == '4':
            tv.aumentar_volume()
        elif escolha == '5':
            tv.diminuir_volume()
        elif escolha == '6':
            print("Encerrando o controle da TV.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()