from code.main import suma, resta, multiplicacion, division
import pytest


@pytest.mark.parametrize(
    (       ## Set de parametros
        "a",
        "b",
        "valor_esperado",
    ),

    [
        (   ## Caso1
            2,
            3,
            5,
        ),

        (   ## Caso2
            4,
            5,
            9,
        )
    ],
    ids=[
        "test_1",
        "test_2",
    ]
)
def test_suma(a, b, valor_esperado):
    assert suma(a, b) == valor_esperado


@pytest.mark.parametrize(
    (       ## Set de parametros
        "a",
        "b",
        "valor_esperado",
    ),

    [
        (   ## Caso1
            2,
            3,
            -1,
        ),

        (   ## Caso2
            4,
            5,
            -1,
        )
    ],
    ids=[
        "test_1",
        "test_2",
    ]
)
def test_resta(a, b, valor_esperado):
    assert resta(a, b) == valor_esperado

#@pytest.mark.skip(reason = "Funcion que se va a depricar")
@pytest.mark.xfail()
def test_division():
    assert division(2,0) == 2