class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums :
            freq[num] = freq.get(num,0)+1
        
        sort_num = sorted(freq,key=lambda x : freq[x],reverse=True)

        return sort_num[:k]