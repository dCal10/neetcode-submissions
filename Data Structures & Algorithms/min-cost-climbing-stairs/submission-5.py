class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    prev, curr = cost[0], cost[1] 
    n = len(cost)
    
    #loop  
    for i in range(2, n):     
        #update prev curr
        prev, curr = curr, min(cost[i] + prev, cost[i] + curr)

    # at the end calculate and return min
    return min(prev, curr)