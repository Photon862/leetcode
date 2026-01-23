
# if its palindrome sentence string return true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #define 2 pointers left and right side
        l, r = 0, len(s) - 1

        # loop while left pointer is less than right pointer
        while l < r:
            # move left pointer to right and checks if its alphanumeric until its = r
            while l < r and not self.alphaNum(s[l]):
                # move 1 step to right
                l += 1

            # move right pointer to left and checks if its alphanumeric until its = l
            while r > l and not self.alphaNum(s[r]):
                #move 1 step to left
                r -= 1

            # now check if the letters are same if all lowercase using lower()
            if s[l].lower() != s[r].lower():
                return False

            # last step is move pointers to middle now to end the loop
            l, r = l + 1, r - 1

        #when loop stops then return true
        return True

    #constraints function to allow only alphabets and letters
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


# nested array of 3 that add up to 0 in the main array

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create empty array to store results
        res = []

        #sorts the nums strig in ascending order
        nums.sort()

        # loop through each number in array
        for i, a in enumerate(nums):

            # if a is bigger than 0 stop loop since no way to add to 0
            if a > 0:
                break

            # skip same element to avoid duplicates in answer
            if i > 0 and a == nums[i - 1]:
                continue

            # define the 2 pointers for each side left and right
            l, r = i + 1, len(nums) - 1

            #while they are at opposite sides
            while l < r:
                # the number chosen at start + 2 pointer numbers
                threeSum = a + nums[l] + nums[r]

                # if the sum is too big move right pointer to left (smaller)
                if threeSum > 0:
                    r -= 1

                # if the sum is too small move left pointer to right (bigger)
                elif threeSum < 0:
                    l += 1

                # else it equals to 0 and append (add) it to res array at the start
                else:
                    res.append([a, nums[l], nums[r]])
                    #cancel loop by adding and removing from l and r each
                    l += 1
                    r -= 1

                    # this 3 set numbers is done so now make sure there is no duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        # show the result array
        return res