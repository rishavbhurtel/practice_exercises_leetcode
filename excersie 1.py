from typing import List
def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    while i < j:
        s[i] , s[j] = s[j] , s[i]
        i += 1
        j -= 1
    print(s)
    
s = ["h","e","l","l","o"]
reverseString(s)