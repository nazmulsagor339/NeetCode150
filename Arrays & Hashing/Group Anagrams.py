# Problem Link: https://neetcode.io/problems/anagram-groups/question


#Approach 1:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We can use a dictionary to group the anagrams together. 
        # The key of the dictionary will be the sorted version of the word,
        # and the value will be a list of words that are anagrams of each other.
        anagram_dict = {}
        for i in strs:
            sorted_str = ''.join(sorted(i)) # sorting each word
            # If the sorted version of the word is already 
            # a key in the dictionary, we append the original word 
            # to the list of anagrams.
            if sorted_str in anagram_dict: 
                anagram_dict[sorted_str].append(i)
            else:
                anagram_dict[sorted_str] = []
                anagram_dict[sorted_str].append(i)
        # Finally, we return the values of the dictionary, 
        # which are the lists of anagrams.
        anagram_list = [anagram_dict[i] for i in anagram_dict]
        return anagram_list
    

#Approach 2:
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())