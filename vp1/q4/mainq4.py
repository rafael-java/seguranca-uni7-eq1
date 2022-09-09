## Utilizando SHA-256 e o AES, implementar o envio de uma mensagem e de um método de verificação de integridade

## 1 passo: Pegar a mensagem
## 2 passo: transformar a mensagem em hashcode
## 3 passo: Concatenar a mensagem e o hash
## 4 passo: passo 3 criptografado com uma chave
## 5 passo: descriptografar usando a chave.
## 6 passo: pegar a mensagem e o hash
## 7 passo: Comparar o hash da mensagem do passo 6 com o hash da mensagem do passo 2.

from Crypto.Cipher import AES
from secrets import token_bytes
import hashlib

global nonce
global tag

## 7 passo: Comparar o hash da mensagem do passo 6 com o hash da mensagem do passo 2.
def compararHashs(mensagem, hashRetornado):
    hashNovo = createHash(mensagem)
    if hashNovo == hashRetornado:
        return True
    else:
        return False


## 6 passo: pegar a mensagem e o hash
def pegarMensagemEHash(mensagemEHash):
    mensagemEHash = mensagemEHash.split("|")
    return mensagemEHash[0], mensagemEHash[1]


## 5 passo: descriptografar usando a chave.
def decrypt(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode("ascii")
    except:
        return False


## 4 passoº: passo 3 criptografado com uma chave
def cryptoMessageAndHash(messageAndHash, key):
    # cria um objeto de cifra com a função new() no módulo Crypto.Cipher
    # o primeiro parâmetro é sempre a chave criptográfica (uma string de bytes)
    # o segundo parâmetro é sempre a constante que seleciona o modo de operação
    # nonce (bytes) – o valor do nonce fixo. Deve ser exclusivo para a combinação mensagem/chave.
    # Se não estiver presente, a biblioteca cria um nonce aleatório (16 bytes para AES)

    # OLHAR ESSA CHAVE
    # Disponibilzar a chave para o usuário poder descript
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(messageAndHash.encode("ascii"))
    # print("cryptoMessageAndHash")
    return nonce, ciphertext, tag


## 2º passo: transformar a mensagem em hashcode
def createHash(message):

    sha256 = hashlib.sha256()
    sha256.update(message.encode("utf-8"))
    return sha256.hexdigest()


## 1º passo: Pegar a mensagem
## 3º passo: Concatenar a mensagem e o hash
def message():
    message = input("Digite sua mensagem: ")
    # key = input("Insira a chave que deseja para criptografar: ")
    messageHash = createHash(message)
    messageAndHash = message + "|" + messageHash
    keyToken = token_bytes(16)
    nonce, ciphertext, tag = cryptoMessageAndHash(messageAndHash, keyToken)
    text = decrypt(nonce, ciphertext, tag, keyToken)
    mensagemRetornada, hashRetornado = pegarMensagemEHash(text)
    if compararHashs(mensagemRetornada, hashRetornado):
        print("tudo certo")
    else:
        print("tudo errado")


def menu():
    print(
        """
            ======== AES =======

            [1] -> Enviar mensagem criptografada
            [2] -> Sair
    """
    )
    aux = True
    while aux == True:
        option = str(input("Escolha uma opção: ")).lower()
        if option == "1":
            message()
        elif option == "2":
            aux = False
            print("Fim")
        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu()
