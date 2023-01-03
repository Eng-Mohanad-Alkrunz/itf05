import math


# Function to find mean.
def mean(arr, n):
    sum = 0
    for i in range(0, n):
        sum = sum + arr[i]
    return sum / n


# Function to find covariance.
def covariance(arr1, arr2, n):
    sum = 0
    mean_arr1 = mean(arr1, n)
    mean_arr2 = mean(arr2, n)
    for i in range(0, n):
        sum = (sum + (arr1[i] - mean_arr1) * (arr2[i] - mean_arr2))
    return sum / (n - 1)


# function that returns correlation coefficient.
def correlationCoefficient(X, Y, n) :
    sum_X = 0
    sum_Y = 0
    sum_XY = 0
    squareSum_X = 0
    squareSum_Y = 0


    i = 0
    while i < n :
        # sum of elements of array X.
        sum_X = sum_X + X[i]

        # sum of elements of array Y.
        sum_Y = sum_Y + Y[i]

        # sum of X[i] * Y[i].
        sum_XY = sum_XY + X[i] * Y[i]

# sum of square of array elements.
        squareSum_X = squareSum_X + X[i] * X[i]
        squareSum_Y = squareSum_Y + Y[i] * Y[i]

        i = i + 1

# use formula for calculating correlation
# coefficient.
    corr = (float)(n * sum_XY - sum_X * sum_Y)/(float)(math.sqrt((n * squareSum_X - sum_X * sum_X)* (n * squareSum_Y -sum_Y * sum_Y)))
    return corr
# Driver method


arr1 = [65.21, 64.75, 65.26, 65.76, 65.96]
n = len(arr1)
arr2 = [67.25, 66.39, 66.12, 65.70, 66.64]
m = len(arr2)

if (m == n):
    print(covariance(arr1, arr2, m))
print ('{0:.6f}'.format(correlationCoefficient(arr1, arr2, n)))
