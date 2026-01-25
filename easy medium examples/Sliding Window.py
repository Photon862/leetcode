
# in an array find combination that 2nd number - first number = biggest value
# first number must be in before 2nd number in order of array list
# question is buy and sell profit in order of days when to buy and sell - each value is 1 day

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set maxprofit to 0
        maxP = 0

        #start with 1st item in array cause its first day to buy
        minBuy = prices[0]

        # loop through price list
        for s in prices:
            # update maxP each time if the profit is bigger
            # max() function returns biggest value
            maxP = max(maxP, s - minBuy)

            # if an array value is smaller than 1st day price change minBuy to that
            # compare 2 values to see if the s or current minBuy value is same
            minBuy = min(minBuy, s)

        #return max profit value
        return maxP


# find longest substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create dictionary to store characters
        mp = {}
        # left pointer of sliding window
        l = 0
        # final result to store the substring length
        res = 0

        # loop through each character in string
        for r in range(len(s)):
            # if the character in the string of index r is in dictionary
            if s[r] in mp:
                # move left pointer to the right with +1 of the dictionary index value
                # max() so it only gets bigger and never smaller - the l is there to compare itself
                l = max(mp[s[r]] + 1, l)
            # add character to dictionary with index value
            mp[s[r]] = r


            res = max(res, r - l + 1)

        #return result number (length of substring)
        return res

