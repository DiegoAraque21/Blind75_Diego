class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """

        curr_node = self.root

        for letter in word:
            # check if letter in children so we reuse
            if letter not in  curr_node.children:
                curr_node.children[letter] = TrieNode()

            curr_node = curr_node.children[letter]

        curr_node.end_of_word = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        curr_node = self.root

        for letter in word:

            if letter not in curr_node.children:
                return False
            
            curr_node = curr_node.children[letter]

        return curr_node.end_of_word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        curr_node = self.root

        for letter in prefix:

            if letter not in curr_node.children:
                return False
            
            curr_node = curr_node.children[letter]

        return True

        