def make_palindrome(s):
    # If the string is already a palindrome, return it
    if s == s[::-1]:
        return s
    
    # Find the longest palindrome suffix
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            # Return the original string + reversed part of the string that's not in the palindrome suffix
            return s + s[:i][::-1]

# Main program
input_string = input().strip()
result = make_palindrome(input_string)
print(result)