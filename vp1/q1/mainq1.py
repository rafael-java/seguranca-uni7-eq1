# Opcoes validas para sair
opcoes_validas_sair = ["xx", "XX", "Xx", "xX"]


def sair():
    print("Ok, encerrando")
    raise SystemExit(0)


def perguntaSobreCifragem():
    erro = True
    # Permite três tipos de casos, mas no erro só diz que aceita um, para facilitar
    opcoes_validas_c = ["CIFRAR", "cifrar", "Cifrar"]
    opcoes_validas_d = ["DECIFRAR", "decifrar", "Decifrar"]
    opcao = ""

    # Fica pedindo até ter um resultado certo
    while erro != False:
        opcao = input("Voce deseja CIFRAR ou DECIFRAR? ")

        # checa se opcao é valida
        if opcao in opcoes_validas_c or opcao in opcoes_validas_d:
            erro = False
            break
        # checa se opcao é sair
        elif opcao in opcoes_validas_sair:
            sair()
        # checa se opcao é invalida
        else:
            print("Error! Você precisa digitar CIFRAR, DECIFRAR, ou xx para sair")

    if opcao in opcoes_validas_c:
        print("ok, vamos cifrar")
        return True
    else:
        print("ok, vamos decifrar")
        return False


def pegaMensagemEChave():
    # Pega a mensagem
    m = input("Escreva a mensagem:")
    # Teste
    # m = "u v !!! # x z abc fgh iii"
    while m == "" or m == " " or m in opcoes_validas_sair:
        if m in opcoes_validas_sair:
            sair()
        else:
            print("Mensagem não pode estar em branco")
            m = input("Escreva a mensagem:")

    # Pega a chave
    # PERGUNTA: CHAVE PODE SER NEGATIVA?
    c = input("Escreva a chave:")
    if c in opcoes_validas_sair:
        sair()
    else:
        erro = True
        while erro:
            try:
                c = int(c)
                erro = False
            except:
                print("Chave deve ser número, tente novamente")
                c = input("Escreva a chave:")

    # Coloca em um dicionário
    mensagemChave = {"mensagem": "", "chave": ""}
    mensagemChave["mensagem"] = m
    mensagemChave["chave"] = c
    return mensagemChave


def pegarPosicao(listaMensagem, alfabeto, listaPosicoes):
    for car in listaMensagem:
        if car in alfabeto:
            listaPosicoes.append(alfabeto.index(car))
        else:
            listaPosicoes.append(car)
    return listaPosicoes


def calculaQuantoDeveAndar(deveCifrar, listaPosicoes, chave, alfabeto):
    list = []
    tamanhoAlf = len(alfabeto)
    chaveAnterior = chave
    # Para cada posicao

    for posicao in listaPosicoes:
        if type(posicao) == int:
            chave = chaveAnterior
            while chave >= tamanhoAlf:
                chave = chave - tamanhoAlf
            if deveCifrar:
                while chave > 0:
                    posicao = posicao + 1
                    if (posicao) > tamanhoAlf - 1:
                        posicao = 0
                    chave = chave - 1
            else:
                while chave > 0:
                    posicao = posicao - 1
                    if (posicao) < 0:
                        posicao = tamanhoAlf - 1
                    chave = chave - 1

        # Salvar a nova posicao na lista nova
        list.append(posicao)

    # Array com novas posições
    return list


def converteParaTexto(listaPosicoes, alfabeto):
    stri = ""

    for posicao in listaPosicoes:
        if type(posicao) == int:
            stri += alfabeto[posicao]
        else:
            stri += posicao

    return stri


def process(mensagem, chave, deveCifrar):
    alfabeto = []
    # Converte o alfabeto para lista
    alfabeto[:0] = "abcdefghijklmnopqrstuvwxyz"
    listaMsg = []
    listaMsg[:0] = mensagem
    # print(listaMsg)
    listaPosicoes = []
    listaPosicoes = pegarPosicao(listaMsg, alfabeto, listaPosicoes)
    # print(listaPosicoes)
    listaNovasPosicoes = []
    listaNovasPosicoes = calculaQuantoDeveAndar(
        deveCifrar, listaPosicoes, chave, alfabeto
    )
    # print(listaNovasPosicoes)
    stringNova = converteParaTexto(listaNovasPosicoes, alfabeto)
    return stringNova


def coleta_dados():
    # - - - - PARTE 1 - - - - #
    while True:
        print("Questão 1. Implementar cifra de césar (Cifragem e decifragem)")
        print("Digite xx para sair")
        # Impede de sair, para sair, digite uma opcao valida de sair
        # deveCifrar = False
        deveCifrar = perguntaSobreCifragem()
        mensagemChave = pegaMensagemEChave()
        mensagem = mensagemChave["mensagem"]
        chave = mensagemChave["chave"]
        # chave = 1
        # print(mensagem, " ", chave)
        mensagemNova = process(mensagem, chave, deveCifrar)
        print(mensagemNova)


if __name__ == "__main__":
    coleta_dados()
