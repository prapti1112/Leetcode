from pyparsing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        indices, p_len = [], len(p)
        for start_index in range(len(s)-p_len+1):
            if sorted(s[ start_index: start_index+p_len ]) == p:
                indices.append(start_index)
        
        return indices