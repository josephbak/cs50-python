from seasons import convert, number_to_words

def main():
    test_convert()
    test_number_to_words

def test_convert():
    assert convert("2022-11-08") == 525600

def test_number_to_words():
    assert number_to_words(525600) == "five hundred twenty-five thousand, six hundred minutes"

if __name__ == "__main__":
    main()