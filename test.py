from collections import defaultdict

dict =["hot","dot","dog","lot","log"]
graph = defaultdict(list)

for word in dict:
    for i in range(len(word)):
        key = word[:i] + "*" + word[i + 1:]
        graph[key].append(word)

print(graph) 
