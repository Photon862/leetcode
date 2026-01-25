
# see if all brackets are properly closed and arranged

class Solution:
    def isValid(self, s: str) -> bool:
        # create an array to keep track of open brackets
        stack = []

        # the matching bracket pairs open and close - in order of close to open
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # loop through each character in the string
        for c in s:
            # look for the characters with closing to find the open to see if theres a match
            if c in closeToOpen:
                # check if the last item in the array is matching with an open bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # this pop function removes the last item in array and returns a the array without last value
                    stack.pop()
                else:
                    #if its not matching open close its false already
                    return False
            else:
                # if there is no closing bracket add open bracket to the stack array
                stack.append(c)

        # if the stack is empty all brackets are matched and removed
        # if stack is not empty at the end return false cause unfinished paris
        return True if not stack else False

