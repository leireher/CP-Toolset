# LIS
# in O(n Log n) time.
# Binary search
def GetCeilIndex(arr, T, l, r, key):
    while (r - l > 1):
        m = l + (r - l)//2
        if (arr[T[m]] >= key):
            r = m
        else:
            l = m
    return r
  
def LongestIncreasingSubsequence(arr, n):
    # Add boundary case,
    # when array n is zero
    # Depend on smart pointers
    # Initialized with 0
    tailIndices =[0 for i in range(n + 1)] 
    # Initialized with -1
    prevIndices =[-1 for i in range(n + 1)] 
    # it will always point
    # to empty location
    len = 1
    for i in range(1, n):
        if (arr[i] < arr[tailIndices[0]]):
            # new smallest value
            tailIndices[0] = i
        elif (arr[i] > arr[tailIndices[len-1]]):
            # arr[i] wants to extend
            # largest subsequence
            prevIndices[i] = tailIndices[len-1]
            tailIndices[len] = i
            len += 1
        else:
            # arr[i] wants to be a
            # potential condidate of
            # future subsequence
            # It will replace ceil
            # value in tailIndices
            pos = GetCeilIndex(arr, tailIndices, -1,len-1, arr[i])
            prevIndices[i] = tailIndices[pos-1]
            tailIndices[pos] = i
    i = tailIndices[len-1]
    res = []
    while(i >= 0):
        res.append(arr[i])
        i = prevIndices[i]
    res.reverse()
    return len, res
