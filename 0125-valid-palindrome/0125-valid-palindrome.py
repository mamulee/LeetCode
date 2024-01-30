class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s.lower() if c.isalnum()])
        l = len(s)
        print(s)
        
        for i in range(l):
            if s[i] != s[l-1-i]:
                return False
        
        return True
        