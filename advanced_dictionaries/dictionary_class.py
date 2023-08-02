from collections import defaultdict


class MyDefaultDict(defaultdict):
    
    def __missing__(self, key):
        self[key] = value = len(key)
        return value
    

t = MyDefaultDict()
print(t["hello"]) # 5
print(t["hi"]) # 2
print(t) # MyDefaultDict(None, {'hello': 5, 'hi': 2})

