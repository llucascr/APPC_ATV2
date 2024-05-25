def Salário_entre_2150_e_6950(salario_bruto):
    while salario_bruto < 2150 or salario_bruto > 6950:
        print("Por favor, digite um salário dentro da faixa especificada.") # CASO O COLABORADOR DIGITE UM SALARIO ONDE NAO SE ENCAIXA ENTRE 2150 E 6950
        salario_bruto = float(input("Salário do funcionário:"))
    return salario_bruto
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def Validar_Código_de_Função(codigo_funcao):
    while codigo_funcao != 102 and codigo_funcao != 101:
        print("Você digitou um codigo invalido!")
        codigo_funcao = int(input("Código da função:"))  # CODIGO DA FUNÇÃO QUE ELE EXERCE
    return codigo_funcao
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def Codigo_101_102(codigo_funcao):
    if codigo_funcao == 101:
        comissao = int(input("Volume de vendas no mês: "))
        salario_bruto = comissao*(9/100) + 1500
        if salario_bruto <= 2259.20:
            imposto = 0
        elif salario_bruto <= 2828.65:
            imposto = 7.5
        elif salario_bruto <=3751.05:
            imposto = 15
        elif salario_bruto <=4664.68:
            imposto = 22.5
        elif salario_bruto > 4664.68:
            imposto = 27.5
        faltas = faltas = int(input("Faltas: "))
        salario_bruto -= faltas*salario_bruto / 30
        desconto_imposto = salario_bruto*(imposto/100) 
        salario_liquido = salario_bruto-desconto_imposto   
        print(salario_bruto,imposto,desconto_imposto)
    if codigo_funcao == 102:
        print("Salário varia entre R$2150,00 até R$6950,00")
        salario_bruto = float(input("Salário do funcionário:"))
        salario_bruto = Salário_entre_2150_e_6950(salario_bruto)
        if salario_bruto <= 2259.20:
            imposto = 0
        elif salario_bruto <= 2828.65:
            imposto = 7.5
        elif salario_bruto <=3751.05:
            imposto = 15
        elif salario_bruto <=4664.68:
            imposto = 22.5
        elif salario_bruto > 4664.68:
            imposto = 27.5
        faltas = int(input("Faltas: "))
        salario_bruto -= faltas*salario_bruto / 30 
        desconto_imposto = salario_bruto*(imposto/100) 
        salario_liquido = salario_bruto-desconto_imposto   
    return codigo_funcao,salario_bruto,salario_liquido,faltas,imposto,desconto_imposto   
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def Menu_1():
    quantidade = int(input("Selecione a quantidade de funcionários que deseja inserir.\n:"))
    for i in range(quantidade):
        id_matricula = int(input("Digite o ID da matrícula: "))
        while id_matricula in funcionarios:
            print("ID de matrícula ja existente. Tente novamente!")
            id_matricula = int(input("Digite o ID da matrícula:"))
        nome = str(input("Nome do funcionário: ")).title() 
        print("[101] - VENDEDOR")
        print("[102] - ADMINISTRATIVO")
        codigo_funcao = int(input("Código da função:"))
        codigo_funcao = Validar_Código_de_Função(codigo_funcao)
        codigo_funcao,salario_bruto,salario_liquido,faltas,imposto,desconto_imposto = Codigo_101_102(codigo_funcao)
        funcionarios[id_matricula] = [nome,codigo_funcao,faltas,imposto,desconto_imposto,salario_bruto,salario_liquido]
        print("")
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def Menu_2(): 
    print("\t\t    REMOVER FUNCIONÁRIO")
    remover = int(input("\t\tDigite o ID da matrícula: "))
    while remover not in funcionarios:
        print("ID de matrícula não existente. Tente novamente!")
        remover = int(input("Digite o ID da matrícula:"))
    simnao = input("Confirmar remoção? (S/N):").upper()
    if simnao == "S":
        del funcionarios[(remover)]
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def Menu_3():
    find = int(input("ID_FUNCIONÁRIO: "))
    for id,funcionario in funcionarios.items():
        if find == id:
           print(f"""
              ID_MATRÍCULA: {id}
              NOME: {funcionario[0]}
              CÓDIGO FUNÇÃO: {funcionario[1]}
              SALÁRIO BRUTO: {funcionario[5]}
              PERCENTUAL DE IMPOSTO: {funcionario[3]}%
              SALÁRIO LIQUIDO: {funcionario[6]}""")
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def Menu_4():
    print(f"ID_MATRÍCULA\tNOME\tCÓDIGO_FUNÇÃO\tSALÁRIO_BRUTO\tSALÁRIO_lIQUIDO")
    print("="*72)
    for id,funcionario in funcionarios.items():
        print(f"{"":<5}{id:<11}{funcionario[0]:<13}{funcionario[1]:<13}{funcionario[5]:<16.2f}{funcionario[6]:.2f}")
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def Menu_5():
    maior = 0
    key = 0
    for id,funcionario in funcionarios.items():
        if funcionario[4] > maior:
            maior = funcionario[4]
            key = id
    for id,dados in funcionarios.items():
        if key == id:
            print(f"""
              ID_MATRÍCULA: {id}
              NOME: {dados[0]}
              CÓDIGO FUNÇÃO: {dados[1]}
              SALÁRIO BRUTO: {dados[5]}
              PERCENTUAL DE IMPOSTO: {dados[3]}%
              SALÁRIO LIQUIDO: {dados[6]}""")
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def Menu_6():
    maior_falta = 0
    key = 0
    for id,funcionario in funcionarios.items():
        if funcionario[2] > maior_falta:
            maior_falta = funcionario[2]
            key = id
    for id,dados in funcionarios.items():
        if key == id:
            print(f"""
              ID MATRÍCULA: {id}
              NOME: {dados[0]}
              CÓDIGO FUNÇÃO: {dados[1]}
              FALTAS: {dados[2]}
              DESCONTO: {dados[4]}""")           
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

funcionarios={}
menu = -1
while menu != 0: 
    menu = int(input(""" 
            ╔════════════════════════════════════╗
                            MENU  
                     
            ╚════════════════════════════════════╝
                  [1] - INSERIR FUNCIONÁRIOS
                     
                  [2] - REMOVER FUNCIONÁRIOS
                     
                  [3] - FOLHA DE PAGAMENTO
                     
                  [4] - RELATÓRIO DE SALÁRIO
                     
                  [5] - MAIOR SALÁRIO
                     
                  [6] - MAIOR NÚMERO DE FALTAS
                
                  [0] - Sair do Programa
            ╚═════════════════════════════════════╝
                          OPÇÃO: """))
    c=1
    if menu == 1:
        Menu_1()
    elif menu == 2:
        Menu_2()
    elif menu == 3:
        Menu_3()
    elif menu == 4:
        Menu_4()
    elif menu == 5:
        Menu_5()
    elif menu == 6:
        Menu_6()