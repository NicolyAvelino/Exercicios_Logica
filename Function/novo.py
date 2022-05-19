# Elaborar funções e testar
# 1 - Implemente uma função que recebe por parametro a quantidade de linhas e colunas e crie uma matriz com essas dimensões;
def lerMatriz(l,c):
    m = [0]*l
    for i in range(len(m)):
        m[i] = [0]*c
        for j in range(len[m[i]]):
            m[i][j] = int(input())
    return m
# 2- Implemente uma função por parametro, calcule e retorne a media dos elementos.
def media(m):
    s = 0
    qtdeElem = 0
    for i in range(len(m)):
        for j in range(m[i]):
            s += m[i][j]
            qtdeElem += 1
    return s/qtdeElem
# 3 - Implemente uma função que recebe por parâmetro uma matriz e mostra os elementos maiores que esse valor
def mostrarAcimaMedia(matriz, media):
     for i in range(len(matriz)):
        for j in range(matriz[i]):
            if matriz[i][j] > media:
                print(matriz[i][j])
def main():
    print(lerMatriz(2,3))
    
    m1 = lerMatriz(2,2)
    media1 = media(m1)
    mostrarAcimaMedia(m1,media1)
    print(media(m1))
main()