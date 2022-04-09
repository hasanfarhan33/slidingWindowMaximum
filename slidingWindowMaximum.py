import collections

k = 3
nums = [10,32,23,4,-1,7]

def maxSlidingWindow(nums, k):
    q = deque()
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(i)
        if q[0] == i - k:
            q.popleft()
        if i >=k-1:
            res.append(nums[q[0]])
    return res


