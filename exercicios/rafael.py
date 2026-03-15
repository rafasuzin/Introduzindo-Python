#modo antigo
nome="Leo"
idade=14
grana=74.89
print("%s tem %d anos e R$%f no bolso" %(nome, idade, grana))

print("%8s tem %03d anos e R$%4.2f no bolso" %(nome, idade, grana))

print("%8s tem %3d anos e R$%4.1f no bolso" %(nome, idade, grana))

print("%-8s tem %-3d anos e R$%-4.2f no bolso" %(nome, idade, grana))

#modo format

print("{} tem {} anos e R${} no bolso".format(nome, idade, grana))

print("{:8} tem {:03} anos e R${:4.2f} no bolso".format(nome, idade, grana))

print("{:8} tem {:3} anos e R${:4.1f} no bolso".format(nome, idade, grana))

print("{:<8} tem {:<3} anos e R${:<4.2f} no bolso".format(nome, idade, grana))

#modo f-string

print(f"{nome} tem {idade} anos e R${grana} no bolso")

print(f"{nome:8} tem {idade:03} anos e R${grana:4.2f} no bolso")

print(f"{nome:8} tem {idade:3} anos e R${grana:4.1f} no bolso")

print(f"{nome:<8} tem {idade:<3} anos e R${grana:<4.2f} no bolso")