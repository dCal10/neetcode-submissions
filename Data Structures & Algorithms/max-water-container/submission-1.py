class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        l, r = 0, n - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            ans = max(ans, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                newL, newR = l, r
                print(f"starting newL: {newL}, newR: {newR}")
                while newL < newR:

                    newL += 1
                    newR -= 1
                    print(f"iterating newL: {newL}, newR: {newR}")
                    if heights[newL] > heights[newR]:
                        l = newL
                        break
                    elif heights[newL] < heights[newR]:
                        r = newR
                        break
                    else:
                        if heights[newL] != heights[l]:
                            l = newL
                            r = newR
                            break
                if newL >= newR:
                    print(f"{newL} {newR} break")
                    break
        
        return ans