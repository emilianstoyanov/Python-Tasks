# Given an array of integers, determine whether the array is monotonic or not.
def solution(isMonotonic):
    return (all(isMonotonic[i] <= isMonotonic[i + 1] for i in range(len(isMonotonic) - 1)) or
            all(isMonotonic[i] >= isMonotonic[i + 1] for i in range(len(isMonotonic) - 1)))


arr1 = [1, 2, 3, 4, 5]  # True
arr2 = [5, 4, 3, 2, 1]  # True
arr3 = [1, 2, 2, 3, 4]  # True
arr4 = [1, 2, 3, 4, 5, 4]  # False

print(solution(arr1))  # should return True
print(solution(arr2))  # should return True
print(solution(arr3))  # should return True
print(solution(arr4))  # should return False
