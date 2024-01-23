class DictionaryNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary(object):

    def __init__(self):
        self.root = DictionaryNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """

        curr_node = self.root

        for letter in word:

            if letter not in curr_node.children:
                curr_node.children[letter] = DictionaryNode()
            
            curr_node = curr_node.children[letter]

        curr_node.end_of_word = True


    def search(self, word, node=False):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(start, root):

            curr_node = root

            for i in range(start, len(word)):
                if word[i] == ".":
                    for node in curr_node.children.values():
                        if dfs(i+1, node):
                            return True
                    return False
                else:
                    if word[i] not in curr_node.children:
                        return False
                    curr_node = curr_node.children[word[i]]
            return curr_node.end_of_word
        
        return dfs(0, self.root)