class Solution:
    def longestConsecutive(self, nums):
        #Convert the array into set first 
        numSet = set(nums)
        #initialize to 0, no pattern yet
        longest = 0
        #go through each number in the set 
        for n in numSet:
        #check if the number before is in the set
            if (n-1) not in numSet:
                length = 1

                while (n + length) in numSet:
                    length+=1
                longest = max(length, longest)

        return longest 
