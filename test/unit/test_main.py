import pytest

from main import \
    somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, \
    dividir_dois_numeros, elevar_um_numero_pelo_outro, calcular_area_do_quadrado, \
    calcular_area_do_retangulo, calcular_area_do_triangulo, calcular_area_do_circulo, \
    calcular_volume_do_paralelograma

def testar_somar_dois_numeros():
    # - 1ª Etapa : Configura/ Prepara
    # Input/output

    num1 = 4
    num2 = 5

    resultado_esperado = 9

# - Etapa 2: Executa

    resultado_atual = somar_dois_numeros(num1, num2)

# - Etapa 3: Confirma/Check/valida

    assert resultado_atual == resultado_esperado

def testar_subtrair_dois_numeros():

    num1 = 10
    num2 = 9
    resultado_esperado = 1

    resultado_atual = subtrair_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_multiplicar_dois_numeros():

    num1 = 5
    num2 = 2
    resultado_esperado = 10

    resultado_atual = multiplicar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_dividir_dois_numeros():

    num1 = 10
    num2 = 2
    resultado_esperado = 5

    resultado_atual = dividir_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_dividir_dois_numeros():

    num1 = 10
    num2 = 2
    resultado_esperado = 5

    resultado_atual = dividir_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_elevar_um_numero_pelo_outro():

    num1 = 2
    num2 = 3
    resultado_esperado = 8

    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_quadrado():

    area = 2
    lado = 2
    resultado_esperado = 4

    resultado_atual = calcular_area_do_quadrado(area, lado)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_retangulo():

    base = 5
    altura = 5
    resultado_esperado = 25

    resultado_atual = calcular_area_do_retangulo(base, altura)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_triangulo():

    lado1 = 6
    lado2 = 6
    resultado_esperado = 36

    resultado_atual = calcular_area_do_triangulo(lado1 * lado2)
    assert resultado_atual == resultado_esperado

#anotação para utilizar como massa de teste
@pytest.mark.parametrize ('raio,resultado_esperado',[
                              # valores
                              (1,3.14 ), # teste n 1
                              (2,12.56), # teste n 2
                              (3,28.26), # teste n 3
                              (4,50.24), # teste n 4
                              ('a' , 'Falha no cálculo - Raio não é um número'), # teste n 5
                              (' ' , 'Falha no cálculo - Raio não é um número'), # teste n 6
                        ])
def testar_calcular_area_do_circulo(raio, resultado_esperado):

    #raio = 2
    #resultado_esperado = 12.56

    resultado_atual = calcular_area_do_circulo(raio)
    assert resultado_atual == resultado_esperado

def testarcalcular_volume_do_paralelograma():
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)
    assert resultado_atual == resultado_esperado



