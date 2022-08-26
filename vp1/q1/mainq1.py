## Implementar cifra de césar (Cifragem e decifragem)

## Obs: todas as variáveis são globais! Lembrar do modificador "global": https://www.w3schools.com/python/python_variables_global.asp
## Obs2: Respeitar o local de declaração de variáveis
## Obs3: Comentar o bloco de declaração de variáveis de teste antes de commitar
## Obs4: não renomear os metodos, ainda. Vamos fazer isso juntos!
## Obs5: Lembrar da tratativa de erros!

## METODO 1 - fácil - LEANDRO
## metodo para escolher se vai cifrar ou decifrar
## ENTRADA: INPUT vai originar uma variavel (nome: cifrar), tipo: boleana
## SAIDA: Variavel (nome: cifrar), tipo: boleana

## METODO 2 - médio - RAFAEL
## método de entrada - receber mensagem e chave
## EX: 'mensagem' e '2'
## Dois inputs!
## Chave tem que converter do input para integer
## ENTRADA: -
## SAIDA: duas variaveis: mensagem e chave

## METODO 4 - fácil - RUBENS
# dividir a mensagem em um array (pesquisar sobre split)
## EX: [m, e, n, s, a, g, e, m]
## ENTRADA: variavel "mensagem"
## SAIDA: variável ListaMensagem mensagem em forma de lista de chars

## METODO 5 - médio - LEANDRO
# se for qualquer coisa que não esteja no alfabeto (pesquisar sobre função in - if (char not in alfabeto)...), ignora
# pega a primeira letra, localiza no array de alfabeto (usar um for ou while, e um if), retorna a posição do array que tem a letra
## ENTRADA: variável ListaMensagem
## SAIDA: posição do array que contem a letra (variavel posicao)

## METODO 6 - difícil - RUBENS
# vai ser chamado dentro do método 5
# a posição que tem a letra + chave = nova letra
# se nova letra > 26, nova letra = nova letra + 26 (**conferir**) - > se for cifrar
# se for decifrar -> nova letra = nova letra - 26 (**conferir**)
# salva no novo array
## ENTRADA: posição do array que contem a letra
## SAIDA: variável "nova letra" (que é cifrada)

## METODO 7 - fácil - RAFAEL
# vai ser chamado dentro do método 6 (Acho)
## ENTRADA: variável "nova letra" - cada uma (que é cifrada)
## SAIDA: arrayNovo com chars

## METODO 8 - fácil - MATEUS
## método de saída - mostra a mensagem cifrada, ou decifrada, de acordo com metodo1
## ENTRADA: variável arrayNovo
## SAIDA: arrayNovo convertido em string, com uma mensagem bonitinha

##** DECLARAÇÃO DE VARIAVEIS - inicio **##
alfabeto = ['a', 'b', 'c', 'd', 'e', "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cifrar = False
mensagem = ""
chave = 0
ListaMensagem = []
arrayNovo = []
mensagemNova = ""
##** DECLARAÇÃO DE VARIAVEIS - fim **##

## Espaço para criar variáveis de teste - inicio ##
# Antes de subir, comentar.
## ListaMensagem = ["a", "b", "c"]
## ListaAlfabeto = ["a", "b", "c"]
## Espaço para criar variáveis de teste - fim ##


def metodo1():
    print("1")


def metodo2():
    global mensagem, chave
    m = input("Escreva a mensagem:")
    while m == "" or m == " ":
        print("Mensagem não pode estar em branco")
        m = input("Escreva a mensagem:")

    c = input("Escreva a chave:")
    erro = True
    while erro:
        try:
            c = int(c)
            erro = False
        except:
            print("Chave deve ser número, tente novamente")
            c = input("Escreva a chave:")

    mensagem = m
    chave = c


def metodo3():
    print("3")


def metodo4():
    print("4")


def metodo5():
    # dentro de um for...
    metodo6(posicao)

    ## Teste Rafael - não apagar
    # teste = ["a", "b", "c", "d", "e", "f"]
    # for i in teste:
    #     metodo6(i)


def metodo6(posicao):
    ## Teste Rafael - não apagar
    # novaLetra = posicao
    metodo7(novaLetra)


def metodo7(novaLetra):
    erro = True
    while erro:
        if not (isinstance(novaLetra, str)):
            print("Algo deu errado. A nova letra não é uma letra!")
            raise SystemExit(0)
        else:
            erro = False
    global arrayNovo
    arrayNovo.append(novaLetra)


def metodo8():
    print("8")


def main():
    metodo1()
    metodo2()
    metodo4()
    metodo5()
    metodo8()


main()

## Falta: colocar isso em um loop
