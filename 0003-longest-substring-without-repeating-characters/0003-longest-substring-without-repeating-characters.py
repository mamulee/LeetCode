class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # to store the last index of each character
        start = 0  # start index of the current substring
        max_length = 0  # maximum length of substring without repeating characters

        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1

            char_index_map[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length