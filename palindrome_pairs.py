class PalindromePairs:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        res = []
        word_to_idx = {word: i for i, word in enumerate(words)}
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                if prefix == prefix[::-1]:
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_to_idx and word_to_idx[reversed_suffix] != i:
                        res.append([word_to_idx[reversed_suffix], i])
                
                if j < len(word) and suffix == suffix[::-1]:
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_to_idx and word_to_idx[reversed_prefix] != i:
                        res.append([i, word_to_idx[reversed_prefix]])
        
        return res

class Solution(PalindromePairs):
    pass
