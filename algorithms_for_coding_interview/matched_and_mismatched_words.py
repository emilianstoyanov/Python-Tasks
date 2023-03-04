# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.


def solution(arr1, arr2):
    set1 = set(arr1.split(' '))
    set2 = set(arr2.split(' '))

    return sorted(list(set1 ^ set2)), sorted(list(set1 & set2))


sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

print(solution(sentence1, sentence2))

# Output:
# (['The','We','a','are','by','heavy','hit','in','meet','our', 'pleased','storm','to','was','you'],
#  ['city', 'really'])
