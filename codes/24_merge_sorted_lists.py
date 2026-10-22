def merge_sorted_lists(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i = i + 1
        else:
            result.append(list2[j])
            j = j + 1

    while i < len(list1):
        result.append(list1[i])
        i = i + 1

    while j < len(list2):
        result.append(list2[j])
        j = j + 1

    return result


if __name__ == "__main__":
    list1 = list(map(int, input("Enter first sorted list: ").split()))
    list2 = list(map(int, input("Enter second sorted list: ").split()))

    print("Merged list:", merge_sorted_lists(list1, list2))