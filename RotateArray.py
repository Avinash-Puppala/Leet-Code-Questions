from typing import List
class Solution:
    # def removeDuplicates(nums: List[int]) -> int:
    #     size = len(nums)
    #     index = 1
    #     for i in range(1, size):
    #         if nums[i-1] != nums[i]:
    #             nums[index] = nums[i]
    #             index += 1
    #         print(nums)
    #     return index
                
    # removeDuplicates([1,1,2])

    def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        size = len(nums)
        tempArr = []
        for i in range(0, size):
            tempArr.append(nums[i])
        
        print("size: " + str(size))
        print("initial input: " + str(nums))
        print("\n")

        if k < size:
            for i in range(0, size):
                j = i+k
                if j > size-1:
                    print(i)
                    j = j-(size)
                    print(j)
                    nums[j] = tempArr[i]
                    j = i+k
                    print(nums)
                    print(tempArr)
                    print("\n")
                    continue
                elif j <= size-1:
                    print(i)
                    print(j)
                    nums[j] = tempArr[i]

                print(nums)
                print(tempArr)
                print("\n")
        
            
            

    rotate([1,2,3,4,5,6,7],3)