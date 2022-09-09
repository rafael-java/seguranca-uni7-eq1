from email import message
from Crypto.Cipher import AES
from secrets import token_bytes

# chave criptografica
key = token_bytes(16)

# varáveis globais para receber os códogos hash necessários para a descriptografia
nonce = ""
ciphertext = ""
tag = ""


# função para deceber a mensagem a ser criptografada
def encrypt(msg):
    # cria um objeto de cifra com a função new() no módulo Crypto.Cipher
    # o primeiro parâmetro é sempre a chave criptográfica (uma string de bytes)
    # o segundo parâmetro é sempre a constante que seleciona o modo de operação
    # nonce (bytes) – o valor do nonce fixo. Deve ser exclusivo para a combinação mensagem/chave.
    # Se não estiver presente, a biblioteca cria um nonce aleatório (16 bytes para AES)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag


# função que recebe três valores para descriptografar a mensagem
# Se não estiver presente, a biblioteca cria um nonce aleatório (16 bytes para AES)
# faz a verivicação da chave e retorna a mensagem descriptografada
def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


# solicta ao usuário um texto simples, que é passado ao método encrypt
# que retorna três códigos hash que são amazenados globalmento para serem usados
# para descifrar a menssage
def message():
    global nonce
    global ciphertext
    global tag
    nonce, ciphertext, tag = encrypt(input('Digite a mensagem: '))
    print(f'\nTexto cifrado: {ciphertext}')


# criação do menu
# pergunta pro usuário uma opção de criptografia e descriptografia!
def menu():
    aux = True
    while aux == True:
        print('''
======== AES =======

[C] -> criptografar
[D] -> descriptografar
[S] -> Sair
        ''')
        option = str(input("Escolha uma opção: ")).lower()
        if option == 'c':
            message()
        elif option == 'd':
            plaintext = decrypt(nonce, ciphertext, tag)
            if not plaintext:
                print('\nA mensagem está corrompida')
            else:
                print(f'\nTexto: {plaintext}')
        elif option == 's':
            aux = False
            print("\nFim")
        else:
            print("\nOpção inválida")


# método pricipa do programa
menu()
