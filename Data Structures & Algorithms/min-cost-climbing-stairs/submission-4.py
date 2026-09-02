class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    prev, curr, prevCost, currCost = 0, 0, cost[0], cost[1]  
    n = len(cost)
    if n == 2: return min(prevCost, currCost)
    #loop  
    for i in range(2, n):     
        #update prev curr
        prev, curr = curr, min(prev + prevCost, curr + currCost)
        prevCost, currCost = currCost, cost[i]

    # at the end calculate and return min
    return min(prev + prevCost, curr + currCost)