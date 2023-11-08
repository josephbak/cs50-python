from plates import is_valid

def main():
    test_plates()

def test_plate():
    assert is_valid("111111") == False
    assert is_valid("1123") == False
    assert is_valid("cs50") == True
    assert is_valid("1adsdf") == False
    # lengh check
    assert is_valid("asdfghj") == False
    assert is_valid("asd054") == False
    assert is_valid("cs50s") == False
    assert is_valid("AAAAAA") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AA12.") == False

if __name__ == "__main__":
    main()