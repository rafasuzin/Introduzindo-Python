V=int(input("Qual é a velocidade do seu carro?"))
if V<=80:
    print("Você está dentro do limite, então não será multado")
if V>80:
    Excesso=V-80
    Multa=Excesso*5
    print(f"Você ultrapassou a velocidade limite em {Excesso} km/h, portanto, pagará uma multa de R${Multa:.2f}")