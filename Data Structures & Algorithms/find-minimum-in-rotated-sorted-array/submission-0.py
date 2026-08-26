class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break
            
            m = (left + right) // 2
            res = min(res, nums[m])
            if nums[m] < nums[left]:
                right = m - 1
            else:
                left = m + 1
        return res

        
        