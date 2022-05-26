# 3.
# Considere a função (consulte as demais funções no código-fonte apresentado em aula):

# def posicaoVazia(tabela, linha,coluna):
#     i = indiceLista(linha,coluna)
        
#     if tabela[i] == "-":
#         return True
#     else:
#         return False

# E considere que tabela = ['-','X','O','-','O','X','-','-','-'], linha=1 e coluna =1. Assinale a alternativa com o valor que será retornado pela função posicaoVazia:
def posicaoVazia(tabela, linha,coluna):
  i = indiceLista(linha,coluna)
  if tabela[i] == "-":
    return True
  else:
    return False
tabela = ['-','X','O','-','O','X','-','-','-']

posicaoVazia(tabela,1,1)
#False