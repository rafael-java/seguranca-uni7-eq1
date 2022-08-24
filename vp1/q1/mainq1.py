## Implementar cifra de césar (Cifragem e decifragem)

## METODO 1 - fácil
## metodo para escolher se vai cifrar ou decifrar

## METODO 2 - médio
## método de entrada - receber mensagem e chave (se for cifrar), se for decifrar, recebe mensagem
## EX: 'mensagem'
## dois inputs!
## chave tem que converter do input para integer

## METODO 3 - dificil
## método de processamento
## array com o alfabeto, percorrer esse array, de acordo com a chave recebida
## EX: [a, b, c, d, e, f]

## METODO 4 - fácil
# dividir a mensagem em um array (split)
## EX: [m, e, n, s, a, g, e, m]

## METODO 5 - médio
# se for qualquer coisa que não esteja no alfabeto (função in), ignora
# pega a primeira letra, localiza no array de alfabeto (for e um if), retorna a posição do array que tem a letra

## METODO 6 - difícil
# a posição que tem a letra + chave = nova letra
# se nova letra > 26, nova letra = nova letra - 26 (**conferir**)
# salva no novo array

## METODO 7 - fácil
# converte de array para string

## METODO 8 - fácil
## método de saída - mostra a mensagem cifrada, ou decifrada, de acordo com metodo1
