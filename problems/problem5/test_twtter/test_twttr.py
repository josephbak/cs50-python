from twttr import shorten

def main():
    test_twttr()


def test_twttr():
    # try:
    #     assert shorten("twitter") == "twttr"
    # except AssertionError:
    #     print("the shorten form of twitter is twttr")
    assert shorten("twitter") == "twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("123es") == "123s"
    assert shorten("acE") == "c"

if __name__ == "__main__":
    main()