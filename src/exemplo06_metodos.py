
# métod com retorno do tipo int
def somar() -> int:
    numero1 = 10
    numero2 = 20
    soma = numero1 + numero2
    return soma

# método sem retorno
def calculadora():
    solicitar_nome()
    # chama o método somar e armazena a soma dos dois número
    resultado = somar()
    print("Soma:", resultado)


# Método sem retorno
# Reponsabilidade do método: solicitar o nome garantindo no mínimo 3 carac
def solicitar_nome() -> str:
    nome_solicitado = input("Digite o nome: ").strip()
    while len(nome_solicitado) < 3:
        print("Nome inválido, deve conter no mínimo 3 caracteres")
        nome_solicitado = input("Digite o nome: ").strip()
    return nome_solicitado


# Método com retorno do tipo string
# Responsabilidade do método: solicitar o sobrenome garantindo no mínimo 3 máximo 100
def solicitar_sobrenome() -> str:
    sobrenome_solicitado = input("Digite o sobrenome: ").strip()
    while len(sobrenome_solicitado) < 3 or len(sobrenome_solicitado) > 100:
        print("Sobrenome inválido, deve conter no mínimo 3 caracteres e no máximo 100")
        sobrenome_solicitado = input("Digite o sobrenome: ").strip()
    return sobrenome_solicitado


# Método sem retorno
def apresentar_nome_completo():
    # Executando o método solicitar_nome() e armazenando seu retorno na variável nome
    nome = solicitar_nome()
    # Executando o método solicitar_sobrenome() e armazenando seu retorno na variável sobrenome
    sobrenome = solicitar_sobrenome()

    nome_completo = nome + " " + sobrenome
    print("Nome completo: ", nome_completo)


# Exercício:
# Criar uma função solicitar_modelo min: 4, retornando o modelo
# Criar uma função solicitar_quantidade min: 1 max: 5, retornando a quantidade
# Criar uma função solicitar_preco min: 100, max: 500, retornando o preco
# Criar uma função solicitar_calcular_produto, chamando as funções e armazenar em variáveis
# Apresentar o total e as variáveis


if __name__ == "__main__":
    import os 
    os.system("cls")
    apresentar_nome_completo()
