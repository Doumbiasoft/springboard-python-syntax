def print_upper_words(words):
    """For a list of words, print out each word on a separate line, in uppercase"""
    print("fonction print_upper_words\n")
    for word in words:
        print(f"{word.upper()}")
    print("\n")


def print_upper_words_2(words, must_start_with):
    """For a list of words, print out each word on a separate line, in uppercase with the start letter"""
    print(f"fonction print_upper_words_2 => letter start with '{must_start_with}'\n")
    for word in words:
        if word.lower().startswith(must_start_with.lower()):
            print(f"{word.upper()}")
    print("\n")


def print_upper_words_3(words, must_start_with):
    """For a list of words, print out each word on a separate line, in uppercase with the set of start letter"""
    print(f"fonction print_upper_words_3 => letter start with a set of {must_start_with}\n")
    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter.lower()):
                print(f"{word.upper()}")
    print("\n")


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words_2(["hello", "hey", "goodbye", "yo","yes"], must_start_with="y")
print_upper_words_3(["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"h", "y"})
