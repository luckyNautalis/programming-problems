import heapq


class Solution:

    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        heap = []
        for index in range(len(nums)):
            heapq.heappush(heap, [nums[index], index])

        for i in range(k):
            replacement, index = heap[0]
            replacement *= multiplier
            heapq.heapreplace(heap, [replacement, index])
            nums[index] *= multiplier


s = Solution()
s.getFinalState([1, 2], 2, 2)
