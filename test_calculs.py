# test_calculs.py - Mes 3 tests
from calculs import arrondi_5, remise, total

def test_arrondi_5():
    assert arrondi_5(3352) == 3350

def test_remise():
    assert remise(1000, 10) == 900

def test_total():
    assert total([500, 1000, 250]) == 1750

if __name__ == "__main__":
    test_arrondi_5()
    test_remise()
    test_total()
    print("Les 3 tests passent !")