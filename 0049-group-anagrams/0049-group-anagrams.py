class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = []
        memo = defaultdict(list)
        for string in strs:
            anagram = "".join(sorted(list(string)))
            memo[anagram].append(string)
        for k in memo:
            ans.append(memo[k])
        return ans