def count_vowels(s):
    counter = 0
    vowels = "aeiouy"
    for char in s:
        if char in vowels:
            counter += 1
    return counter


def main():
    word = input("Type a word: ")
    print(count_vowels(word))


if __name__ == "__main__":
    main()
