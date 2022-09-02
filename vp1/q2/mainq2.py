from Crypto.Cipher import AES
from secrets import token_bytes

# chave criptografica
key = token_bytes(16)

global nonce

global tag

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


def mesage():
    nonce, ciphertext, tag = encrypt(input('Enter a message: '))
    plaintext = decrypt(nonce, ciphertext, tag)
    print(f'Cipher text: {ciphertext}')
    if not plaintext:
        print('Message is corrupted')
    else:
        print(f'Plain text: {plaintext}')

# criação do menu
# pergunta pro usuário uma opção de criptografia e descriptografia!
def menu():
    print('''
          ======== AES =======

          [C] -> criptografar
          [D] -> descriptografar
          [S] -> Sair
  ''')

    aux = True
    while aux == True:
        option = str(input("Escolha uma opção: ")).lower()
        if option == 'c':
            mesage()
        elif option == 'd':
            print("Decifrar")
        elif option == 's':
            aux = False
            print("Fim")
        else:
            print("Opção inválida")


if __name__ == '__main__':
    menu()
