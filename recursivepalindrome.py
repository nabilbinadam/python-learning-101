def is_palindrome(s):
    if len(s) <= 1: #basecase
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

result = is_palindrome("radar")
print(result)