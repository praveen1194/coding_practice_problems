import re

#check if a given string is a palindrome without all non-alphanumeric characters in it
def check_valid_palindrome(s: str) -> bool:
    #remove all non-alphanumeric characters before checking
    s = re.sub(r'[^a-zA-z0-9]', '', s)

    left, right = 0, len(s)-1
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True

input = "a dog! a panic in a pagoda"
print(check_valid_palindrome(input))