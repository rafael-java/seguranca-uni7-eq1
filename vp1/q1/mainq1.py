# Opcoes validas para sair
opcoes_validas_sair = ["xx", "XX", "Xx", "xX"]


def sair():
    print("encerrando")
    raise SystemExit(0)


def converterParaBoolean():
    erro = True
    # Permite três tipos de casos, mas no erro só diz que aceita um, para facilitar
    opcoes_validas_c = ["CIFRAR", "cifrar", "Cifrar"]
    opcoes_validas_d = ["DECIFRAR", "decifrar", "Decifrar"]
    opcao = ""

    # Fica pedindo até ter um resultado certo
    while erro != False:
        opcao = input("Voce deseja CIFRAR ou DECIFRAR?")

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
        return True
    else:
        return False


def pegaMensagemEChave():
    # Pega a mensagem
    m = input("Escreva a mensagem:")
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


# variável que impede de sair, para sair, digite uma opcao valida de sair
continuar = True


# - - - - INICIO - - - - #

print("Implementar cifra de césar (Cifragem e decifragem)")
print("Digite xx para sair")

alfabeto = []
# Converte o alfabeto para lista
alfabeto[:0] = "abcdefghijklmnopqrstuvxywz"

while continuar == True:
    # deveCifrar = converterParaBoolean()
    mensagemChave = pegaMensagemEChave()
    mensagem = mensagemChave["mensagem"]
    chave = mensagemChave["chave"]
    print(mensagem, " ", chave)
    listaMsg = []
    listaMsg[:0] = mensagem
    print(listaMsg)

    arrayNovo = []
    mensagemNova = ""

## METODO 5
# se for qualquer coisa que não esteja no alfabeto (pesquisar sobre função in - if (char not in alfabeto)...), ignora
# pega a primeira letra, localiza no array de alfabeto (usar um for ou while, e um if), retorna a posição do array que tem a letra
## ENTRADA: variável ListaMensagem
## SAIDA: posição do array que contem a letra (variavel posicao)

## METODO 6
# vai ser chamado dentro do método 5
# a posição que tem a letra + chave = nova letra
# se nova letra > 26, nova letra = nova letra + 26 (**conferir**) - > se for cifrar
# se for decifrar -> nova letra = nova letra - 26 (**conferir**)
# salva no novo array
## ENTRADA: posição do array que contem a letra
## SAIDA: variável "nova letra" (que é cifrada)

## METODO 7
# vai ser chamado dentro do método 6 (Acho)
## ENTRADA: variável "nova letra" - cada uma (que é cifrada)
## SAIDA: arrayNovo com chars

## METODO 8
## método de saída - mostra a mensagem cifrada, ou decifrada, de acordo com metodo1
## ENTRADA: variável arrayNovo
## SAIDA: arrayNovo convertido em string, com uma mensagem bonitinha

# def metodo5():
#     # dentro de um for...
#     metodo6(posicao)
#     ## Teste Rafael - não apagar
#     # teste = ["a", "b", "c", "d", "e", "f"]
#     # for i in teste:
#     #     metodo6(i)

# def metodo6(posicao):
#     ## Teste Rafael - não apagar
#     # novaLetra = posicao
#     metodo7(novaLetra)

# def metodo7(novaLetra):
#     erro = True
#     while erro:
#         if not (isinstance(novaLetra, str)):
#             print("Algo deu errado. A nova letra não é uma letra!")
#             raise SystemExit(0)
#         else:
#             erro = False
#     global arrayNovo
#     arrayNovo.append(novaLetra)

# def main():
#     metodo2()
#     metodo4()
#     metodo5()
#     metodo8()
