phrase = str(input())

palavras = phrase.split()


resultado={}


for palavra in palavras:
    resultado[palavra]=len(palavra)

print(resultado)