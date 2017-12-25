
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if nums1[0] < nums2[0] :
       return findMedian(nums1, nums2)
    else:
       return findMedian(nums2,nums1)

def findMedian(numsLeft, numsRight):
    totalLenght = len(numsRight) + len(numsLeft)
    isEven = totalLenght % 2
    if isEven == 1:
        midPoint = totalLenght / 2
    else:
        midPoint = (totalLenght / 2) - 1

    print "1) %d %d %d" % (totalLenght, midPoint, isEven)

    leftLen = len(numsLeft) - 1
    index = 0
    if midPoint > leftLen:
        index = midPoint - len(numsLeft)
        firstMedian = numsRight[index]
        secondMedian = numsRight[index + 1]
        print "a) %d %d" % (firstMedian, secondMedian)
    elif midPoint == leftLen:
        firstMedian = numsLeft[-1]
        secondMedian = numsRight[0]
        print "b) %d %d" % (firstMedian, secondMedian)
    else:
        firstMedian = numsLeft[midPoint]
        secondMedian = 0 #numsRight[midPoint+1]
        print "c) %d %d" % (firstMedian, secondMedian)

    median = 0
    if isEven == 0 :
        median = firstMedian
        print "median << %.2f" % median
    else:
        median = (firstMedian+secondMedian)/float(2)
        print "median >> %.2f" % median
    return(median)

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3]
    median = findMedianSortedArrays(nums1, nums2)
    print "%.2f" % median

    nums1 = [1, 2]
    nums2 = [3, 4]
    median = findMedianSortedArrays(nums1, nums2)
    print "%.2f" % median

    nums1 = [1, 2]
    nums2 = [3, 4, 5]
    median = findMedianSortedArrays(nums1, nums2)
    print "%.2f" % median

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8]
    median = findMedianSortedArrays(nums1, nums2)
    print "%.2f" % median
