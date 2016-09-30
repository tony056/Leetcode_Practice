class Solution(object):
	def singleNumber(self, nums):
		returnNum = 0
		for num in nums:
			returnNum = returnNum ^ num
		# find the number to divide into two groups
		firstbit = returnNum & ~(returnNum - 1)
		ans1 = 0 
		ans2 = 0
		for num in nums:
			if firstbit & num == 0:
				ans1 ^= num
			else:
				ans2 ^= num
		return [ans1, ans2]
		# onceElement = []
		# for num in nums:
		# 	if num in onceElement:
		# 		index = onceElement.index(num)
		# 		del onceElement[index]
		# 	else:
		# 		onceElement.append(num)
		# return onceElement

solution = Solution()
print solution.singleNumber([1, 2, 3, 4, 5, 1, 3, 2])
		