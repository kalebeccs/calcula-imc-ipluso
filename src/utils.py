IMC_CLASSIFICACAO = [
    (18.5, 'Abaixo do peso'),
    (25, 'Peso normal'),
    (30, 'Sobrepeso'),
    (35, 'Obesidade Grau 1'),
    (40, 'Obesidade Grau 2'),
]

def calcula_IMC(peso, altura):
    return peso / altura ** 2

def classifica_IMC(imc):
    for limite, classificacao in IMC_CLASSIFICACAO:
        if imc < limite:
            return classificacao
    return 'Obesidade Grau 3'
