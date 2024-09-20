def merge_sort(string: str):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left_half = merge_sort(string[:mid])
    right_half = merge_sort(string[mid:])
    return merge(left_half, right_half)


def merge(left, right: list):
    sorted_string = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_string.append(left[i])
            i += 1
        else:
            sorted_string.append(right[j])
            j += 1
    while i < len(left):
        sorted_string.append(left[i])
        i += 1
    while j < len(right):
        sorted_string.append(right[j])
        j += 1
    return sorted_string


def is_anagram(first_string, second_string: str):
    first_string = first_string.lower()
    second_string = second_string.lower()

    if not first_string or not second_string:
        sorted_first_string = "".join(merge_sort(first_string))
        sorted_second_string = "".join(merge_sort(second_string))
        return (sorted_first_string, sorted_second_string, False)

    ordered_first_string = merge_sort(first_string)
    ordered_second_string = merge_sort(second_string)
    return (
        "".join(ordered_first_string),
        "".join(ordered_second_string),
        ordered_first_string == ordered_second_string,
    )

    raise NotImplementedError
