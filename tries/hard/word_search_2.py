class TrieNode(object):
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def create_word(self, word):
        curr_root = self.root
        for l in word:
            if l not in curr_root.children:
                curr_root.children[l] = TrieNode(l)
            curr_root = curr_root.children[l]
        curr_root.is_word = True

    def prune_word(self, word):
        # list the word
        node = self.root
        par_childkey = []
        for l in word:
            par_childkey.append([node, l])
            node = node.children[l]

        # traverse the lsit in reverse order
        for parent, childkey in reversed(par_childkey):
            target = parent.children[childkey]
            if len(target.children) == 0:
                del parent.children[childkey]
            else:
                return


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
    
        # contains all words that are contained in the board
        result = []
        # create trie and add words
        trie = Trie()
        # create dictionary
        for word in words:
            trie.create_word(word)
        root = trie.root
        # result and path set
        res, path = set(), set()

        # baord dimensions
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, word):
            # check if doesn't exist
            # r out of bounds, or already in path
            # we didn't find anything
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] not in node.children or (r,c) in path):
                return
            
            # add to path and change word
            path.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            # if we found a word add it to the result
            if node.is_word:
                res.add(word)
                node.is_word = False
                trie.prune_word(word)

            # boundaries for recursive step
            boundaries = [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]
            for bound in boundaries:
                dfs(bound[0], bound[1], node, word)
            
            # cleanup the path
            path.remove((r,c))

        # brute force to check every cell
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root, "")
        
        return res