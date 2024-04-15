# Leetcode problem 253: https://leetcode.com/problems/meeting-rooms-ii/description/
# Time: O(NlogN)
# Space: O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))
        # sort time by start time, if startTime == endTime, end comes first
        time.sort(key=lambda interval: (interval[0], interval[1]))

        ongoing_meeting = 0
        counter = 0 

        for _, t in time:
            ongoing_meeting += t
            counter = max(counter, ongoing_meeting)
        
        return counter
