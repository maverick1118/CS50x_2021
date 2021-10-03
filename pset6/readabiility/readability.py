from cs50 import get_string


def count_sentence(word):
    s = 0
    for i in range(len(word)):
        c = word[i]
        if c == '!' or c == '.' or c == '?':
            s += 1
    return s


def count_letters(word):
    counter = 0
    for i in range(len(word)):
        c = word.lower()[i]
        if c >= 'a' and c <= 'z':
            counter += 1
    return counter
    

def count_words(word):
    counter = 0
    for i in range(len(word)):
        c = word.lower()[i]
        if c == " ":
            counter += 1
    return counter + 1
    

def main():
    word = get_string("Text: ")
    w = count_words(word)
    l = count_letters(word)
    s = count_sentence(word)

    L = (100 * l) / w
    S = (100 * s) / w

    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
