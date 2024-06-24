# CS 9 - Lab 3
# purpose of recursive functions is to keep calling function while making a change. 
def multiply(x, y):
    if x == 1:
        return y # anything multiplied by one is itself (y)
    elif y == 1:
        return x # anything multiplied by one is itself (x)
    elif x == 0 or y == 0: # have to test for all cases. If one variable is 0, expression is equal to 0.
        return 0 
    elif x < y:    # keeps larger value as first term.
        return multiply(y,x)
    else:
        return x + multiply(x, y-1)

def collectMultiples(intList, n):
    if len(intList) == 0:
        return []
    elif intList[0] % n == 0:
        return [intList[0]] + collectMultiples(intList[1:], n)
    else:
        return collectMultiples(intList[1:], n)

def countVowels(s):
    vow = 'AEIOUaeiou'
    if len(s) == 0:
        return 0
    elif s[0] in vow:
        return 1 + countVowels(s[1:])
    else:
        return countVowels(s[1:])

def reverseVowels(s):
    vow = 'AEIOUaeiou'
    if len(s) == 0:
        return ''
    if s[0] in vow:
        return reverseVowels(s[1:]) + s[0]
    else:
        return reverseVowels(s[1:])

def removeSubString(s, sub):  # both s and sub are strings.
    if len(s) < len(sub):  # if what we are removing is greater than starting, we just don't remove anything and return start.
        return s
    elif s[:len(sub)] == sub: # if string from s, starting from the beginning up until length of sub equals sub, then we proceed.
        return removeSubString(s[len(sub):], sub)
    else:
        return s[0] + removeSubString(s[1:], sub)
    