import random

# ---------- Gerando os nove primeros  ---------- 
nove_digitos = [random.randint(0,9) for _ in range(9)]

# ---------- Cálculo do primeiro dígito ----------
contador_regressivo = 10
soma_dos_nove_primeiros = 0

for digito in nove_digitos:
    soma_dos_nove_primeiros += digito * contador_regressivo
    contador_regressivo -= 1

primeiro_digito_final_do_cpf = (soma_dos_nove_primeiros * 10) % 11

if primeiro_digito_final_do_cpf > 9:
    primeiro_digito_final_do_cpf = 0

# ---------- Cálculo do segundo dígito ----------
dez_primeiros_digitos = nove_digitos + [primeiro_digito_final_do_cpf]

contador_regressivo = 11
soma_dos_dez_primeiros = 0
for digito in dez_primeiros_digitos:
    soma_dos_dez_primeiros += digito * contador_regressivo
    contador_regressivo -= 1


segundo_digito_final_do_cpf = (soma_dos_dez_primeiros * 10) % 11

if segundo_digito_final_do_cpf > 9:
    segundo_digito_final_do_cpf = 0

cpf_gerado_pelo_calculo = ''.join([str(digito) for digito in nove_digitos + [primeiro_digito_final_do_cpf] + [segundo_digito_final_do_cpf]])

print(f'CPF gerado: {cpf_gerado_pelo_calculo[:3]}.{cpf_gerado_pelo_calculo[3:6]}.{cpf_gerado_pelo_calculo[6:9]}-{cpf_gerado_pelo_calculo[9:]}')