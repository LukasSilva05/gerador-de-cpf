import random

def calcular_digitos(digitos):
    contador_regressivo = len(digitos) + 1
    soma = sum(digito * (contador_regressivo - i) for i, digito in enumerate(digitos))
    resto = (soma * 10) % 11
    return 0 if resto > 9 else resto

def formatar_cpf(cpf): 
    return f'CPF gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def gerar_cpf():
    nove_digitos = [random.randint(0, 9) for _ in range(9)]
    primeiro_digito = calcular_digitos(nove_digitos)
    segundo_digito = calcular_digitos(nove_digitos + [primeiro_digito])
    cpf = ''.join(map(str, nove_digitos + [primeiro_digito, segundo_digito]))
    return formatar_cpf(cpf)

print(gerar_cpf())