class WordDistance:
    from collections import defaultdict
    def __init__(self, wordsDict: List[str]):
        self.words_dict = wordsDict
        self.loc = defaultdict(list)
        
        for i,word in enumerate(wordsDict):
            self.loc[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc_1,loc_2 = self.loc[word1],self.loc[word2]

        diff = int(1e10)

        upper,bottom = 0,0
        
        while upper < len(loc_1) and bottom < len(loc_2):
            diff = min(diff,abs(loc_1[upper] - loc_2[bottom]))
            if loc_1[upper] < loc_2[bottom]:
                upper += 1
            else:
                bottom += 1
        return diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)