## Implementar cifra de césar (Cifragem e decifragem)

## Obs: todas as variáveis são globais!
## Obs2: Respeitar o local de declaração de variáveis
## Obs3: Comentar o bloco de declaração de variáveis de teste antes de commitar
## Obs4: não renomear os metodos, ainda. Vamos fazer isso juntos!

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

## METODO 3 - dificil - MATEUS
## gerar array com o alfabeto
## EX: [a, b, c, d, e, f...]
## ENTRADA: -
## SAIDA: variável lista "alfabeto" preenchida

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
# se for decifrar -> nova letra = nova letra - 26
# salva no novo array
## ENTRADA: posição do array que contem a letra
## SAIDA: variável "nova letra" (que é cifrada)

## METODO 7 - fácil - RAFAEL
# vai ser chamado dentro do método 6 (Acho)
# converte de array para string
## ENTRADA: variável "nova letra" - cada uma (que é cifrada)
## SAIDA: arrayNovo com chars

## METODO 8 - fácil - MATEUS
## método de saída - mostra a mensagem cifrada, ou decifrada, de acordo com metodo1
## ENTRADA: variável arrayNovo
## SAIDA: mostrar pro usuário o arrayNovo, com uma mensagem bonitinha


##** DECLARAÇÃO DE VARIAVEIS - inicio **##

##** DECLARAÇÃO DE VARIAVEIS - fim **##

## Espaço para criar variáveis de teste - inicio ##
# Antes de subir, comentar.
#ListaMensagem = ["a", "b", "c"]
#ListaAlfabeto = ["a", "b", "c"]
## Espaço para criar variáveis de teste - fim ##


print("Cifra de César")
def metodo1(decifrar):
    switcher = {
        0: 0,
        1: 1,
    }
    return switcher.get(decifrar)


#def metodo2():
#    print("2")


#def metodo3():
#    print("3")


#def metodo4():
#    print("4")


#def metodo5():
#    # dentro de um for...
#    metodo6(posicao)


#def metodo6(posicao):
#    metodo7(novaLetra)


#def metodo7(novaLetra):
#    print("7")


#def metodo8():
#    print("8")


if __name__ == "__main__":
    print("Escolha decifrar ou cifrar:")
    print("decifrar- Opção 1")
    print("cifrar- Opção 0")
    cifrar = input()
    print(metodo1(int(cifrar)))
#    metodo2()
#    metodo3()
#    metodo4()
#    metodo5()
#    metodo8()