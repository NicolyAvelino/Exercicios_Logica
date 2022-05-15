# Função para somar valores
def somar(a,b):
    return a+b

def multiplicar(a,b,c):
    return a*b*c

# Função para subtrair
def subtrair(a,c):
    return a-c

# media
def media(a,b,c):
    return (a+b+c) / 3
 
def main():
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())

    # somar
    print("Resultado da Soma: %d"%somar(v1,v2))

    # multiplicar    
    print("Resultado da Multiplicação: %d"%multiplicar(v1,v2,v3))

    # subtrair
    print("Resultado da Subtração: %d"%subtrair(v1,v3))

    # media
    print("Media: %d"%media(v1,v2,v3))
    
main()