import readline


f = open("demofile.txt", "r")
arquivo= f.read()
print("Arquivo Original")
print(f.read())

print("Divisão do Arquivo por Linhas")
lista = arquivo.split("\n")
print(lista)

print("Divisão de Cada Linha por Espaço em Branco")
for linha in lista:
    print(linha.split(" "))

while arquivo != "":
    print("Linha Original")
    print(arquivo)
    arquivo = f.readline()
f.close()

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
