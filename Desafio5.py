print("Vamos retrever as coisas?")
print("Digite o que quiser que eu reverto para você:")
palavras = input()

palavras = list(palavras)
tam = len(palavras)
i = tam-1
reverso = []
while(i>=0):
    reverso.append(palavras[i])
    i-=1

palavras_revertidas = ''.join(reverso)
print("Revertido: ", palavras_revertidas)
print("Prontinho!!")
print("*********************************")