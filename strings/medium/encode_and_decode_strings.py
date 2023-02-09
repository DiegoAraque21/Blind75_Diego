"""

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example:

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        # join all the words. Putting the
        # size of the word and a semicolon as separators at
        # the beginning
        encoded_arr = []
        for str in strs:
            word = f'{len(str)};{str}'
            encoded_arr.append(word)

        return "".join(encoded_arr)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        decoded_str = []
        i = 0

        # i is always goin to be in a number, that reflects the
        # length of that str. If i is not on a number
        # it's because it is out of range
        while i < len(str):
            j = i
            # find the semicolon
            # this while is done to accept double digits
            while str[j] != ";":
                j+=1
            
            # get the length of that str
            # ignore the number sign
            length = int(str[i:j])
            # by using j and the length variable
            # we get the exact word we need
            decoded_str.append(str[j+1:j+1+length])
            # i pointer is in the beginning of the next string
            i = j + 1 + length
        
        print(decoded_str)
        return decoded_str
            


encoded_str = Solution.encode(Solution, ["lint","code","love","you"])
print(encoded_str)
Solution.decode(Solution, encoded_str)