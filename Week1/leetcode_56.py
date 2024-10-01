class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## Thinking Process
        # Sort the list by the start value of each intervals (n log n)
        intervals = sorted(intervals, key=lambda x: x[0])
        answer = []
        # Iterate through each interval (n)
        for i in range(len(intervals) - 1):
        # Check if the next interval's start greater than the current interval's end
        # That means, next interval does not overlap with current interval. Therefore,
            # If True, append the current interval to answer
            # If False, merge the two intervals by updating next interval as:
                # [min of two starts, max of two ends]
            if intervals[i + 1][0] > intervals[i][1]:
                answer.append(intervals[i])
            else:
                intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
        # Append the last interval
        answer.append(intervals[-1])
        return answer