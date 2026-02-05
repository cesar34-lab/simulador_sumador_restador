"""
Simulador de Sumador–Restador de 4 Bits
=====================================

Autor: César Alberto Mora Duarte
Proyecto: Simulación de un sumador–restador binario de 4 bits
Lenguaje: Python 3

Descripción:
------------
Este programa simula el funcionamiento de un sumador–restador binario
de 4 bits utilizando únicamente compuertas lógicas AND, OR y NOT.
La operación de resta se realiza mediante el método de complemento a dos.

El sistema emula el comportamiento de un circuito digital combinacional,
empleando sumadores completos (Full Adders) conectados en cascada.

El código está documentado con docstrings para facilitar su comprensión,
mantenimiento y evaluación académica.
"""

def AND(a, b):
    """
    Compuerta lógica AND.

    Parámetros:
        a (int): Bit de entrada (0 o 1).
        b (int): Bit de entrada (0 o 1).

    Retorna:
        int: Resultado de la operación AND.
    """
    return a & b


def OR(a, b):
    """
    Compuerta lógica OR.

    Parámetros:
        a (int): Bit de entrada (0 o 1).
        b (int): Bit de entrada (0 o 1).

    Retorna:
        int: Resultado de la operación OR.
    """
    return a | b


def NOT(a):
    """
    Compuerta lógica NOT.

    Parámetros:
        a (int): Bit de entrada (0 o 1).

    Retorna:
        int: Negación lógica del bit de entrada.
    """
    return 1 - a

def XOR(a, b):
    """
    Compuerta lógica XOR construida a partir de compuertas básicas.

    Expresión lógica:
        A XOR B = (A AND NOT(B)) OR (NOT(A) AND B)

    Parámetros:
        a (int): Bit de entrada.
        b (int): Bit de entrada.

    Retorna:
        int: Resultado de la operación XOR.
    """
    return OR(AND(a, NOT(b)), AND(NOT(a), b))


def full_adder(a, b, cin):
    """
    Sumador completo de un bit.

    Parámetros:
        a (int): Bit del operando A.
        b (int): Bit del operando B.
        cin (int): Bit de acarreo de entrada.

    Retorna:
        tuple:
            sum_bit (int): Bit de suma.
            carry_out (int): Bit de acarreo de salida.
    """
    suma_parcial = XOR(a, b)
    sum_bit = XOR(suma_parcial, cin)

    carry1 = AND(a, b)
    carry2 = AND(suma_parcial, cin)
    carry_out = OR(carry1, carry2)

    return sum_bit, carry_out

def sumador_restador_4bits(A, B, M):
    """
    Sumador–restador binario de 4 bits.

    Modo de operación:
        M = 0 → Suma
        M = 1 → Resta (complemento a dos)

    Parámetros:
        A (list): Operando A (4 bits, LSB primero).
        B (list): Operando B (4 bits, LSB primero).
        M (int): Señal de control del modo.

    Retorna:
        tuple:
            result (list): Resultado binario de 4 bits.
            carry_out (int): Acarreo final.
    """
    resultado = []
    carry = M

    for i in range(4):
        b_mod = XOR(B[i], M)
        suma, carry = full_adder(A[i], b_mod, carry)
        resultado.append(suma)

    return resultado, carry


def int_to_bits(numero):
    """
    Convierte un número entero a binario de 4 bits.

    Parámetros:
        numero (int): Número entre 0 y 15.

    Retorna:
        list: Lista de 4 bits (LSB primero).
    """
    return [(numero >> i) & 1 for i in range(4)]


def bits_to_int(bits):
    """
    Convierte una lista de bits a número entero.

    Parámetros:
        bits (list): Lista de 4 bits (LSB primero).

    Retorna:
        int: Número entero equivalente.
    """
    return sum(bits[i] << i for i in range(4))

if __name__ == "__main__":
    """
    Bloque principal de ejecución para pruebas del sistema.
    """

    A = int_to_bits(5)  # 0101
    B = int_to_bits(3)  # 0011

    # Prueba de suma
    resultado_suma, carry_suma = sumador_restador_4bits(A, B, 0)
    print("Suma 5 + 3 =", bits_to_int(resultado_suma), "Carry:", carry_suma)

    # Prueba de resta
    resultado_resta, carry_resta = sumador_restador_4bits(A, B, 1)
    print("Resta 5 - 3 =", bits_to_int(resultado_resta))
