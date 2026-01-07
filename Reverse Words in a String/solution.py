class Solution:
    def reverseWords(self, s: str) -> str:
        s =  [ word for word in s.strip().split() if word not in [" ", ""]][::-1]
        return " ".join(s)