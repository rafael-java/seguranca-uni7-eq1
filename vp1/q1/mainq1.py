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


def pegarPosicao(listaMensagem, listaAlfabetosPossiveis, listaPosicoes):

    alfabeto0 = []
    alfabeto1 = listaAlfabetosPossiveis[0]
    alfabeto2 = listaAlfabetosPossiveis[1]
    alfabeto3 = listaAlfabetosPossiveis[2]

    listaPosicoes = []
    for car in listaMensagem:
        caracter = {"char": car, "alfabeto": alfabeto0, "posicao": -1}

        if car in alfabeto3:
            letraNova = removeAcento(car, alfabeto3)
            car = letraNova

        if car in alfabeto1:
            caracter["alfabeto"] = alfabeto1
            caracter["posicao"] = alfabeto1.index(car)
        elif car in alfabeto2:
            caracter["alfabeto"] = alfabeto2
            caracter["posicao"] = alfabeto2.index(car)

        listaPosicoes.append(caracter)
    return listaPosicoes


def removeAcento(letra, alfabeto3):
    if alfabeto3.index(letra) >= 0 and alfabeto3.index(letra) < 4:
        letraNova = "a"
    elif alfabeto3.index(letra) >= 4 and alfabeto3.index(letra) < 8:
        letraNova = "A"
    elif alfabeto3.index(letra) >= 8 and alfabeto3.index(letra) < 13:
        letraNova = "e"
    elif alfabeto3.index(letra) >= 13 and alfabeto3.index(letra) < 17:
        letraNova = "E"
    elif alfabeto3.index(letra) >= 17 and alfabeto3.index(letra) < 21:
        letraNova = "i"
    elif alfabeto3.index(letra) >= 21 and alfabeto3.index(letra) < 25:
        letraNova = "I"
    elif alfabeto3.index(letra) >= 25 and alfabeto3.index(letra) < 29:
        letraNova = "o"
    elif alfabeto3.index(letra) >= 29 and alfabeto3.index(letra) < 33:
        letraNova = "O"
    elif alfabeto3.index(letra) >= 33 and alfabeto3.index(letra) < 37:
        letraNova = "u"
    elif alfabeto3.index(letra) >= 37 and alfabeto3.index(letra) < 41:
        letraNova = "U"
    return letraNova


def calculaQuantoDeveAndar(deveCifrar, listaPosicoes, chave):
    list = []
    chaveAnterior = chave

    # listaPosicoes = list de caracter
    # caracter = {"char": car, "alfabeto": alfabeto0, "posicao": -1}
    for caracter in listaPosicoes:
        novo = {"char": "", "alfabeto": None, "posicao": -1}
        tamanhoAlf = len(caracter["alfabeto"])
        posicao = caracter["posicao"]

        if posicao != -1:
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

        novo["char"] = caracter["char"]
        novo["alfabeto"] = caracter["alfabeto"]
        novo["posicao"] = posicao

        # Salvar a nova posicao na lista nova
        list.append(novo)

    # Array com novas posições
    return list


def converteParaTexto(listaPosicoes):
    stri = ""
    # listaPosicoes = list de novos
    # novo = {"char": "", "alfabeto": None, "posicao": -1}

    for novo in listaPosicoes:
        if novo["posicao"] != -1:
            alfabeto = novo["alfabeto"]
            posicao = novo["posicao"]
            stri += alfabeto[posicao]
        else:
            stri += novo["char"]

    return stri


def pegaAlfabetosPossiveis():
    # Uma lista de alfabetos possiveis
    alfabetosPossiveis = []
    alfabeto1 = []
    alfabeto1[:0] = "abcdefghijklmnopqrstuvwxyz"
    alfabeto2 = []
    alfabeto2[:0] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto3 = []
    alfabeto3[:0] = "áàâäÁÀÂÄéèêêëËÊÈÉíìîïÎÌÍÏóòôöÒÓÔÖúùûüÚÙÛÜ"
    alfabetosPossiveis.append(alfabeto1)
    alfabetosPossiveis.append(alfabeto2)
    alfabetosPossiveis.append(alfabeto3)
    return alfabetosPossiveis


def process(mensagem, chave, deveCifrar):
    # - - - - PARTE 2 - - - - #
    alfabetosPossiveis = pegaAlfabetosPossiveis()
    listaMsg = []
    listaMsg[:0] = mensagem
    # print(listaMsg)
    listaPosicoes = []
    listaPosicoes = pegarPosicao(listaMsg, alfabetosPossiveis, listaPosicoes)
    # print(listaPosicoes)
    listaNovasPosicoes = []
    listaNovasPosicoes = calculaQuantoDeveAndar(deveCifrar, listaPosicoes, chave)
    # print(listaNovasPosicoes)
    stringNova = converteParaTexto(listaNovasPosicoes)
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
