class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for _ in range(32):
        # take last bit of n
            bit = n & 1
        # shift result left and add bit 
            result = (result << 1) | bit
        
        # shift n right 
            n >>= 1

        return result
    
