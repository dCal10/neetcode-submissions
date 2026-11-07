class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(st: str) -> bool:
            return ('0' <= st and st <= '9') or ('a' <= st.lower() <= 'z')
        #left adn right to 0, n - 1
        n = len(s)
        l, r = 0, n - 1
        
        #while l < r
        while l < r:
            leftStr, rightStr = s[l], s[r]
        #if l not alphanumeric continue
            if not isAlphanumeric(leftStr):
                l += 1
                continue
            if not isAlphanumeric(rightStr):
                r -= 1
                continue 
      
       
            if leftStr.lower() != rightStr.lower():
                return False
            l += 1
            r -= 1


        #in the end return true
        return True