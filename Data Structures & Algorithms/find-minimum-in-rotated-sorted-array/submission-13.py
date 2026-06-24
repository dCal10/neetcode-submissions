class Solution:
    def findMin(self, nums: List[int]) -> int:
      n = len(nums)
      l, r = 0, n - 1
      leftmostIndex, rightmostIndex = 0, n - 1
      leftEnd, rightEnd = nums[leftmostIndex], nums[rightmostIndex]  

      #already sorted case
      if rightEnd - leftEnd > 0:
            return leftEnd
      # case of 2
      if len(nums) == 2:
        a,b = nums
        return a if a < b else b

      while l < r:
        m = (l + r) // 2

        if nums[m -1] > nums[m] and nums[m] < nums[m + 1]: return nums[m]
        elif (nums[m] - leftEnd) < 0:
            r = m - 1
        else:
            l = m + 1
      return nums[l]
