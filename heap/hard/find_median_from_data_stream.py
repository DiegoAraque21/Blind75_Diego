import heapq

class MedianFinder(object):

    def __init__(self):
        self.small_heap, self.large_heap = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        heapq.heappush(self.small_heap, -1 * num)

        # if the largest number in the small heap belongs
        # to the large heap. Then shift
        if (self.small_heap and self.large_heap and 
            (-1 * self.small_heap[0]) > self.large_heap[0]):
            shift_num = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, shift_num)

        # check if the heaps have equal or similar sizes
        if (len(self.small_heap) > len(self.large_heap) + 1):
            shift_num = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, shift_num)
        if (len(self.large_heap) > len(self.small_heap) + 1):
            shift_num = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -1 * shift_num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        
        # if small heap has more numbers
        if (len(self.small_heap) > len(self.large_heap)):
            return -1 * self.small_heap[0]
        # opposite
        if (len(self.large_heap) > len(self.small_heap)):
            return self.large_heap[0]
        
        # we actually need the mean of the highest in small and lowest in large
        return (-1 * self.small_heap[0] + self.large_heap[0])/2.0