import string

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"


def solution(sentence):
    total = 0
    av = ''.join([x for x in sentence if
                  x in string.ascii_letters + '\'- '])  # 'Hi all my name is TomI am originally from Australia'

    for el in av.split(" "):
        total += len(el)

    return round(total / len(av.split(" ")), 2)


# def solution(sentence):
#     for p in "!?',;.":
#         sentence = sentence.replace(p, '')
#     words = sentence.split()  # ['Hi', 'all', 'my', 'name', 'is', 'TomI', 'am', 'originally', 'from', 'Australia']
#     return round(sum(len(word) for word in words) / len(words), 2)


print(solution(sentence1))
print(solution(sentence2))

# Output:
# 4.2
# 4.08
