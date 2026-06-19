class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) #number to frequency
        for num in nums:
            freq[num] += 1
        ascending = sorted(freq.items(), key = lambda item : (item[1], item[0]), reverse = True)
        return list(ascending[i][0] for i in range(k))