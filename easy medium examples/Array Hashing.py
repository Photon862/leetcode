
# finding duplicate numbers in array

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True

#lens - returns length of array
#set - puts array in set with no duplicates

# finding if 2 strings are anagrams (same letters rearranged)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #quick check first if length is same to save time
        if len(s) != len(t):
            return False

        # defines 2 dictionaries
        countS = {}
        countT = {}

        # loop length of s number of times and for each item in the string,
        # add 1 on for that letter
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #if the letters in each dictionary have the same score then return true
        return countS == countT

# finding 2 numbers that add up to target and output which numbers they are the index in array
# two pointer problem similiar

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create dictionary to store previous numbers
        prevMap = {}  # val -> index

        # loop through nums - enumerate gives index and number unlike len is just length
        for i, n in enumerate(nums):
            # find difference between target and current number
            diff = target - n

            # if the diff is in dictionary, for eg u need +2 left, if 2 is there then add 2 so done
            if diff in prevMap:
                # give the number that was found to hit target and return answer
                return [prevMap[diff], i]

            # if its not there, put it in dictionary for next loop to find and check
            prevMap[n] = i

# a list of words group them into anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # creates a defaultdict - imported cause defaultdict if there is no key it creates new one
        res = defaultdict(list)

        # loop through each string in the array
        for s in strs:
            #create a count of 26 for each letter in alphabet
            count = [0] * 26

            # for each character in string, add 1 to that letter in count
            # now a is 97 b is 98 so if u -a from it its a=0, b=1..etc easier to index
            for c in s:
                count[ord(c) - ord('a')] += 1

            # tuple converts immutable list to mutable so it can be put in the dictionary as a key
            # now append adds all the words in the count tuple format to the dictionary
            res[tuple(count)].append(s)

        # res.values() only returns value of dictionary not keys - cuts out the numbers of "count" var
        return list(res.values())

