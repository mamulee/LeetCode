class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {')' : '(', '}' : '{', ']' : '['}
        
        for c in s:
            if c in p.values():
                stack.append(c)
            elif c in p.keys():
                if not stack or stack.pop() != p[c]:
                    return False
            else:
                return False

        return not stack

