class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:

            if i in count:
                count[i] += 1

            else:
                count[i] = 1

        # count = {1: 1, 2: 2, 3: 3}

        freq = [[] for i in range(len(nums) + 1)] #[ [], [], [], [], [], [], [] ] => chỉ số là số lần xuất hiện, giá trị là bản thân số đó

        for num, c in count.items():
            freq[c].append(num)
        # [ [], [1], [2], [3], [], [], [] ]

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
