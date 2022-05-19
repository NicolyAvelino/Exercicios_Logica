def lerLista():
    lista = [0]*100
    for i in range(len(lista)):
        lista[i] = int(input("Digite um valor:"))
    return lista

def media(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s/len(a)
    
def mostrarMaiores(lista,media):
    for i in range(len(lista)):
        if lista[i]>media:
            print(lista[i])
        
def main():
    x = lerLista()
    m = media(x)
    mostrarMaiores(x,m)
    y = lerLista()
    p = media(x)
    mostrarMaiores(y,p)
   
main()