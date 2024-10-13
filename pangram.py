# Define the alphabet map
alphabet_map = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user input
user_input = input("Type a sentence: ").lower()

# Remove spaces from the input for accurate comparison
user_input = user_input.replace(" ", "")

# Convert input to a list of characters
input_list = list(user_input)

# Sort both lists to compare them
input_list.sort()
alphabet_map_sorted = sorted(alphabet_map)

# Compare the sorted lists
if input_list == alphabet_map_sorted:
    print("This is an anagram of the alphabet")
else:
    print("Not an anagram of the alphabet")
