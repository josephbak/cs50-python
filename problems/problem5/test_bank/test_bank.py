from bank import value

def main():
    test_bank()

def test_bank():
    assert value("Hello") == 0
    assert value("What's up") == 100
    assert value("hi") == 20

if __name__ == "__main__":
    main()