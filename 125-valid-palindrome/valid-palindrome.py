class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[i for i in s.lower() if i.isalnum()]
        return l==l[::-1]
    
        