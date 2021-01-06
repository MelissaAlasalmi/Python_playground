haystack = "ajkgjlkjiosjifoejojwioejofjowdjowjedf"
haystackList = list(haystack)
length = len(haystackList)
result = []
needles = 0
result.insert(0, haystackList[0])
foundNeedle = 1

#returns a list of all the characters found in a string, in order, without duplicates
while needles < length:
    i = 0
    print("needles: " + str(needles))
    print("current needle in haystack: " + haystackList[needles])
    print("result progress: " + str(result))
    print("foundNeedle: " + str(foundNeedle))
    while i < foundNeedle:
        print("i value: " + str(i))
        print("foundNeedle value: " + str(foundNeedle))
        print("current needle in haystack: " + haystackList[needles])
        print("current needle in result: " + result[i])
        if haystackList[needles] == result[i]:
            i += 1
        else:
            result.insert(foundNeedle, haystackList[needles])
            foundNeedle += 1
        needles += 1
print(result)