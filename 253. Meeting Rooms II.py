# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                heapq.heapreplace(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)