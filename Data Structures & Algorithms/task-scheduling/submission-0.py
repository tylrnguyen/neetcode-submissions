class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tracker = [0] * 26
        
        # count the frequency in each task
        for i in tasks:
            tracker[ord(i) - ord('A')] += 1

        # see which task occurs the most
        max_freq = max(tracker)

        # count how many tasks have that same highest freq
        max_count = tracker.count(max_freq)

        # (number of gaps - 1) * (n cooldown spots)
        intervals = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), intervals)