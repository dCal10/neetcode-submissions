class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqTuples = defaultdict(list) # tuple -> List[int] of indices
        for index, word in enumerate(strs):

            #get frequency counter for each word
            freq = defaultdict(int)
            for char in word:
                freq[char] = freq.get(char,0) + 1
            
            #convert to tuple to hash

            freqTup = tuple(freq[chr(ord('a') + char)] for char in range(26))

        #add to hashmap
            freqTuples[freqTup].append(index)
        #print all out
        output = []
        currIndex = 0

        for group in freqTuples.values():
            output.append([])
            for index in group:
                output[currIndex].append(strs[index])
            currIndex += 1
        
        return output
