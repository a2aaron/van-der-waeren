import pytest
from vdw import *

def test_is_simple_VDW():
    assert is_simple_VDW("r") == True
    assert is_simple_VDW("rbr") == True
    assert is_simple_VDW("rrbbrrbb") == True
    assert is_simple_VDW("") == False
    assert is_simple_VDW("rrr") == False    
    assert is_simple_VDW("rbrbr") == False
    assert is_simple_VDW("rbbrbbr") == False

def test_iter_simple_VDW():
    string = "1234567"
    expected = ["123", "234", "345", "456", "567",
                "135", "246", "357",
                "147"]
    for i, s in enumerate(iter_simple_VDW(string)):
        # Turn the ["1", "2", "3"] into "123" because lazy.
        assert "".join(s) == expected[i]

def test_first_monochrome():
    assert first_monochrome("") == None
    assert first_monochrome("brbbrb") == None
    assert first_monochrome("rrr") == [0, 1, 2]
    assert first_monochrome("rbbrbbr") == [0, 3, 6]

def test_make_simple_vdw():
    assert is_simple_VDW(make_simple_VDW(8, ["r", "b"])) == True
    assert is_simple_VDW(make_simple_VDW(10, ["r", "b", "g"])) == True