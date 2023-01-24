from typing import List
class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
        
        ans = False
        nums.sort()
        print(nums)
        n = len(nums)
        count = 0
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                ans = True
        
        

        print(ans) 

    containsDuplicate([1,2,3,1])

