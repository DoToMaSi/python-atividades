# Boas Vindas
print('Bem-vindo a loja Douglas Tomacheski')

# Capturo o valor unitário
valor_unitario = float(input('Entre com o valor do produto: '))

# Capturo a quantidade
quantidade = int(input('Entre com a quantidade do produto: '))

# Calculo o valor total
valor_total = valor_unitario * quantidade

# Crio a variavel para a porcentagem de desconto e valor final
desconto = 0
valor_final = 0

# Valido condicionais de valor de desconto
if (valor_total >= 2500 and valor_total < 6000):
    desconto = 0.04

elif (valor_total >= 6000 and valor_total < 10000):
    desconto = 0.07

elif (valor_total >= 10000):
    desconto = 0.11

# Faço o cálculo do valor líquido
valor_final = valor_total - (valor_total * desconto)

# Exibo o valor sem desconto
print(f'O valor SEM desconto: {valor_total:.2f}')

# Caso haja desconto, exibo o desconto e o valor líquido.
if (desconto > 0):
    print(f'O valor COM desconto de {(desconto * 100):.0f}%: {valor_final:.2f}')
else:
    print('Não houve desconto nesta compra')