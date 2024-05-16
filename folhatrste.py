def Validar_Código_de_Função(codigo_funcao):
    while codigo_funcao != 102 and codigo_funcao != 101:
        print("Vocfe digitou um codigo invalido!")
        print("entre com outro codigo valido")
        codigo_funcao = int(input("Código da função:"))  # CODIGO DA FUNÇÃO QUE ELE EXERCE
#========================================================================================================================
def inserir_funcionario():  
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
                Validar_Código_de_Função(codigo_funcao)
                if codigo_funcao == 101:
                    codigo_funcao = "101 = VENDEDOR"
                    salario_bruto = 1500
                    imposto = 0
                elif codigo_funcao == 102:
                    codigo_funcao = "102 - ADMINISTRATIVO"
                    print("Salário varia entre R$2150,00 até R$6950,00")
                    salario_bruto = float(input("Salário do funcionário:"))
                    while salario_bruto < 2150 or salario_bruto > 6950:
                        print("Por favor, digite um salário dentro da faixa especificada.") # CASO O COLABORADOR DIGITE UM SALARIO ONDE NAO SE ENCAIXA ENTRE 2150 E 6950
                        salario_bruto = float(input("Salário do funcionário:"))
                    if salario_bruto <= 2259.20:
                        imposto = 0
                        print("O funcionário está livre de impostos")
                    elif salario_bruto <= 2828.65:
                        imposto = 7.5
                    elif salario_bruto <=3751.05:
                        imposto = 15
                    elif salario_bruto <=4664.68:
                        imposto = 22.5
                    elif salario_bruto > 4664.68:
                        imposto = 27.5
                
                    # desconto_imposto = salario_bruto*(imposto/100) #
                    # salario_liquido = salario_bruto-desconto_imposto #
                funcionarios[id_matricula] = [nome,codigo_funcao,salario_bruto,imposto] # ATRIBUINDO O FUNCIONARIO NO DICIONARIO "FUNCIONARIOS"
            c+=1       
#========================================================================================================================
def remover_funcionario(): # SEGUNDA OPÇÃO DO MENU
        print("Remoção de funcionário.")
        remover = int(input("Código do funcionário: "))
        del funcionarios[(remover)] # REMOVE O CODIGO QUE O COLABORADOR QUER
#========================================================================================================================
def folha_de_pagamento():  # TERCEIRA OPÇÃO DO MENU
        print("Determinar folha de pagamento por ID de determinado funcionário")
        key = int(input("ID do(a) funcionário: ")) # PROCURAR POR ID
        for achar in funcionarios.keys(): # PERCORRE PELAS CHAVES DO DICIONARIO FUNCIONARIOS E ENTRA NA CONDIÇÃO
            if key==achar: # QUANDO O PERCORRER FOR O MESMO QUE A KEY QUE O USUARIO DIGITOU ELE ENTRA NO FOR E MOSTRA TODAS AS INFORMAÇÕES DO FUNCIONÁRIO
                for id,outros in funcionarios.items():
                    print(f"""
            ID: {id}
            NOME: {outros[0]}
            CODIGO: {outros[1]}
            SALÁRIO BRUTO: R${outros[2]}
            PORCENTUAL DO IMPOSTO: {outros[3]}
                     """)
                    if outros[3] == 0:
                        print("\t  Funcionário isento de impostos")
#========================================================================================================================
print("\t    Marketing é TUDO!")
funcionarios = {}

menu = -1
while menu != 0:
    menu = int(input("""
       |================================|
       | [1] - Adicionar funcionários.  |
       |                                |
       | [2] - Remover funcionários.    |
       |                                |
       | [3] - Folha de pagamento por ID|
       |                                |
       | [0] - Sair do programa         |
       |================================|
                    OPÇÃO:"""))
    if menu == 1:
        inserir_funcionario()
    elif menu == 2:
        remover_funcionario()
    elif menu == 3:
        folha_de_pagamento()
    
    
