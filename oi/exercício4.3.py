a=int(input("Digite o primeiro número:"))
b=int(input("Digite o segundo número:"))
c=int(input("Digite o terceiro número"))
if a>b and a>c:
    print(f"O primeiro número ({a}) é o maior")
if b>a and b>c:
    print(f"O segundo número ({b}) é o maior")
if c>a and c>b:
    print(f"O terceiro número ({c}) é o maior")

if a<b and a<c:
    print(f"O primeiro número ({a}) é o menor")
if b<a and b<c:
    print(f"O segundo número ({b}) é o menor")
if c<a and c<b:
    print(f"O terceiro número ({c}) é o menor")