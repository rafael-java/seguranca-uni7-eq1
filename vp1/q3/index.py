## Dado um arquivo qualquer, calcular o SHA-XXX do arquivo
import hashlib

def readFile(file):
  with open(file) as f:
    return f.read()

def encodeFiles():
  Sha1.update(content.encode())
  Sha256.update(content.encode())
  Sha512.update(content.encode())
  Sha224.update(content.encode())
  Sha384.update(content.encode())

content = readFile('testFile.txt')

Sha1 = hashlib.sha1()
Sha224 = hashlib.sha224()
Sha256 = hashlib.sha256()
Sha384 = hashlib.sha384()
Sha512 = hashlib.sha512()

encodeFiles()

print("Sha1: " + Sha1.hexdigest())
print("Sha224: " + Sha224.hexdigest())
print("Sha256: " + Sha256.hexdigest())
print("Sha384: " + Sha384.hexdigest())
print("Sha512: " + Sha512.hexdigest())




