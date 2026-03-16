distancia=float(input("Quantos kilômetros foram percorridos?"))
dias=int(input("Por quantos dias o carro foi alugado?"))
total_a_pagar=60*dias+0.15*distancia
print(f"Ao percorrer {distancia:.2f}km e alugar o carro por {dias} dias, sua dívida total a pagar é {total_a_pagar:.2f}") 
