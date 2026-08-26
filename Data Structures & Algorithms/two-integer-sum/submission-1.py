class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_Map = {}
        for i, n in enumerate(nums):
            hash_Map[n] = i
        
        for i,n in enumerate(nums):
            difference = target - n
            if difference in hash_Map and hash_Map[difference] != i:
                return [i, hash_Map[difference]]
        return []

        