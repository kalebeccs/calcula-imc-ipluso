IMC_CLASSIFICACAO = [
    (18.5, 'Abaixo do peso'),
    (25, 'Peso normal'),
    (30, 'Sobrepeso'),
    (35, 'Obesidade Grau 1'),
    (40, 'Obesidade Grau 2'),
]

def calcula_IMC(peso: float, altura: float) -> float:
    """
    Calcula o Índice de Massa Corporal (IMC).
    :param peso: Peso da pessoa em quilogramas.
    :param altura: Altura da pessoa em metros.
    :return: float: Valor do IMC.
    """
    return peso / altura ** 2

def classifica_IMC(imc: float) -> str:
    """
    Classifica o Índice de Massa Corporal (IMC).
    :param imc: Valor do IMC calculado.
    :return: str: Classificação do IMC.
    """
    for limite, classificacao in IMC_CLASSIFICACAO:
        if imc < limite:
            return classificacao
    return 'Obesidade Grau 3'
