class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        #create hashmap of (value, list[inidices])
        values = {}
        for index, num in enumerate(nums):
            if num in values:
                values[num].append(index)
            else:
                values[num] = [index]
        #iterate through i (0, n) and j (i + 1, n)
        for i in range(0, n):

        # if i >0 and == prev continue, asme with j
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range (i + 1, n):
                if j > (i + 1) and nums[j] == nums[j - 1]:
                    continue
                # if sum of ith and jth 's negative in map
                #if last index of found value > j, add tor esult
                summ = nums[i] + nums[j]
                target = -1 * summ
                if target in values and values[target][-1] > j:
                    result.append([nums[i], nums[j], target])
        return result


        


        # return result