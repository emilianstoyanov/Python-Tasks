from collections import defaultdict

words = ["apple", "banana", "carrot", "avocado", "brocoli", "orange"]


grouped_words = defaultdict(list)


for word in words:
    grouped_words[word[0]].append(word)
    
    
    
print(grouped_words)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'brocoli'], 'c': ['carrot'], 'o': ['orange']}