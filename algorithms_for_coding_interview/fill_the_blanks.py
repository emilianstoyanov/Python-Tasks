# Given an array containing None values fill in the None values with most recent
# non None value in the array


def solution(arr):
    state = 0
    save = []
    for el in arr:

        if el is not None:
            save.append(el)
            state = el
        else:
            save.append(state)
    return save


array1 = [1, None, 2, 3, None, None, 5, None]
print(solution(array1))

# Output: [1, 1, 2, 3, 3, 3, 5, 5]
