from pyparsing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sorted_key = "".join(sorted(string))
            if sorted_key in anagrams:
                anagrams[sorted_key].append(string)
            else:
                anagrams[sorted_key] = [ string ]
        
        return list(anagrams.values())