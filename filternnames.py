def filter_names(names):
    return list(filter(lambda name: name.startswith('A'), names))

result = filter_names(["Alice", "Bob", "Anna", "Charlie", "Annie"])
print(result)


