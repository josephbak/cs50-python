from um import count

def main():
    test_count()

def test_count():
    assert count("um") == 1
    assert count("um, hello, um, world") == 2
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("Um, thanks for the alum") == 1

if __name__ == "__main__":
    main()