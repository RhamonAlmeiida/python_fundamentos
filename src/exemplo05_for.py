import time


def exemplo_for_apresentar_numeros():
    # indice = 0
    # while indice < 5:
    #     print(indice)
    #     indice = indice + 1
    # 
    for indice in range(0, 5):
        print(indice)


def exemplo_for_incrementar_dois_em_dois():
    # Apresentar 0, 3, 6, 9
    for indice in range(0, 10, 3):
        print(indice)


def exemplo_solicitar_dados():
    quantidade_desejada = int(input("Digite a quantidade desejada: "))
    for i in range(0, quantidade_desejada):
        nome = input("Digite o nome: ").strip()
        sobrenome = input("Digite o sobrenome: ").strip()
        nome_completo = nome + " " + sobrenome
        print("Nome completo:", nome_completo)



def exemplo_apresentar_contagem_regresiva():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1) # delay 1
    
def exemplo_relogio():
    # 00:00:00
    # 00:00:01
    # 00:00:59
    # 00:01:00
    # 00:01:01
    # 00:59:59
    # 01:00:00
    for hora in range(0, 24):
        for minuto in range(0, 60):
            for segundo in range(0, 60):
                print(hora, minuto, segundo, sep=":")
                time.sleep(1)

    # for em java
    # for (int hora = 0; hora < 24; hora = hora + 1)


if __name__ == "__main__":
    import os 
    os.system("cls")
    exemplo_relogio()