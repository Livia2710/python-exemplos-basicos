sabor = int(input("Indique o sabor desejado: "))

# Função Fim de Semana
def sabor_pizza(sabor):
    match sabor:
        case 1:
            return print ("Mussarela")
        case 2:
            return print ("Calabresa")
        
        case 3:
            return print ("Frango c/ catupiry")
        
        case 4:
            return print ("Portugesa")
        
        case _:
            return  print("Sabor")

    
# Exibe o resultado da função na tela 
sabor_pizza(sabor)

