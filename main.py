while True:
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        
        ano_atual = 2026 - ano_nascimento
    
        if ano_atual >= 18:
            print(f"Você é maior de idade e tem {ano_atual} anos.")
        else:
            print(f"Você é menor de idade e tem {ano_atual} anos.")
        
    except:
        print("Por favor, digite um número válido para o ano de nascimento.")