class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        for i in range(len(s)):
            cnt = 1
            if len(s) == 0:
                break
            temp = [s[i]]
            for j in range(i+1, len(s)):
                if s[j] in temp:
                    break
                cnt = cnt + 1
                temp.append(s[j])
            maxl = max(maxl, cnt)
        
        return maxl