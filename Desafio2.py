print("Pense em um número bem legal que eu vou ver se está na sequência de Fibonacci")
print("Digite o número aqui:")
num = int(input())

print("Verificando...")

fib=[0]
cont = 1

while(fib[-1]<num):
    if(cont == 1):
        fib.append(1)
        cont+=1
    if (cont > 1):
        fib.append(fib[-1] + fib[-2])
        cont+=1

if(fib[-1]==num):
    print("O número pertence a sequência!")
else:
    print("O número não pertence a sequencia :'(")

print("Essa é a sequência que eu calculei: ", fib)
print("Prontinho, matou sua curiosidade?")
print("********************************")