velocidade = int(input("Informe a velocidade: "))

# uso de if ternario
alerta = "Alta velocidade! Multado." if velocidade> 60 else "Dentro do limite de velocidade."

# Exibição
print(alerta)