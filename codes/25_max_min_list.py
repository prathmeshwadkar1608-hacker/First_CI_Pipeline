def find_max_min(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum


if __name__ == "__main__":
    numbers = list(map(int, input("Enter two numbers separated by spaces: ").split()))
    print("Maximum and minimum:", find_max_min(numbers))