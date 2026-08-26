class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
        
        for i in hash_map:
            if hash_map[i] > n // 2:
                return i
                

         
        