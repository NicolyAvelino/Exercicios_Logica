# 1º Ler números reais da matriz 3x3
# 2º Calcular e mostrar a somatoria dos elementos de cada linha
m = [0.0]*3
for i in range(len(m)):
    m[i] = [0.0]*3
    for j in range(len(m[i])):
        m[i][j] = float(input())
for i in range(len(m)):
    s = 0
    for j in range(len(m[i])):
        s += m[i][j]
    print("Somatoria %d é: %f"%(i,s))