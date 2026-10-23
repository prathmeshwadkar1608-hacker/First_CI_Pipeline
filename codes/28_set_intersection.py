"""Program 28: Find the intersection of two sets."""


def set_intersection(first, second):
    return set(first) & set(second)


if __name__ == "__main__":
    first = set(map(int, input(
        "Enter first set numbers: "
    ).split()))
    second = set(map(int, input(
        "Enter second set numbers: "
    ).split()))

    print("Intersection:", set_intersection(first, second))