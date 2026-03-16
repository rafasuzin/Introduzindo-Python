salario=float(input("Qual é o seu salário?"))
if salario<=1250:
    aumento=salario*0.15
    print(f"O seu aumento será de R${aumento:.2f}")
if salario>1250:
    aumento=salario*0.1
    print(f"O seu aumento será de R${aumento:.2f}")