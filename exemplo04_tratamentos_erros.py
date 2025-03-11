def tratar_erro_conversao_string_nao_inteira():
    #tentar executar um trecho de codigo que sabemos que poderá acontecer algum erro
    try: # tente
        # convertendo o que o usuario digitou de str pata int e sabemos que pode acontecer algum erro
        numero = int(input("Digite o número: "))
    except Exception as erro: # quando ocorrer algum erro executa o código daqui de dentro do except
        print("deu erro na conversão do número")
        # Caso desejar apresentar a mensagem do erro
        print("mensagem do erro: ", erro)
        
        
        # Apresentar essa mensagem dando erro ou nao
        print("Programa finalizado com sucesso")
        
 if __name__ == "__main__":
    tratar_erro_conversao_string_nao_inteira()