# main => é o ponto de entrada de uma aplicação
# import src.exemplo_importacoes.exemplo_imports
# from src.exemplo_importacoes import exemplo_imports
from src.exemplo_importacoes.exemplo_imports import executar_calculos_matematicos
from src.exemplo07_metodos_parametros import calculadora, calcular_folha_pagamento

if __name__ == "__main__":
    # src.exemplo_importacoes.exemplo_imports.executar_calculos_matematicos()
    # exemplo_imports.executar_calculos_matematicos()
    # executar_calculos_matematicos()
    calcular_folha_pagamento()
