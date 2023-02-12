# import functions
#
# print(functions.multiply(5, 6))
#
# def test_multiplay():
#     assert functions.multiply(5, 10) == 50 #first test
#     assert functions.multiply(100, 1.1) == 110
#     assert functions.multiply(1.5, 1.5) == 2.25
#     assert functions.multiply(0.0000001, 100) == 0.00001
#     assert functions.multiply(None, 5) == None
#
# def test_number_of_letter():
#     assert functions.no_of_letter('mama') == 4
#     assert functions.no_of_letter('mama.tata') == 8
#     #nie odpowiedzielimsy na ten warunek
import pytest

import functions

# def test_fissbuzz():
#     assert functions.fissbuzz(1) == 1
#     assert functions.fissbuzz(2) == 2
#     assert functions.fissbuzz(3) == 'fiss'
#     assert functions.fissbuzz(4) == 4
#     assert functions.fissbuzz(5) == 'buzz'
#     assert functions.fissbuzz(6) == 'fiss'
#     assert functions.fissbuzz(10) == 'buzz'


@pytest.mark.parametrize('number, result', [(1,1), (3, 'fiss'), (5,'buzz')])
def test_fissbuzz_param(number, result):
    assert test_fissbuzz_advanced(number) == result

def test_fissbuzz_advanced():
    assert functions.fissbuzz(1.3) == 1
    assert functions.fissbuzz(1.9) == 1
    assert functions.fissbuzz('1') == 1
    assert functions.fissbuzz('1.7') == 1
    assert functions.fissbuzz(5.9) == 'buzz'
    assert functions.fissbuzz('5.99') == 'buzz'
    assert functions.fissbuzz(0) == None
    assert functions.fissbuzz(0.999) == None
    assert functions.fissbuzz('mama') == None
    assert functions.fissbuzz('-5') == None
    assert functions.fissbuzz('-15.8') == None
