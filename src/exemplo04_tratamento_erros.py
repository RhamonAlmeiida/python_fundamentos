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
        while len(nome) < 8 or len(nome) > 20:
            print("Nome deve conter no mínimo 8 e no máximo 20 caracteres")
            nome = input("Digite o nome do curso: ").strip()

        quantidade_alunos: int = 0
        quantidade_valida = False
        while quantidade_valida == False:
            try:
                quantidade_alunos: int = int(input("Digite a quantidade de alunos: "))
                # if quantidade_alunos < 5 or quantidade_alunos > 20:
                #     print("A quantidade mínima de alunos é 5 e a máxima é 20")
                #     continue

                if quantidade_alunos < 5:
                    print("A quantidade mínima de alunos para uma turma é 5")
                    continue
                
                if quantidade_alunos > 20:
                    print("A quantidade máxima de alunos para uma turma é 20")
                    continue

                quantidade_valida = True
            except Exception as erro:
                print("A quantidade de alunos deve ser um número inteiro")

        opcao = input("Pressione enter para continuar ou digite 'sair' para encerrar... ")


if __name__ == "__main__":
    import os 
    os.system("cls")
    exemplo_curso()


# Ex. 1: Solicitar um número inteiro e apresentar se ele é menor que 15 ou maior que 15
# Ex. 2: Solicitar o nome de um animal e apresentar a quantidade de caracteres
# Ex. 3: Solicitar um texto, remover espaços do começo transformando em minúsculo
# Ex. 4: Solicitar o nome de uma empresa e remover o texto 'LTDA', assim como, 'SA'.
# Ex. 5: Solicitar o nome do curso e apresentar se o curso começa com SuperDev, caso contrário apresentar que não começa com SuperDev
# Ex. 6: Solicitar uma idade e apresentar se é:
#   - Adulto
#   - Criança
#   - Adolescente
#   - Idoso
#  UTILIZAR WHILE para estes exercícios abaixo:
# Ex. 7: Solicitar o nome da empresa e verificar se termina com LTDA, apresentar que é uma empresa 'Sociedade de responsabilidade limitada', caso terminar com SA apresentar que é uma empresa 'Sociedade Anônima
# Ex. 8: Solicitar 5 vezes o nome do dia da semana
# Ex. 9: Solicitar o nome da cidade e a quantidade de habitantes para quatro cidades.
# Ex. 10: Solicitar o nome e altura de 6 alunos, descobrir  qual a maior altura e apresentar
# Ex. 11: Solicitar nome e preço de 5 notebooks, descobrir qual o nome e o valor do notebook que tem o menor preço
# Ex. 12: Solicitar o preço do petróleo e tratar o erro (neste não precisa de while, somente try/except)
# Ex. 12: Solicitar o peso da carne e tratar o erro (neste precisa de while e try/except)
# Ex. 13: Solicitar o salário do pedreiro (neste precisa de while e try/catch), passos para resolver:
#         Solicitar o salário
#         Adicionar o try/except
#         Fazer com que repita com while
#         Validar que o salário mínimo é de R$ 4000,00
#         Validar que o salário máximo é R$ 15000,00
# Ex. 13: Solicitar nome do projeto, categoria e seu custo, apresentar conforme abaixo:
#           - Quantidade de projetos da categoria 'Cross Fit'
#           - Quantidade de projetos da categoria 'Pilates'
#           - Quantidade de projetos da categoria 'Fisioculturismo'
# Ex. 14: Solicitar nome, nota 1, nota 2 e nota 3 até que o usuário digite 'fim'.
# Ex. 14: (continuação) Calcular a média das notas e apresentar.
# Ex. 14: (continuação) Descobrir qual o status da média e apresentar
#        Critérios de média:
#        Até 4.99 reprovado
#        Até 6.99 em exame
#        Até 10 aprovado
# Ex. 14: (continuação) Descobrir e apresentar qual é a menor nota 1
# Ex. 14: (continuação) Descobrir e apresentar qual é a maior nota 2
# Ex. 14: (continuação) Descobrir e apresentar qual é a maior média e o nome do aluno
# Ex. 14: (continuação) Descobrir e apresentar qual é a menor média e o nome do aluno
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que tem "Enzo" em seu nome
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o nome começa com "Valentina"
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é reprovado
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é aprovado
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é em exame