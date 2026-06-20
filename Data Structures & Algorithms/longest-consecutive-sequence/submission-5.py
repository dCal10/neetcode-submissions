class Solution:
    def findLongestLength(self, everyNum : List[int]) -> int:
        currLen = 0
        maxLen = 0
        for num in everyNum:
            if num > 0:
                currLen += 1
            else:
                if currLen > maxLen:
                    maxLen = currLen
                currLen = 0
        if currLen > maxLen:
            maxLen = currLen
        return maxLen
                
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        minNum = min(nums)
        maxNum = max(nums)
        everyNum = [0] * (maxNum - minNum + 1) # total of max - min elements
        for num in nums:
            everyNum[num - minNum] += 1
        
        return self.findLongestLength(everyNum)
        