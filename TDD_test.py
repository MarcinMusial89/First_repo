import functions

print(functions.multiply(5, 6))

def test_multiplay():
    assert functions.multiply(5, 10) == 50 #first test
    assert functions.multiply(100, 1.1) == 110
    assert functions.multiply(1.5, 1.5) == 2.25
    assert functions.multiply(0.0000001, 100) == 0.00001
    assert functions.multiply(None, 5) == None

def test_number_of_letter():
    assert functions.no_of_letter('mama') == 4
    assert functions.no_of_letter('mama.tata') == 8
    #nie odpowiedzielimsy na ten warunek