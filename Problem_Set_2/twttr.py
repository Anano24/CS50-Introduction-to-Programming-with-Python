
def main():
    # get user input
    answer = input("Input: ")
    # print output
    print(f"Output: {shorten(answer)}")



def shorten(word):
    word_without_vowel = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            word_without_vowel += letter
    return word_without_vowel


if __name__ == "__main__":
    main()