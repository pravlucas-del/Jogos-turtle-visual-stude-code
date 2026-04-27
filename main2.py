
def decimal_para_base(n,b):
    if n == 0:
        return '0'
    digitos = ''
    while n > 0:
        digitos = str(n % b) + digitos
        n //= b
        return digitos
    
def base_para_decimal(n_str,b):
    return int(str(n_str), b)

def verificar_bilingue():
    base_origem = int(input("Digite a base de origem : "))
    num_entrada = input("Digite o número na base de origem (2-9): ")
    num_decimal = base_para_decimal(num_entrada, base_origem)
    representacao = {}
    for b in range(2, 10):
        representacao[b] = decimal_para_base(num_decimal, b)
        print(f"Base {b}: {representacao}")
        if representacao[b] == num_entrada:
            print(f"O número {num_entrada} é bilíngue na base {b}!")
        elif representacao[b] == num_entrada:
            print(f"O número {num_entrada} é bilíngue na base {b}!")

print("Bem-vindo ao verificador de números bilíngues!")
verificar_bilingue()

        
        

