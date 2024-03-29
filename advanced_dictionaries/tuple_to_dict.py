from collections import defaultdict

tuple_list = [("A", 10), ("B", 4), ("A", 5), ("B", 1), ("C", 7)]

grouped_data = defaultdict(list)

for key, value in tuple_list:
    grouped_data[key].append(value)
    
    
print(grouped_data) # {'A': [10, 5], 'B': [4, 1], 'C': [7]}

grouped_data = {k: sum(v) for k, v in grouped_data.items()}

print(grouped_data) # {'A': 15, 'B': 5, 'C': 7}
