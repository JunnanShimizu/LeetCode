class Trie:

    def __init__(self):
        self.values = []

    def insert(self, word: str) -> None:
        self.values.append(word)

    def search(self, word: str) -> bool:
        return word in self.values

    def startsWith(self, prefix: str) -> bool:
        for s in self.values:
            if s[:len(prefix)] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)