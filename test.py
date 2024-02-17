def get_prefix(words):
    obj = {} 
    for word in words:
        for i in range(len(word)):
            prefix = word[:i + 1]
            if prefix not in obj:
                obj[prefix] = False 
            obj[word] = True 
    return obj

words = ["dog","dad","dgdg","can","again"]
print(get_prefix(words))

board = [
    "doaf",
    "agai",
    "dcan"
    ]
                    
        