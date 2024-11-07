def mes_por_extenso(mes):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    return meses[mes - 1] if 1 <= mes <= 12 else None

def validar_data(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes in [4, 6, 9, 11] and dia == 31:
        return False
    if mes == 2:
        # Verifica se o ano é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return dia <= 29
        return dia <= 28

    return True

def data_formatada(data):
    try:
        dia, mes, ano = map(int, data.split('/'))

        if not validar_data(dia, mes, ano):
            return None

        mes_extenso = mes_por_extenso(mes)
        if mes_extenso:
            return f"{dia} de {mes_extenso} de {ano}"
        else:
            return None

    except ValueError:
        return None

# Solicitar a entrada do usuário
data_input = input("Digite a data no formato DD/MM/AAAA: ")
resultado = data_formatada(data_input)
if resultado:
    print(resultado)  # Exibe a data formatada
else:
    print("Data inválida")