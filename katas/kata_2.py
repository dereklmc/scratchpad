import bisect
import unittest

class Chopper(object):
	
	METHODS = ["list_slice", "index_mod", "bisect", "recursive", "recursive_slice"]
	
	def __init__(self, method):
		self.method = self.__getattribute__(method)
	
	def __call__(self, *args):
		return self.method(*args)

	def list_slice(self, target, numbers):
		base_index = 0
		while numbers:
			middle = (len(numbers) - 1)/2
			if target is numbers[middle]:
				return base_index + middle
			elif target < numbers[middle]:
				numbers = numbers[:middle]
			else:
				base_index += middle + 1
				numbers = numbers[middle + 1:]
		return -1
	
	def index_mod(self, target, numbers):
		start = 0
		end = len(numbers) - 1
		while start <= end:
			middle = (start + end)/2
			if target is numbers[middle]:
				return middle
			elif target < numbers[middle]:
				end = middle - 1
			else:
				start = middle + 1
		return -1
	
	def bisect(self, target, numbers):
		result = bisect.bisect(numbers, target) - 1
		if result < 0 or result >= len(numbers):
			return -1
		if numbers[result] is not target:
			return -1
		return result
	
	def recursive(self, target, numbers):
		def recurse(start, end, target, numbers):
			if start > end:
				return -1
			middle = (start + end)/2
			if target is numbers[middle]:
				return middle
			elif target < numbers[middle]:
				return recurse(start, middle-1, target, numbers)
			else:
				return recurse(middle+1, end, target, numbers)
		return recurse(0, len(numbers)-1, target, numbers)
	
	def recursive_slice(self, target, numbers):
		if not numbers:
			return -1
		middle = (len(numbers)-1)/2
		if target is numbers[middle]:
			return middle
		elif target < numbers[middle]:
			return self.recursive_slice(target, numbers[:middle])
		else:
			result = self.recursive_slice(target, numbers[middle+1:])
			if result is not -1:
				result += middle + 1
			return result

class ChopTest(unittest.TestCase):
	
	TESTS = [
			"test_small", 
			"test_sane_middle", 
			"test_sane_large", 
			"test_not_exist_middle", 
			"test_not_exist_middle"
	]
	
	def __init__(self, test_name, chopper):
		super(ChopTest, self).__init__(test_name)
		self.chop = chopper
	
	def setUp(self):
		self.uno = [1]
		self.middle = [1, 3, 5]
		self.large = [1, 3, 5, 7]
		
	def test_small(self):
		self.assertEqual(-1, self.chop(3, []), "Failed Empty List")
		self.assertEqual(-1, self.chop(3, self.uno), "Failed Unary out of bounds")
		self.assertEqual( 0, self.chop(1, self.uno), "Failed Unary")
	
	def test_sane_middle(self):
		self.__sane_test(self.middle, [(1,0), (3,1), (5,2)])
	
	def test_sane_large(self):
		self.__sane_test(self.large, [(1,0), (3,1), (5,2), (7, 3)])
	
	def __sane_test(self, search_space, test_vals):
		msg = "chop({0}) is not {1}"
		for target, expect in test_vals:
			self.assertEqual(expect, 
				self.chop(target, search_space), 
				msg.format(target, expect))
	
	def test_not_exist_middle(self):
		self.__no_exist_test(self.middle, [0,2,4,6])
	
	def test_not_exist_large(self):
		self.__no_exist_test(self.large, [0,2,4,6,8])
		
	def __no_exist_test(self, search_space, targets):
		msg = "Should not have found [{0}] in list."
		for target in targets:
			self.assertEqual(-1, self.chop(target, search_space), msg.format(target))
	
	@classmethod
	def createSuite(cls, chop_method):
		chopper = Chopper(chop_method)
		class ChopSuite(unittest.TestSuite):
			def __init__(self, name):
				self.name = name
				super(ChopSuite, self).__init__()
			
			def run(self, *args):
				print "Test", self.name
				super(ChopSuite, self).run(*args)
		suite = ChopSuite(chop_method)
		for test in cls.TESTS:
			suite.addTest(cls(test, chopper))
		return suite
		
def suite():
	suite = unittest.TestSuite()
	for method in Chopper.METHODS:
		suite.addTest(ChopTest.createSuite(method))
	return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=5).run(suite())
