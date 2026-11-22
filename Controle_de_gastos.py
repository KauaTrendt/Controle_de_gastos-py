print("-"*20)
print("Controle de gastos")
print("-"*20)

despesas=[]
valores=[]

while True:

    print("1-Adicionar despesas")
    print("2-Listas despesas")
    print("3-Calcular despesas")
    print("4-Sair")
.gi
    opcao=input("Escolha uma opção: ")

    if opcao =="1":
        despesa=input("Nome da despesa: ")
        while True:
            valor=float(input("Valor da despesa: "))
            if valor>=0:
                break
            print("O valor não pode ser negativo")

        despesas.append(despesa)
        valores.append(valor)

        print("Despesa adicionada!")    
        print("Despesa cadastrada!")

    elif opcao=="2":
        if despesas:
         print(despesas)
        else:
            print("Nenhuma despesa cadastrada")
    
    elif opcao=="3":
        if valores:
            total=sum(valores)
            print(f"Total gasto: R$ {total:.2f}")
        else:
            print("Nenhuma despesa cadstrada")
    
    elif opcao=="4":
        break
    else:
        print("Opção invalida")
    
    input("\nPressione ENTER para continuar")
