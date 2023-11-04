class WordDictionary:
    def __init__(self):
        self.word_dict = {}

    def addWord(self, word: str) -> None:
        if len(word) in self.word_dict:
            self.word_dict[len(word)].append(word)
        else:
            self.word_dict[len(word)] = [word]

    def search(self, word: str) -> bool:
        if len(word) not in self.word_dict:
            return False
        if "." not in word:
            # .이 없으면 그냥 word가 있는지만 확인
            return word in self.word_dict[len(word)]
        for w in self.word_dict[len(word)]:
            # .이 있으면 하나씩 확인
            for i, ch in enumerate(word):
                if ch != w[i] and ch != ".":
                    break
            else:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
