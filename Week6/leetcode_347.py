from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlogn) Solution
        counts = Counter(nums)
        heap = []
        for num, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                if heap[0][0] < count:
                    heappop(heap)
                    heapq.heappush(heap, (count, num))
        return [heappop(heap)[1] for _ in range(k)]
        # O(n) Solution
        # bucket = [[] for _ in range(len(nums) + 1)]
        # Count = Counter(nums).items()  
        # for num, freq in Count: bucket[freq].append(num) 
        # flat_list = [item for sublist in bucket for item in sublist]
        # return flat_list[::-1][:k]