#calculadora do estatístico
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"
    # se eu fosse usar exceção
    # try:
    #     return a / b
    # except ZeroDivisionError:
    #     return "Erro: Divisão por zero"
def potencia(a, b):
    return a ** b
