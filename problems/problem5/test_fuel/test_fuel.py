from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("4/100") == 4
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(5) == "5%"


if __name__ == "__main__":
    main()
