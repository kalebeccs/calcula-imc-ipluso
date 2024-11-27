def calcula_IMC(peso, altura):
    return peso / altura ** 2

def classifica_IMC(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        return 'Peso normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    elif 30 <= imc < 35:
        return 'Obesidade Grau 1'
    elif 35 <= imc < 40:
        return 'Obesidade Grau 2'
    else:
        return 'Obesidade Grau 3'
