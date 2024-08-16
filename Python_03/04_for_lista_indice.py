# Lista usando o laço for
print(" ")
print("Lista de Lojas")
print(" ")

lojas = ["Santo André", "São Bernardo", "SCS", "Mauá", "Diadema"]

# Listar usando laço
for i, loja in enumerate(lojas, 1):
    print(f"{i} - {loja}")