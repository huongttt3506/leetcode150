from typing import List
class MajorityElement:
    def majorityElement(self, nums: List[int]) -> int:
        m = dict()
        for n in nums:
            if n not in m: 
                m[n] = 1
            else:
                m[n] += 1
            if m[n] > len(nums)/2:
                return n
        return 0