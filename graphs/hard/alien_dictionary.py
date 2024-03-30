class Solution:

    def alienOrder(self, words):
        
        # create the graph with all the letters on the given dictioanry
        graph = {l: set() for word in words for l in word}

        for i in range(len(words) - 1):
            # get the word
            word1, word2 = words[i], words[i+1]

            minLen = min(len(word1), len(word2))

            # bad order, same prefix so the largest word should be word2
            # not word1
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        # path hashmap, False = visited before but not in current
        # traversal ----- True = current path and visited
        path = {}
        result = []

        def dfs(letter):
            # if letter has been visited return true if a cycle is detected
            # if not then return False
            if letter in path:
                return path[letter]
            
            # add to path
            path[letter] = True

            # dfs all it's neighbors
            for neighbor in graph[letter]:
                # if a cycle is detected the return True
                if dfs(neighbor):
                    return True
            
            # complete path has been traversed
            # remove last letter from path and add to result array
            path[letter] = False
            result.append(letter)


        # run the dfs for each letter in the dictionary of the alien language
        for l in graph:
            if dfs(l):
                return True

        # since it's recursive the result array will have 
        # the order of the alphabet reversed. [c, b, a], while in reality 
        # the real order is [a, b, c]. So we reverse the array and
        # transform it to a string.
        result.reverse()
        return "".join(result)



