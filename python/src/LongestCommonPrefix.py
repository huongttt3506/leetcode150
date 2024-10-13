from typing import List
class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            while s.find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
        return prefix