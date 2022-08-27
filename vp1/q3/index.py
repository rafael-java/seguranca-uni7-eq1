## Dado um arquivo qualquer, calcular o SHA-XXX do arquivo
import hashlib

def readFile(file):
  with open(file) as f:
    return f.read()

def encodeFiles():
  Sha256.update(content.encode())
  Sha512.update(content.encode())
  Md5.update(content.encode())

content = readFile('testFile.txt')

Sha256 = hashlib.sha256()
Sha512 = hashlib.sha512()
Md5 = hashlib.md5()

encodeFiles()

print("Sha256: " + Sha256.hexdigest())
print("Sha512: " + Sha512.hexdigest())
print("MD5: " + Md5.hexdigest())




