class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            hashmap[n] = i
        
        for i,n in enumerate(nums):
            difference = target - n
            if difference in hashmap and hashmap[difference] != i:
                return [i, hashmap[difference]]
        return []