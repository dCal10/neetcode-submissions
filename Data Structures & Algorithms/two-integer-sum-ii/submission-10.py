class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        #l, r = 0, n - 1 define n
        n = len(numbers)
        l, r = 0, n - 1

        # while l < r
        while l < r:
            
            # check if they add up to target and if so return them
            numL, numR = numbers[l], numbers[r]
            summ = numL + numR

            if summ == target:
                return [l + 1, r + 1]
            elif summ < target:
                l += 1
            else:
                r -= 1

        # return the l and r numbers at end (technically shouldnt get here)
        return [l, r]