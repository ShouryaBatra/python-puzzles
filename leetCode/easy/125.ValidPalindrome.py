import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]', '', s) # removes alphanumeric characters
        s = s.lower()
        return s == s[::-1]