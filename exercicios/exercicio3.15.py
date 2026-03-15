cigarros_por_dia=int(input("Quantos cigarros você fuma por dia?"))
anos=int(input("Há quantos anos você fuma?"))
cigarros_totais=anos*365*cigarros_por_dia
tempo_perdido=cigarros_totais*10*24/60
print(f"Seu tempo perdido de vida é de {tempo_perdido} dias")