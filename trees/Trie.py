# trie for words
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root

        for l in word:
            pos = ord(l) - ord('a')
            if curr.children[pos] == None:
                curr.children[pos] = TrieNode()
            curr = curr.children[pos]

        curr.end_of_word = True

    def print_words(self):
        res = []
        self.dfs(self.root,res)
    
    def dfs(self,root,res):
        if root == None:
            return

        if root.end_word_word == True:
            print(''.join(res))

        for i,c in enumerate(root.children):
            if c != None:
                res.append(chr(i+ord('a')))
                self.dfs(c,res)
                res.pop()
                
