class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make hashmap
        # if target - num exsists in hashmap return indies
        # add key, index if key doesn't exist already

        vals = {}

        for index, num in enumerate(nums):
            if target - num in vals:
                return [vals[target - num], index]
            vals[num] = index
        return [0,0]
                 