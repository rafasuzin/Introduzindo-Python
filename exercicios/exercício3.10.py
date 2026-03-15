salario=float(input("Qual é o seu salário?"))
porcentagem=float(input("Qual será o aumento desse salário, em porcentagem?"))
aumento=salario*porcentagem/100
print(f"Seu aumento será de R${aumento:.2f}")
salario+=aumento
print(f"Seu salário com o aumento é R${salario:.2f}")