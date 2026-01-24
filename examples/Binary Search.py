
# find the smaller number in an array using binary search not just looking through array linearly
# normally u jsut do min(array) but time complexity is O(n)
# so we are trying for time complexity O(log n) which is faster for large arrays

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 2 pointer method left and right pointers
        l, r = 0, len(nums) - 1
        # while left is smaller than right
        while l < r:
            # find the middle index - average of 2 pointer INDEX (not value)
            ## integer division to avoid odd numbers dividing by 2
            m = l + (r - l) // 2
            # check if middle value is less or more than right pointer value
            # array is in order so if its 0 middle and 0,1,2,3 then 0 smaller than 3
            if nums[m] < nums[r]:
                # set new right pointer to middle index
                r = m
            else:
                # if its more than right pointer value
                # aka 3,4,5 - middle is 3 and 5 is BIGGER than 3 now
                # so smallest is on the right side of the array now so move left pointer up to here new start point
                l = m + 1

        # return the smallest value found
        return nums[l]