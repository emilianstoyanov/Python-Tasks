def solution(a):  # [-1, 150, 190, 170, -1, -1, 160, 180]
    idx_tree = []  # [-1, 0, 0, 0, -1, -1, 0, 0]
    only_people = []
    result = []
    # checking if they are only trees
    if len([el for el in a if el == -1]) == len(a):
        return a

    # people are zero and trees are -1
    for el in a:
        if el == -1:
            idx_tree.append(-1)
        else:
            only_people.append(el)
            idx_tree.append(0)

    # sorting people by height
    sort_people = sorted(only_people)  # [150, 160, 170, 180, 190]

    # if it is -1 a tree is placed, if it is 0 a person is placed
    for tree in idx_tree:
        if tree == -1:
            result.append(-1)
        else:
            result.append(sort_people[0])
            del sort_people[0]

    return result


print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))
# Expected Output: [-1, 150, 160, 170, -1, -1, 180, 190].


# Input: [-1, -1, -1, -1, -1]
# Expected Output:[-1, -1, -1, -1, -1]


# Input: [-1, -1, -1, -1, -1]
# Expected Output:[-1, -1, -1, -1, -1]


# Input: [4, 2, 9, 11, 2, 16]
# Expected Output: [2, 2, 4, 9, 11, 16]

# Input: [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
# Expected Output: [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
