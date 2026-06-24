class Solution:
    def classicBinarySearch(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l <= r:
            m = (l + r) // 2
            curr = nums[m]

            if target == curr:
                return m
            elif target > curr:
                l = m  + 1
            else:
                r = m - 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        #find min first
        n = len(nums)
        l, r  = 0, n - 1
        leftEnd, rightEnd = nums[0], nums[n - 1]
        mini = 0 #placeholder for leftEnd < rightEnd

        #edge case 1 ordered n times
        if leftEnd < rightEnd: mini = 0

        #edge case 2, only 2 items
        if len(nums) == 2:
            a, b = nums
            if target == a: return 0
            elif target == b: return 1
            else: return -1

        #find min

        while l < r and rightEnd < leftEnd: #breaking case at l = r and dont do if already sorted~
            m = l + (r - l) // 2
            curr = nums[m]
            if nums[m - 1] > curr and curr < nums[m + 1]:
                mini = m
                break
            if curr < leftEnd:
                r = m - 1
            else:
                l = m + 1
        mini = l

        #binary search from 0 to mini
        index = self.classicBinarySearch(nums, target, 0, mini) 
        if index != -1: return index
        #mini to n - 1
        return self.classicBinarySearch(nums, target, mini, n - 1) 

      
        

