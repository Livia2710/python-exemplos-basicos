dia = (input("Indique o dia da semana: "))

# Função Fim de Semana
def dia_da_semana(dia):
    match dia:
        case "Domingo" | "Sabado":
            return "Fim de semana"
        
        case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
            return "Dia útil"
        
        case "Domingo" | "Sabado":
            return "Fim de semana"
        case _:
            return "Valor inválido"

    

# Exibe o resultado da função na tela 
print(dia_da_semana(dia))

