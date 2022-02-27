from statistics import geometric_mean as gmean
from statistics import median
from statistics import mean

# Iteratively calculate geometric mean, arithmetic mean, and median until convergence
def meandian(a, tol=0.0001, print_rows = True):
    if max(a) - min(a) < tol:
        return median(a)
    else:
        b = [gmean(a), mean(a), median(a)]
        if print_rows:
            print(a)
        return meandian(b, tol, print_rows)

# Given a, a list of lists, calculate the meandian of them all
def msum(a):
    b = []
    for x in a:
        y = meandian(x)
        b += [y]
        print(y)
    return meandian(b)

# For four lists of equal length, compare the values that share the same index.
# Award 3-2-1-0 points from highest to lowest.
def versus(a, b, c, d):
    mySum = [0, 0, 0, 0]
    for y in range(len(a)):
        l = [a[y], b[y], c[y], d[y]]
        z = [sorted(l).index(x) for x in l]
        # print(z)
        for m in range(4):
            mySum[m] += z[m]
    return mySum

# Calculate the results of Voting Valhalla Round 6.
def calculateResults(a):
    # Create the result matrix
    result = []
    for we in range(len(a)):
        result += [[0] * 10]
    # Iterate through all contestants in a
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            rawScore = versus(a[i]["Response0"], a[i]["Response1"], a[j]["Response0"], a[j]["Response1"])

            # Calculate score for i and j separately
            iRaw = [rawScore[0], rawScore[1]]
            iUpper = 1 - (1.0 / 3.0) * (a[i]["Mult"] ** 2)
            iLower = (2.0 / 3.0) * a[i]["Mult"]
            iScore = round(max(iRaw) * iUpper + min(iRaw) * iLower, 5)
            
            jRaw = [rawScore[2], rawScore[3]]
            jUpper = 1 - (1.0 / 3.0) * (a[j]["Mult"] ** 2)
            jLower = (2.0 / 3.0) * a[j]["Mult"]
            jScore = round(max(jRaw) * jUpper + min(jRaw) * jLower, 5)

            # Calculate the differences
            iDiff = round(iScore - jScore, 4)
            jDiff = round(jScore - iScore, 4)
            
            result[i][j] = iDiff
            result[j][i] = jDiff

            # Report the scores
            # print(iUpper, iLower, jUpper, jLower)
            print(a[i]["Name"], "|", iScore, iRaw, "-", a[j]["Name"], "|", jScore, jRaw, "//", iDiff, "/", jDiff)
    # print rows of result matrix
    for k in range(len(result)):
        print(k, result[k])
    return result

