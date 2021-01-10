haystack = "ajkgjlkjiosjifoejojwioejofjowdjowjedf"
haystackList = list(haystack)
length = len(haystackList)
result = []
needles = -1
result.insert(0, haystackList[0])
foundNeedle = 1

#returns a list of all the characters found in a string, in order, without duplicates
while needles < (length - 1):
    i = 0
    needles += 1
    while i < foundNeedle:
        if haystackList[needles] == result[i]:
            i = foundNeedle
        else:
            i += 1
            if i == foundNeedle:
                result.insert(foundNeedle, haystackList[needles])
                foundNeedle += 1
print(result)