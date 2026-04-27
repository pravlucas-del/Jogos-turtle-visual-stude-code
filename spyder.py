from math import*

import math

def volume_cilindro(r,h):
    return math.pi * (r **2) * h

def volume_perdido(r,h,e):
    return math.pi *r *h *(2*r*e-e**2) + math.pi*(r-e)**2*e

def volume_util(r,h,tipo_revestimento):
    if tipo_revestimento == 'epoxi':
        espessura = 0.003
    elif tipo_revestimento == 'fibra_vidro':
        espessura = 0.005
    elif tipo_revestimento == 'azulejo':
        espessura = 00.7
    else:
        espessura = 0.0
    total = volume_cilindro(r,h)
    perdido = volume_perdido(r,h,e)
    return total - perdido


# Bloco Principal

def main():
    print("=== DADOS DO RESERVATÓRIO 1 ===")   
    r1 = float(input("Raio do Reservatório 1 (m) : "))
    h1 = float(input("Altura do Reservatório 1 (m) : "))
    rev1 = input("Tipo de revestimento (epoxi/fibra_vidro/azulejo/outro)) : ")


    print("=== DADOS DO RESERVATÓRIO 2 ===")   
    r2 = float(input("Raio do Reservatório 2 (m) : "))
    h2 = float(input("Altura do Reservatório 2 (m) : "))
    rev2 = input("Tipo de revestimento (epoxi/fibra_vidro/azulejo/outro)) : ")

    v_util1 = volume_util(r1,h1,rev1)
    v_util2 = volume_util(r2,h2,rev2)

    print("=== RESULTADOS ===")
    print(f"Reservatório 1 - Volume útil: {v_util1:.2f} metro cúbico")
    print(f"Reservatório 2 - Volume útil: {v_util2:.2f} metro cúbico")
    if v_util1 > v_util2:
        print(f"Reservatório 1 tem maior volume útil")
    elif v_util2 > v_util1:
        print(f"Reservatório 2 tem maior volume útil")
    else:
        print(f"Ambos possuem o mesmo volume útil")

main()










    

