import pytest

# ==============================
# Tests para int_to_bits y bits_to_int
# ==============================
from Simulador_Sumador_Restador import int_to_bits, bits_to_int, sumador_restador_4bits

def test_int_to_bits_and_back():
    for n in range(16):
        bits = int_to_bits(n)
        assert bits_to_int(bits) == n, f"Error en conversión para {n}"

# ==============================
# Tests de suma
# ==============================
@pytest.mark.parametrize("A,B,expected", [
    (0, 0, 0),
    (1, 1, 2),
    (5, 3, 8),
    (7, 8, 15),
    (15, 0, 15),
])
def test_suma(A, B, expected):
    a_bits = int_to_bits(A)
    b_bits = int_to_bits(B)
    result, carry = sumador_restador_4bits(a_bits, b_bits, 0)
    assert bits_to_int(result) == expected, f"Suma {A} + {B} incorrecta"

# ==============================
# Tests de resta
# ==============================
@pytest.mark.parametrize("A,B,expected", [
    (0, 0, 0),
    (1, 1, 0),
    (5, 3, 2),
    (7, 2, 5),
    (15, 5, 10),
])
def test_resta(A, B, expected):
    a_bits = int_to_bits(A)
    b_bits = int_to_bits(B)
    result, carry = sumador_restador_4bits(a_bits, b_bits, 1)
    assert bits_to_int(result) == expected, f"Resta {A} - {B} incorrecta"

# ==============================
# Test acarreo
# ==============================
def test_carry_suma():
    # 15 + 1 = 16 (overflow)
    a_bits = int_to_bits(15)
    b_bits = int_to_bits(1)
    result, carry = sumador_restador_4bits(a_bits, b_bits, 0)
    assert carry == 1, "Error: Carry no detectado para 15 + 1"
    assert bits_to_int(result) == 0, "Error: Resultado incorrecto con overflow"
