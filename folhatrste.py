#========================================================================================================================
def Validar_Código_de_Função(codigo_funcao):
    while codigo_funcao != 102 and codigo_funcao != 101:
        print("Você digitou um codigo invalido!")
        codigo_funcao = int(input("Código da função:"))  # CODIGO DA FUNÇÃO QUE ELE EXERCE
    return codigo_funcao
#========================================================================================================================
def Salário_entre_2150_e_6950(salario_bruto):
    while salario_bruto < 2150 or salario_bruto > 6950:
        print("Por favor, digite um salário dentro da faixa especificada.") # CASO O COLABORADOR DIGITE UM SALARIO ONDE NAO SE ENCAIXA ENTRE 2150 E 6950
        salario_bruto = float(input("Salário do funcionário:"))
    return salario_bruto
#========================================================================================================================
def Salário_Liquido_101_e_102(codigo_funcao):
    if codigo_funcao == 101:
        codigo_funcao = "101 - VENDEDOR"
        salario_bruto = 1500
        faltas = int(input("Faltas: "))
        salario_bruto -= faltas*(salario_bruto)/30 
        comissao = int(input("Volume de vendas no mês: "))
        salario_bruto += comissao*(9/100)
        salario_liquido = salario_bruto
        imposto = 0
    elif codigo_funcao == 102:
        codigo_funcao = "102 - ADMINISTRATIVO"
        print("Salário varia entre R$2150,00 até R$6950,00")
        salario_bruto = float(input("Salário do funcionário:"))

        salario_bruto=Salário_entre_2150_e_6950(salario_bruto)

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
    return codigo_funcao,salario_bruto,imposto,salario_liquido,faltas,desconto_imposto
#========================================================================================================================
def Menu_1_Inserir_Funcionario():  
        c=1
        print("Selecione a quantidade de funcionários que deseja inserir.")
        quantidadex = int(input("Quantidade: "))
        while c<=quantidadex:
            id_matricula = int(input("Digite o ID da matrícula: "))
            if id_matricula in funcionarios:
                print("ID já existente. Tente novamente")
                continue
            else:
                nome = str(input("Nome do funcionário: ")).title() # ADICIONADO NOME DO FUNCIONARIO
                print()
                print("[101] - Vendedor\n[102] - Administrativo")
                codigo_funcao = int(input("Código da função:"))  # CODIGO DA FUNÇÃO QUE ELE EXERCE
                codigo_funcao=Validar_Código_de_Função(codigo_funcao)
                codigo_funcao,salario_bruto,imposto,salario_liquido,faltas,desconto_imposto = Salário_Liquido_101_e_102(codigo_funcao)
                funcionarios[id_matricula] = [nome,codigo_funcao,salario_bruto,imposto,salario_liquido,faltas,desconto_imposto] # ATRIBUINDO O FUNCIONARIO NO DICIONARIO "FUNCIONARIOS"
                c+=1
        return funcionarios 
#========================================================================================================================
def Menu_2_Remover_Funcionario(): # SEGUNDA OPÇÃO DO MENU
        print("Remoção de funcionário.")
        remover = int(input("Código do funcionário: "))
        del funcionarios[(remover)] # REMOVE O CODIGO QUE O COLABORADOR QUER
#========================================================================================================================
def Menu_3_Folha_de_Pagamento_Por_ID():  # TERCEIRA OPÇÃO DO MENU
        print("Determinar folha de pagamento por ID de determinado funcionário")
        key = int(input("ID do(a) funcionário: ")) # PROCURAR POR ID
        for achar in funcionarios.keys(): # PERCORRE PELAS CHAVES DO DICIONARIO FUNCIONARIOS E ENTRA NA CONDIÇÃO
            if key==achar: # QUANDO O PERCORRER FOR O MESMO QUE A KEY QUE O USUARIO DIGITOU ELE ENTRA NO FOR E MOSTRA TODAS AS INFORMAÇÕES DO FUNCIONÁRIO
                for id,dados in funcionarios.items():
                    print(f"""
            ID: {id}
            NOME: {dados[0]}
            CODIGO: {dados[1]}
            SALÁRIO BRUTO: R${dados[2]}
            PORCENTUAL DO IMPOSTO: {dados[3]}%""")
#========================================================================================================================
def Menu_4_Relatório_Salário_Bruto_e_Salario_Liquido():
    for codigo,dados in funcionarios.items():
        print(f"""
            ID: {codigo}
                NOME: {dados[0]}
                SALÁRIO BRUTO: {dados[2]}
                SALÁRIO LIQUIDO: {dados[4]}
                FALTAS: {dados[5]}
              """)
#========================================================================================================================
def Menu_5_Maior_Salário():
    maior = 0 
    for salario in funcionarios.values(): 
        if salario[4] > maior :
            maior = salario[4]   
    for id,dados in funcionarios.items():
        if dados[4] == maior:
            print(f"""
              ID MATRÍCULA: {id}
              NOME: {dados[0]}
              CÓDIGO: {dados[1]}
              SALÁRIO BRUTO: {dados[2]}
              PERCENTUAL DE IMPOSTO: {dados[3]}%
              SALÁRIO LIQUIDO: {dados[4]}""")
#========================================================================================================================
def Menu_6_Maior_Faltas(): 
    maior_falta = 0
    for faltas in funcionarios.values():
        if faltas[5] > maior_falta:
            maior_falta = faltas[5] # ACHA O MAIOR NÚMERO DE FALTA
    for id,dados in funcionarios.items():
        if dados[5] == maior_falta: # ACHA QUEM TEM O MAIOR NÚMERO DE FALTAS
            print(f"""
                  ID MATRÍCULA: {id}
                  NOME: {dados[0]}
                  CÓDIGO: {dados[1]}
                  NÚMERO DE FALTAS: {dados[5]}
                  DESCONTO DE SALÁRIO: {dados[6]}""")    
#========================================================================================================================
print("\t    Marketing é TUDO!")
funcionarios = {} # ╗ ═ ╚ ╔ ╝
menu = -1
while menu != 0: 
    menu = int(input(""" 
            ╔════════════════════════════════════╗
                            MENU  
            ╚════════════════════════════════════╝
                  [1] - Inserir Funcionários 
                     
                  [2] - Remover Funcionários 
                     
                  [3] - Folha de Pagamento
                     
                  [4] - Relatório de Salário
                     
                  [5] - Maior Salário
                     
                  [5] - Maior número de faltas
            ╚═════════════════════════════════════╝
                          OPÇÃO: """))
    if menu == 1:
        Menu_1_Inserir_Funcionario()
    elif menu == 2:
        Menu_2_Remover_Funcionario()
    elif menu == 3:
        Menu_3_Folha_de_Pagamento_Por_ID()
    elif menu == 4:
        Menu_4_Relatório_Salário_Bruto_e_Salario_Liquido()
    elif menu == 5:
        Menu_5_Maior_Salário()
    elif menu == 6:
        Menu_6_Maior_Faltas()