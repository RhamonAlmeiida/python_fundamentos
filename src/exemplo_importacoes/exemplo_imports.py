# Importação1: importandno o arquivo, tenho que passar o caminho completo
import src.exemplo07_metodos_parametros

# Importação2: importando do src o arquivo exemplo06_metodos
from src import exemplo06_metodos

# Importação3: importando um método do arquivo exemplo05_for
from src.exemplo05_for import exemplo_relogio, exemplo_apresentar_contagem_regresiva

def executar():
    # Importacao1: utilização da importação devo passar o caminho completo e o método
    src.exemplo07_metodos_parametros.calculadora()

    # Importação2: utilização da importação devo passar o nome do arquivo e o método
    exemplo06_metodos.apresentar_nome_completo()

    # Importação3: utilização da importação devo chamar os métodos importados
    exemplo_relogio()
    exemplo_apresentar_contagem_regresiva()


def executar_calculos_matematicos():
    import math
    print("Raiz quadrada de 114: ", math.sqrt(114))
