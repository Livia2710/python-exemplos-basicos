valor = int(input("Informe o valor: "))

# uso de if ternario
teste = "Stuação normal." if valor< 100 else "situação pré-diabetes." if valor in range(100, 125) else "Diabetes"

# Exibição
print(teste)