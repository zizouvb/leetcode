class Solution:
    def minMeetingRooms(self, intervals):
        times = {}
        for interval in intervals:
            if interval[0] in times:
                times[interval[0]] += 1
            else:
                times[interval[0]] = 1
            if interval[1] in times:
                times[interval[1]] -= 1
            else:
                times[interval[1]] = -1
        current_nb_rooms = 0
        max_room = 0
        for _, value in sorted(times.items(), key=lambda item: item[0]):
            current_nb_rooms += value
            if current_nb_rooms > max_room:
                max_room = current_nb_rooms
        return max_room


print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(Solution().minMeetingRooms([[7, 10], [2, 4], [3, 5]]))
