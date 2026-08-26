class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = defaultdict(int)
        counterT = defaultdict(int)

        for char in s:
            counterS[char] += 1
        for char in t:
            counterT[char] += 1
        return counterS == counterT