## Utilizando SHA-256 e o AES, implementar o envio de uma mensagem e de um método de verificação de integridade

## 1 passo: Pegar a mensagem 
## 2 passo: transformar a mensagem em hashcode
## 3 passo: Concatenar a mensagem e o hash
## 4 passo: passo 3 criptografado com uma chave
## 5 passo: descriptografar usando a chave.
## 6 passo: pegar a mensagem e o hash
## 7 passo: Transformar o hash em mensagem e ai comparar a mensagem do passo 6 com a mensagem do passo 7.
from Crypto.Cipher import AES
from secrets import token_bytes
import hashlib
global nonce
global tag

def cryptoMessageAndHash(messageAndHash, key):
  # cria um objeto de cifra com a função new() no módulo Crypto.Cipher
  # o primeiro parâmetro é sempre a chave criptográfica (uma string de bytes)
  # o segundo parâmetro é sempre a constante que seleciona o modo de operação
  # nonce (bytes) – o valor do nonce fixo. Deve ser exclusivo para a combinação mensagem/chave.
  # Se não estiver presente, a biblioteca cria um nonce aleatório (16 bytes para AES)
  
  keyToken = token_bytes(int(key))
  cipher = AES.new(keyToken, AES.MODE_EAX)
  nonce = cipher.nonce
  ciphertext, tag = cipher.encrypt_and_digest(messageAndHash.encode('ascii'))
  print("cryptoMessageAndHash")
  return nonce, ciphertext, tag

def createHash(message):
  
  sha256 = hashlib.sha256()
  sha256.update(message.encode('utf-8'))
  return sha256.hexdigest()

def message(): 
  message = input("Digite sua mensagem: ")
  key = input("Insira a chave que deseja para criptografar: ")
  messageHash = createHash(message)
  messageAndHash = message + "|" + messageHash 
  nonce, ciphertext, tag = cryptoMessageAndHash(messageAndHash, key)


def menu():
  print('''
            ======== AES =======

            [1] -> Enviar mensagem criptografada
            [2] -> Sair
    ''')
  aux = True
  while aux == True:
      option = str(input("Escolha uma opção: ")).lower()
      if option == '1':
          message()
      elif option == '2':
          aux = False
          print("Fim")
      else:
          print("Opção inválida")

if __name__ == '__main__':
  menu()
