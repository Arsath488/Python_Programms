class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Sort the strings lexicographically
        strs.sort()
        
        # Compare the first and the last string
        first = strs[0]
        last = strs[-1]
        i = 0
        
        # Only iterate up to the length of the shorter string
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]
