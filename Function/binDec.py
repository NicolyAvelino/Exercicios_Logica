# Implemente uma função que receba um valor na base binaria(string 4 bits),converta para um numero na base decimal e o retorne
def conversao(valor):
    # 1º obter cada digito do valor
    # a = "1010"
    # a[0]
    # a[1]
    a = v1[0]
    b = v1[1]
    c = v1[2]
    d = v1[3] 
    return 2**0 * a + 2**1 * b + 2**2 *c  +  2**3 * d
    # 2º converta cada digito em um numero inteiro
    # 3º calcular
    # 4º retornar


def main():
    v1 = input()
    print("Valor da Conversão para Decimal é: %d"%valor(v1))
    
main()