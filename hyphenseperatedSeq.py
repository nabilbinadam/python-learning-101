def sort_hyphenated_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

input_str = "green-red-yellow-black-white"
result = sort_hyphenated_words(input_str)
print(result)