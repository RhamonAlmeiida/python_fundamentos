    # PASSO 1

def __solicitar_orcamento() -> float:
    limite_despesas = 0
    while limite_despesas <= 0:
        try:
            limite_despesas = float(input("Digite seu limite de gastos mensal: R$ "))
            if limite_despesas <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
        except ValueError as error:
            print("Erro de operação!! Por favor, insira um número válido.")
    return limite_despesas

     # PASSO 2

def __solicitar_despesas_alimentacao() -> float:
    valor_alimentacao = 0
    while valor_alimentacao <= 0:
        try:
            valor_alimentacao = float(input("Digite o valor gasto com alimentação: R$ "))
            if valor_alimentacao <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
        except ValueError as error:
            print("Erro de operação!! Por favor, insira um número válido.")
    return valor_alimentacao

def __solicitar_despesas_transporte() -> float:
    valor_transporte = 0
    while valor_transporte <= 0:
        try:
            valor_transporte = float(input("Digite o valor gasto com transporte: R$ "))
            if valor_transporte <= 0:
                print("O valor deve ser maior que zero. Tente novamente. ")
        except ValueError as error:
            print("Erro de operação!! Por favor, insira um número válido.")
    return valor_transporte

def __solicitar_despesas_lazer() -> float:
    valor_lazer = 0
    while valor_lazer <= 0:
        try:
            valor_lazer = float(input("Digite o valor gasto com lazer: R$ "))
            if valor_lazer <= 0:
                print("O valor deve ser maior que zero. Tente novamente. ")
        except ValueError as error:
            print("O valor deve ser maior que zero. Tente novamente. ")
    return valor_lazer

def __solicitar_despesas_saude() -> float:
    valor_saude = 0
    while valor_saude <= 0:
        try:
            valor_saude = float(input("Digite o valor gasto com saúde: R$ "))
            if valor_saude <= 0:
                print("O valor deve ser maior que zero. Tente novamente. ")
        except ValueError as error:
            print("O valor deve ser maior que zero. Tente novamente. ")
    return valor_saude

    # PASSO 3

def __calcular_total_despesas(alimentacao: float, transporte: float, lazer: float, saude: float) -> float:
    total_despesas = alimentacao + transporte + lazer + saude
    return total_despesas














def controle_de_despesas():

    orcamento = __solicitar_orcamento()
    alimentacao = __solicitar_despesas_alimentacao()
    transporte = __solicitar_despesas_transporte()
    lazer = __solicitar_despesas_lazer()
    saude = __solicitar_despesas_saude()
    total_despesas = __calcular_total_despesas(alimentacao, transporte, lazer, saude)


