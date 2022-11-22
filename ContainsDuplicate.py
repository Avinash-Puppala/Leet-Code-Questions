from typing import List
class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
        
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    if nums[i] == nums[j]:
                        count += 1
        
        ans = False

        if count > 0:
            ans = True

        print(ans) 

    containsDuplicate([1,2,3,4])

