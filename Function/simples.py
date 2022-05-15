# Criando função
def mensagem1():
    print("Olá!")
# função mensagem2
def mensagem2(nome):
    print("Oii",nome)

# função para retornar valor
def mensagem3(nome):
    return "Hi! ", nome
# Deixando mais organizado usando main()
def main():
    
    # mensagem1()
    # mensagem2("Nick")
    # print(mensagem3("Carol"))
    a = mensagem3("Nick")
    print(a)
main()