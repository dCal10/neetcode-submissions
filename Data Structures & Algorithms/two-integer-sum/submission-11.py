class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''info = {}
        for index, num in enumerate(nums):
            if (target - num) in info:
                return [info[target - num], index]
            if num not in info:
                info[num] = index
        return [0, 1]  # placeholder'''
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and i != indices[diff]:
                return [i, indices[diff]]
        return []
