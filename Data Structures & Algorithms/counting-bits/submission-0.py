class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i>>1]+(i&1)
        return dp

    

# “Binary count of i = binary count of its parent + last bit”
# Where:
# Parent = i >> 1
# Last bit = i & 1

