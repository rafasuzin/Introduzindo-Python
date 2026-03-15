preço_produto=float(input("Qual é o preço do produto?"))

desconto=float(input("Qual é o percentual de desconto aplicado ao produto(s)?"))

valor_desconto=preço_produto*desconto/100

print(f"O valor do desconto é R${valor_desconto:.2f}")

produto_com_desconto=preço_produto-(valor_desconto)

print(f"O preço do produto com desconto de {desconto}% é R${produto_com_desconto:.2f}")
