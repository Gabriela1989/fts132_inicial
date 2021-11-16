import pytest

# Definições
def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'impossível por zero'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

def calcular_area_do_quadrado (area, lado ):
    return area * lado

def calcular_area_do_retangulo (base, altura ):
    return base * altura

def calcular_area_do_triangulo (lado1, lado2):
    return lado1 * lado2 /2

def calcular_area_do_circulo(raio):
    return  3.14 * raio ** 2

# Requisições

if __name__ == '__main__':
    resultado = somar_dois_numeros(5, 7)
    print(f'A soma é {resultado}')

    resultado = subtrair_dois_numeros(7, 5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(3, 5)
    print(f'A multiplição é {resultado}')

    resultado = dividir_dois_numeros(8, 0)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2, 3)
    print(f'A exponenciação é {resultado}')

    resultado = calcular_area_do_quadrado(2,2)
    print(f'A área do quadrado é {resultado}')

    resultado = calcular_area_do_retangulo(3,3)
    print(f'A área do retangulo é {resultado}')

    resultado = calcular_area_do_triangulo(9,9)
    print(f'A área do triangulo é {resultado}')

    resultado = calcular_area_do_circulo(5)
    print(f'A área do circulo é {resultado}')


