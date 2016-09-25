class Solution(object):
	def singleNumber(self, nums):
		onceElement = []
		for num in nums:
			if num in onceElement:
				index = onceElement.index(num)
				del onceElement[index]
			else:
				onceElement.append(num)
		return onceElement

solution = Solution()
print solution.singleNumber([1, 2, 3, 4, 5, 1, 3, 2])
		