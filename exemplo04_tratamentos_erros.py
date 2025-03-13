def tratar_erro_conversao_string_nao_inteira():
    # Tentar executar um trecho de código que sabemos que poderá acontecer algum erro
    try: # tente
        # convertendo o que o usuário digitou de str para int e sabemos que pode acontecer algum erro
        numero = int(input("Digite o número: "))
    except Exception as erro: # quando ocorrer algum erro executa o código daqui de dentro do except
        print("Deu erro na conversão do número")
        # Caso desejar apresentar a mensagem do erro
        print("Mensagem do erro: ", erro)

    # Apresentar essa mensagem dando erro ou não
    print("Programa finalizado com sucesso")


def tratar_divisao_com_multiplos_except():
    try:
        numero1 = int(input("Digite o número 1: "))
        numero2 = int(input("Digite o número 2: "))
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    except ZeroDivisionError as erro: # cai aqui quando ocorrer erro na divisão
        print("Não é possível realizar a divisão por 0")
    except ValueError as erro: # cai aqui quando ocorrer erro na conversão
        print("Não foi possível converter o número para inteiro")
    except Exception as erro: # cai aqui com qualquer tipo de erro, caso n tiver sido tratado nos excepts anteriores
        print("Ocorreu um erro inesperado")

    print("Encerrou a aplicação com sucesso")


# ✔ Solicitar até que o usuário digite sair
# ✔ Solicitar os seguintes dados:
#   ✔ - nome do curso: str
#   ✔   Validar min: 8
#   ✔   Validar max: 20
#   ✔ - quantidade_alunos: int
#   ✔   Validar erro de conversão (try except)
#   ✔   Validar min: 5
#   ✔   Validar max: 20

def exemplo_curso():
    opcao: str = ""
    while opcao.strip().upper() != "SAIR":
        # Solicitar os dados do nome do curso
        nome: str = input("Digite o nome do curso: ").strip()
        while len(nome) < 8 or len(nome) >20:
            print("Nome deve conter no mínimo 8 e máximo 20 caracteres")
            nome = input("Digite o nome do curso:  ").strip()
        
        quantidade_alunos: int = 0
        quantidade_valida = False
        while quantidade_valida == False:
            try:
                quantidade_alunos: int = int(input("Digite a quantidade de alunos:  "))
                # if quantidade_alunos < 5 or quantidade_alunos > 20:
                #    print("A quantidade mínima de alunos é 5 e a máxima é 20")
                #    continue

                if quantidade_alunos < 5:
                    print("A quantidade mínima de alunos para uma turma é 5")
                    continue

                if quantidade_alunos > 20:
                    print("A quantidade máxima de alunos para uma turma é 20")
                    continue

                quantidade_valida = True
            except Exception as erro:
                print("A quantidade de alunos deve ser um número inteiro")

        opcao = input("Pressione enter para continuar ou digite 'sair' para encerrar")


# Ex. 1: Solicitar um número inteiro e apresentar se ele é menor que 15 ou maior que 15

def exercicio_01():

    numero = int(input("Digite um numero: "))
    if numero > 15:
        print("O número e maior que 15 !")
    else:
        print("Número e menor que 15 !")


# Ex. 2: Solicitar o nome de um animal e apresentar a quantidade de caracteres

def exercicio_02():
    nome = input("Digite o nome de um animal:  ")
    print("O nome",nome, "contém", len(nome), "caracteres !")


# Ex. 3: Solicitar um texto, remover espaços do começo transformando em minúsculo

def exercicio_03():
    texto = input("Digite um texto :  ")
    print(texto.lstrip().lower())


# Ex. 4: Solicitar o nome de uma empresa e remover o texto 'LTDA', assim como, 'SA'.

def exercicio_04():

    empresa = input("Digite o nome de uma empresa :  ")
    empresa2 = empresa.upper().replace("LTDA", "").replace("SA", "")
    print(empresa2)


# Ex. 5: Solicitar o nome do curso e apresentar se o curso começa com SuperDev, caso contrário apresentar que não começa com SuperDev

def exercicio_05():
    nome_curso = input("Digite o nome do curso :  ")

    if nome_curso.upper().startswith("SUPERDEV"):
      print("Curso começa com SuperDev")
    else:
      print("Não começa com SuperDev")



# Ex. 6: Solicitar uma idade e apresentar se é:
#   - Adulto
#   - Criança
#   - Adolescente
#   - Idoso

def exercicio_06():
    idade = int(input("Digite a Idade do malandro :  "))

    if idade <= 12 :
     print("E uma Criânça !")
    elif idade > 12 or idade < 19:
     print("E um Adolescente !")
    elif idade > 19 or idade < 64:
     print("E um Adulto !")
    else:
        print("E um idoso !")


if __name__ == "__main__":
    import os
    os.system("cls")
    exercicio_06()