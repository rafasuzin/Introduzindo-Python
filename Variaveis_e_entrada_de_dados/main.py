nome=input("Qual é o seu nome?")
print(f"Muito prazer, {nome}")
idade=int(input(f"Quantos anos você tem, {nome}?"))
salario=float(input(f"Qual é o seu salario, {nome}?"))
bonus=salario*idade/2
print(f"seu bonus é de R${bonus:6.2f}")