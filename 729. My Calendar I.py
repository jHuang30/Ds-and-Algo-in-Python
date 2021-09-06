# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

# Constraints:

# 0 <= start < end <= 109
# At most 1000 calls will be made to book.

class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        if self.calendar:
            for i in range(0, len(self.calendar)):
                if i == 0 and self.calendar[0][0] >= end or self.calendar[i][0] >= end and self.calendar[i - 1][1] <= start:
                    self.calendar.insert(i, [start, end])
                    return True
                elif i + 1 == len(self.calendar) and self.calendar[i][1] <= start:
                    self.calendar.append([start, end])
                    return True
            else:
                return False
        else:
            self.calendar.append([start, end])
            return True


from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        left_idx = self.calendar.bisect_right(start)
        right_idx = self.calendar.bisect_left(end)
        if left_idx == right_idx and not left_idx % 2:
            self.calendar.add(start)
            self.calendar.add(end)
            return True
        return False

