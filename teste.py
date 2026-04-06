import math

def volume_cilindro(raio, altura):
    """Calcula o volume de um cilindro: V = pi * r^2 * h"""
    return math.pi * (raio ** 2) * altura

def obter_espessura(tipo_revestimento):
    """Retorna a espessura com base no tipo de revestimento"""
    if tipo_revestimento == 'epoxi':
        return 0.003
    elif tipo_revestimento == 'fibra_vidro':
        return 0.005
    elif tipo_revestimento == 'azulejo':
        return 0.007
    else:
        return 0.0

def volume_util(raio, altura, tipo_revestimento):
    # Obtém a espessura usando a função auxiliar
    e = obter_espessura(tipo_revestimento)
    
    # Calcula as dimensões úteis (internas)
    # O raio útil é o raio original menos a espessura da parede
    # A altura útil é a altura original menos a espessura do fundo
    raio_u = raio - e
    altura_u = altura - e
    
    # Garante que as dimensões não sejam negativas
    if raio_u < 0 or altura_u < 0:
        return 0.0
    
    # Retorna o volume utilizando a função de cálculo de cilindro
    return volume_cilindro(raio_u, altura_u)

volume_cilindro(10,50)
obter_espessura(0.003)
volume_util(5,10,'epoxi')