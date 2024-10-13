from typing import List
class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        i = 1

        while i < len(nums):
            if nums[i] == nums[i -1]:
                i+=1
            else:
                nums[count] = nums[i]
                i += 1
                count += 1
        return count
