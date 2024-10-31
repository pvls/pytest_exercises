from functions import *
import pytest

operators = Operations()

class TestOperations:
    def test_add(self):
        assert operators.add(2, 3) == 5
        assert operators.add('space', 'ship') == 'spaceship'

    # # uncomment the following test in step 5
    def test_subtract(self):
       assert operators.subtract(2, 3) == -1

    def test_multiply(self):
        assert operators.multiply(2, 3) == 6

    # # uncomment the following test in step 11
    def test_convert_fahrenheit_to_celsius(self):
       assert operators.convert_fahrenheit_to_celsius(32) == 0
       assert operators.convert_fahrenheit_to_celsius(122) == pytest.approx(50)
       with pytest.raises(AssertionError):
           operators.convert_fahrenheit_to_celsius(-600)
           assert False