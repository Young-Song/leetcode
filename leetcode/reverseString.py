class Solution(obejct):
	def reverseString(self,s):
		"""
		type s: str
		rtype: str

		"""
		len = len(s)
		s = list(s)
		left =0 ; right = len-1
		while left<=right:
			s[left],s[right] = s[right],s[left]
			lef+=1;right-=1
	
		return ''.join(s)


	"""
	extended slicing
	one-line solution:
	def reverseString(self,s):
		return s[::-1]

	"""

