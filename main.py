import os

# funcionarios = {
#     matricula: [nome, codigo_função, numero_faltas_mes, salario_bruto]
# }
funcionarios = {}

def limpar_tela():
    os.system('cls')

def menu():
    menu = int(input("""
    [1]. INSERIR FUNCIONARIO
    [2]. REMOVER FUNCIONARIO
    [3]. FOLHA PAGAMENTO
    [4]. RELATORIO FUNCIONARIO
    [5]. MAIOR SALARIO LIQUIDO
    [6]. MAIOR NUMERO DE FALTAS NO MES 
    """))
    return menu

def inserir_func():
    opcao = menu()
    if opcao == 1:
        matricula = int(input("Matricula: "))
        nome = str(input("Nome: "))
        cod_funcao = int(input("Código da função: "))
        while cod_funcao != 101 and cod_funcao != 102:
            print("Código da funçõa invalido >>> Tente novamente!!! ")
            cod_funcao = int(input("Código da função: "))
        numero_faltas = int(input("Número de faltas por mês: "))
        salario_bruto = float(input("Salario Bruto: "))
        funcionarios[matricula] = [nome, cod_funcao, numero_faltas, salario_bruto]
    else:
        print("opção invalida")
    
inserir_func()
