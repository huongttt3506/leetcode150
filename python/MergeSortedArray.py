from typing import List

class MergeSortedArray:
    def __init__(self):
        self.ans = 0

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n -1
        p1 = m -1
        p2 = n - 1

        while p1>= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -=1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    
    def lastSum(self):
        return self.ans

    def add(self, a, b):
        self.ans = a + b
        return self.ans


if __name__ == '__main__':
    sol = Solution()
    print('sum:', sol.add(3,4))
    print("last sum:", sol.lastSum())
    print('sum:%d' % sol.add(3,4))
    print('sum:{}'.format(sol.add(3,4)))
    print(f'sum: {sol.add(3,4)}')
    print(f'sum: {sol.add(3.213123, 4.34534983):.2f}')