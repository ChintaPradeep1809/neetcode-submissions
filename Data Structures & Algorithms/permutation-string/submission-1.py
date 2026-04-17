class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        if n>m:
            return False
        def idx(c):
            return ord(c)-ord('a')
        count1=[0]*26
        count2=[0]*26

        for i in range(n):
            count1[idx(s1[i])]+=1
            count2[idx(s2[i])]+=1
        
        if count1==count2 :
            return True

        # slide the window
        for i in range(n,m):
            count2[idx(s2[i])]+=1
            count2[idx(s2[i-n])]-=1
            if count1==count2:
                return True
        return False