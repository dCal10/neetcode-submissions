class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        every = list(zip(position, speed))
        every.sort(reverse = True)

        cycles = []
        for pos, speed in every:
            cycles.append((target - pos) / speed)
        
        fleets = 0
        curr = cycles[0]
        n = len(cycles)
        i = 0
        while i < n:
            while i < n and cycles[i] <= curr:
                i += 1
            fleets += 1
            if i < n: curr = cycles[i]
        return fleets

