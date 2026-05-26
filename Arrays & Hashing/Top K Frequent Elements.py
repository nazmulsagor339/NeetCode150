# Problem Link: https://neetcode.io/problems/top-k-elements-in-list/question

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create a frequency dictionary to count the occurrences of each number
        frequency_dict = {}

        # Create a list of lists to store numbers based on their frequency
        frequency_list = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number in the input list
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        # Group numbers by their frequency in the frequency_list
        for element, frequency in frequency_dict.items():
            frequency_list[frequency].append(element)

        result = []

        # Iterate through the frequency_list in reverse order 
        # to get the most frequent elements first
        for i in range(len(frequency_list)-1,0,-1):
            for res in frequency_list[i]:
                result.append(res)
                if len(result) == k:
                    return result
        return result