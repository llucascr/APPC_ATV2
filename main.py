import os

funcionarios = {}

def Limpar():
    os.system("cls")

def Validar_codigo_funcao():
    cod_funcao = int(input("Código da função: "))
    while cod_funcao != 101 and cod_funcao != 102:
        print("Código da função invalido >>> Tente novamente!!! ")
        cod_funcao = int(input("Código da função: "))
    return cod_funcao

def Validar_id_matricula():
    id_matricula = int(input("Digite o ID da matrícula:"))
    while id_matricula in funcionarios:
        print("ID de matricula ja existe >>> Tente novamente!!! ")
        id_matricula = int(input("Digite o ID da matrícula:"))
    return id_matricula

def Calculo_imposto(salario_liquido):
    if salario_liquido <= 2259.20:
        imposto = 0
    elif salario_liquido <= 2828.65:
        imposto = 0.075
    elif salario_liquido <= 3751.05:
        imposto = 0.15
    elif salario_liquido <= 4664.68:
        imposto = 0.225 
    else:
        imposto = 0.275
    return imposto


def Cadastro_funcionario():
    id_matricula = Validar_id_matricula()
    nome = str(input("Nome do funcionario: "))
    print("[101] - Vendedor\n[102] - Administrativo")
    cod_funcao = Validar_codigo_funcao()
    if cod_funcao == 101:
        volume_vendas = int(input("Volume de vendas: "))
        salario_bruto = (volume_vendas * 0.9) + 1500
        print(salario_bruto)
        imposto = 0
    else:
        print("Salário varia entre R$2150,00 até R$6950,00")
        salario_bruto = float(input("Salário do funcionário: "))
        while salario_bruto < 2150 or salario_bruto > 6950:
            print("Por favor, digite um salário dentro da faixa especificada.")
            salario_bruto = float(input("Salário do funcionário: "))
    numero_faltas = int(input("Número de faltas por mês: "))
    for i in range(numero_faltas):
        # Pesquisar sobre salario liquido e salario bruto
        # Atenção: Mudança no nome das variaveis salario bruto e salario liquido
        # Percentual do Imposto – para determinar o Salário Líquido
        salario_liquido = salario_bruto - 1500/30
    imposto = Calculo_imposto(salario_bruto)

    funcionarios[id_matricula] = [nome, cod_funcao, numero_faltas, salario_liquido, salario_bruto, imposto]

def Remover_funcionario():
    print(">>> Remoção de Funcionario >>>")
    remover = int(input("ID Matriucla do funcionário: "))
    while remover not in funcionarios:
        print("ID de matricula não existe >>> Tente novamente!!!")
        remover = int(input("ID Matriucla do funcionário: "))
    del funcionarios[(remover)]

def Folha_pagamento():
    print("Determinar folha de pagamento por ID de determinado funcionário")
    key = int(input("ID do(a) funcionário: "))
    for id, index in funcionarios.items(): 
        if key == id:
            print(f"""
            ID: {id}
            NOME: {index[0]}
            CODIGO: {index[1]}
            SALÁRIO BRUTO: R${index[3]}
            PORCENTUAL DE IMPOSTO: {index[4]}
            """)
        else:
            print(">>> ID não existe")

def Relatorio():
    print("Relatório com salario bruto e liquido de todos os funcionarios")
    for id, index in funcionarios.items():
            print(f"""
            ID: {id}
            NOME: {index[0]}
            CODIGO: {index[1]}
            SALÁRIO BRUTO: R${index[4]}
            SALÁRIO LIQUIDO: R$ {index[3]}
            """)   

menu = 1
while menu > 0:
    menu = int(input("""
       |================================|
       | [1] - Adicionar funcionários.  |
       |                                |
       | [2] - Remover funcionários.    |
       |                                |
       | [3] - Folha de pagamento por ID|
       |                                |
       | [4] - Relatório                |
       |                                |
       | [0] - Sair do programa         |
       |================================|
                    OPÇÃO:"""))
    Limpar()
    if menu == 1:
        Cadastro_funcionario()
    elif menu == 2:
        Remover_funcionario()
    elif menu == 3:
        Folha_pagamento()
    elif menu == 4:
        Relatorio()