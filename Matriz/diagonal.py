# 1º Ler strings para matriz 2x2
# 2º Exibir as string que estão na diagonal principal
m = [""]*2
for i in range(len(m)):
    m[i] = [""]*2
    for j in range(len(m[i])):
        m[i][j] = input()
for i in range(len(m)):
    print(m[i][i])