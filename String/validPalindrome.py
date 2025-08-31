import string

def isPalindrome(s):
    if s.isspace():
            return True
    
    # remove spacing between characters
    clean_s = "".join(c.lower() for c in s if c.isalnum())

    return clean_s == clean_s[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
