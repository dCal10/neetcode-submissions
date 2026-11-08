class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        result = []
        n = len(nums)
        prev = None
        # iterate thru numd, index i
        for i, val in enumerate(nums):
            if prev is not None and val == prev:
                #print(f"{val} skipped")
                continue
            #call two pointers on negative target
            def twoPointers(target):
                #print(f" iteration on {-1 * target}")
                nonlocal result
                #two pointers
                #l, r = i + 1, n - 1
                l, r  = i + 1, n - 1
                while l < r:
                    prevL, prevR = nums[l], nums[r]
                    lVal, rVal = nums[l], nums[r]
                    # do two pointers and update if > or < target
                    if lVal + rVal < target:

                        # keep updating sole l and r until neither out of bounds and not equal to prev
                        l += 1
                        
                        while l < n and nums[l] == prevL:
                            l+= 1
                        #print("less")
                        #print(f"l: {l}")
                    elif lVal + rVal > target:

                        # keep updating sole l and r until neither out of bounds and not equal to prev
                        r -= 1
                        while r > i and nums[r] == prevR:
                             r -= 1
                        #print("more")
                        #print(f"r: {r}")
                    #if target add to result, update both until blh
                    else: 
                        #print("same")
                        result.append([-1 * target, lVal, rVal])
                        #print(f"starting l and r {l} {r}")
                        l += 1
                        #print(f"prevL: {prevL}")
                        while l < n and nums[l] == prevL:
                            
                            l += 1
                            #print(f"l going up {l}")
                        r -= 1
                        while r > i and nums[r] == prevR:
                             r -= 1
                             #print(f"r going dwob {r}")
                        
                        #print(f"l: {l}")
                        #print(f"r: {r}")
            twoPointers(-1 * val)
            #print(f"{val}: {result}")
            prev = val
                
        # return result
        return result