# Problem: check if any permutation of a given string is a palindrome
# ex: civic  = true
#     cciiv  = true
#     aabbcc = true
#     aaabb  = true
#     aaabbb = false
#     abc    = false


# Problem is relatively simple with "any permutation"
# as a palindrome is characters occur an even amount of time
# except one can appear an odd number of time.


class PermutationPalindrome:
    def __init__(self, string):
        self.string = string
        self.lettermap = dict()
   
    def mapletters(self):
        # map the letter and their occurences in a dictionary
        for letter in list(self.string):
            self.lettermap[letter] = self.lettermap.get(letter, 0) + 1

    def checkPalindrome(self):
        # this is my initial approach
        # check that all letters appear an even number of times
        # we can have 1 letter that appear an odd number of time only
        # this method is O = 2n
        self.mapletter()
        maxUnevenLetter = 0
        for key in self.lettermap:
            if self.lettermap[key] % 2 != 0:
                maxUnevenLetter += 1
            if maxUnevenLetter > 1:
                return False
        return True

    def checkPalindromeBetter(self):
        # the better approach is to just check
        # that a character has appeared once before
        # we remove it from the set if it has been already seen as it forms a pair
        # this method is O = n and uses less memory to store the characters that have a pair.
        unpaired_characters = set()

        for letter in self.string:
            if letter in unpaired_characters:
               unpaired_characters.remove(letter)
            else:
               unpaired_characters.add(letter)
        return len(unpaired_characters) <= 1;




myPP = PermutationPalindrome("aabbccddeeeffgg")
print (myPP.checkPalindromeBetter())
                
                
        
