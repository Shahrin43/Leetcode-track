class Trienode:
    def __init__(self):
        self.children={}
        self.endswith= False

class Trie:

    def __init__(self):
        self.root=Trienode()
        

    def insert(self, word: str) -> None:
        curly= self.root
        for w in word:
            if w not in curly.children:
                curly.children[w]= Trienode()
            curly= curly.children[w]
        curly.endswith= True
        

    def search(self, word: str) -> bool:
        curly=self.root
        for w in word:
            if w not in curly.children:
                return False
            curly=curly.children[w]
        return curly.endswith
        

    def startsWith(self, prefix: str) -> bool:
        curly=self.root
        for w in prefix:
            if w not in curly.children:
                return False
            curly=curly.children[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)