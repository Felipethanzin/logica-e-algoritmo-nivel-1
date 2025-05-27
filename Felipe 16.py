qtd = int(input("Quantas maçãs deseja comprar? "))
if qtd < 12:
    preco = 1.30
else:
    preco = 1.00
total = qtd * preco
print(f"Total a pagar: R$ {total:.2f}")
