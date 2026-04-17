class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(l:int,r:int)->bool:
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return is_pali(l+1,r) or is_pali(l,r-1)
        return True

        
