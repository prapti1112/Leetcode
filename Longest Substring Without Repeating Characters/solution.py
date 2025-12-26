class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring, longest_sub_len = [], 0
        for ind in range(len(s)):
            if s[ind] in substring:
                cut_ind = substring.index(s[ind]) + 1
                substring = substring[cut_ind:] + [s[ind]]
            else:
                substring.append(s[ind])
            if len(substring) > longest_sub_len:
                longest_sub_len = len(substring)
        
        return longest_sub_len