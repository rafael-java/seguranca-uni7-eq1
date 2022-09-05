# How to run

- There is no need for external libs to run this.
- This process has been checked using OSX. It is possible that on Windows it works in a different way.
- In the terminal you need to specify the path of question 3, that is, if you are in the path <span style='color: red'>c:\xxx\xxx\seguranca-uni7-eq1\ </span> you need to insert the following commands:

```
cd vp1
```
- After that
```
cd q1
```
- And then run the command

```
python3 mainq1.py
```

# Brief introduction to program

- The code will gather input to know if the user wants to encrypt or decypt the message, then it will ask for the message, then the key to encrypt the message. 
- It is always possible to type xx to exit the program. Otherwise it will be on loop.
- The program checks for some errors and works for some accents and all the letters on the english alphabet, being upper or lower case.

# Brief introduction to code
- The code is separated in 10 methods, starting from the bottom:

## coleta_dados
- Responsible for the first part of the program. It shows messages for the user and gather the needed inputs

## process
- Responsible for the process itself. It will call the other methods

## pegaMensagemEChave
- Called in the first method. It gathers message and key, while checking for some errors in the input. It also checks if the user wants to exit the process.

## perguntaSobreCifragem
- Called in the first method. It gathers if the user wants to encrypt or decrypt, while checking for some errors in the input. It also checks if the user wants to exit the process.

## sair
- If the user wants to exit the process, it shows a message and call SystemExit.

## pegaAlfabetosPossiveis
- It gathers three possible alphabets: lower case, upper case and with the main accents

## pegarPosicao
- It checks against the alphabets to see which alphabet the letter is in. If it is in the alphabet with accents, it removes the accent. Otherwise it stores the character, alphabet and position in a dictionary. It does the same for all the characters, and stores each dictionary in a list.

## removeAcento
- It checks against the alphabet with accent to know which letter it should replace and returns the new letter.

## calculaQuantoDeveAndar
- It gets the list of dictionaries and runs the same for each dictionary: gather the letter, run against the logic to see which new position it should be, and gets the new character from its respective alphabet.
- The logic is based on the manual process for the caesar cipher: if it wants to encrypt, it walks one position until the end of the alphabet. If it reaches the end, it starts the alphabet over. If it wants to decrypt, it walks one position until the start of the alphabet. If it reaches the beginning, it goes to the end of the alphabet.
- It stores the result in a new list of dictionaries.

## converteParaTexto
- With the new list of dictionaries, it gets the character from each index and stores in a string, that is returned as "new message"

# Future Works
- Implement testing
- Conver the written code to english
- Check for more possible errors on the program
- Check for more possible accents for the input 



