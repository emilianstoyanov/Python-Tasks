def solution(a, target):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == target:
            return mid
        elif a[right] < a[mid]:
            right -= 1
        else:
            left += 1
    return -1


print(solution([1, 5, 10, 15, 30, 50, 60, 70, 75, 80, 100], 75))
# Expected Output: 8
