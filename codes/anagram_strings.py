def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    return sorted(first) == sorted(second)


if __name__ == "__main__":
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")

    if is_anagram(first, second):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")