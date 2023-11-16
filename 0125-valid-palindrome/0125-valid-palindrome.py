from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for i in range(len(s)):
            asc = ord(s[i])
            if (97 <= asc <= 122) or (65 <= asc <= 90) or (48 <= asc <= 57):
                a=a+s[i].lower()
        new_string = a[::-1]
        if(new_string==a):
            return True
        else: 
            return False