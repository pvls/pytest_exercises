import pytest
from return_number import *


def test_factorial():
    assert factorial(3) == 6

def test_count_words_occurence_in_string():
    assert count_words_occurence_in_string("try to understand what is happening here ok ok", "ok") == 2