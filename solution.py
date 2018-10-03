import sys

###############################
#  Synonyms Dictionary Class  #
###############################
class SynsDict:
	dic = {}
	
	@classmethod
	def addSynm(cls, lst):
		"""
		lst: array of synonyms
		rtype: void
		"""
		for word in lst:
			temp = lst[:]
			temp.remove(word)

			if word not in cls.dic:
				cls.dic[word] = temp

			else:
				# if the word is already in the dict
				# expand the synonyms
				for syn in temp:
					cls.dic[word].append(syn)

	@classmethod
	def isSynm(cls, word1, word2):
		"""
		rtype: bool
		"""
		if word1 not in cls.dic:
			return False
		
		if word2 not in cls.dic:
			return False

		syns = cls.dic[word1]

		return word2 in syns



#################
#  NTuple Class #
#################
class NTuple:
	def __init__(self, synsDict, size=3):
		"""
		synsDic: SynsDict, Dictionary of synonyms
		size: int, Tuple size
		"""
		self.synsDict = synsDict
		self.size = size
		self.count = 0
		self.similar = 0

	def nTuple(self, line1, line2):
		"""
		Sliding Window Technique

		rtype: bool
		"""
		# assumption: 
		#	- len(line1) == len(line2)
		#	- len(line1) >= self.size, if not throw error

		size = self.size

		if size > len(line1):
			raise SizeError("Tuple size > length of a line")

		for i in range(len(line1)-size+1):
			tup1 = line1[i:i+size]
			tup2 = line2[i:i+size]
			bool = self.tupleComp(tup1, tup2)
			self.count += 1

			if bool is True:
				self.similar += 1

	def tupleComp(self, tup1, tup2):
		"""
		Comparator

		rtype: bool
		"""
		for i in range(len(tup1)):
			if tup1[i] != tup2[i]:
				if not self.synsDict.isSynm(tup1[i], tup2[i]):
					return False 

		return True

	def result(self):
		"""
		Return the result

		rtype: string
		"""
		return str((self.similar/float(self.count) * 100)) + "%"



##################
#  Custom Error  #
##################
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class SizeError(Error):
	"""
	Tuple Size > length of a line
	"""
	def __init__(self, msg):
		self.msg = msg



#####################
#  Helper Function  #
#####################
def stringToLst(string):
	return string.split(" ")


if __name__ == '__main__':
	if len(sys.argv) != 4 and len(sys.argv) != 5:
		print "Usage:\n1. file name for a list of synonyms\n2. input file 1\n3. input file 2\n4. (optional) the tuple size\n"
		exit()


	synonyms = sys.argv[1]
	file1 = sys.argv[2]
	file2 = sys.argv[3]

	tup_size = 3 #default value
	if len(sys.argv) == 5:
		tup_size = int(sys.argv[4])

	try:
		syns_contents = open(synonyms, "r").read()
		syns_contents = syns_contents.split("\n")

		file1_contents = open(file1, 'r').read()
		file1_contents = file1_contents.split("\n")

		file2_contents = open(file2, 'r').read()
		file2_contents = file2_contents.split("\n")

		# Add to synsDict
		synsDict = SynsDict()
		for syns in syns_contents:
			if syns != "":
				synsDict.addSynm(stringToLst(syns))

		solution = NTuple(synsDict, tup_size)

		# Compare each line
		for ind in range(len(file1_contents)):
			if file1_contents[ind] != "" and file2_contents[ind] != "":
				line1 = stringToLst(file1_contents[ind])
				line2 = stringToLst(file2_contents[ind])
				solution.nTuple(line1, line2)

		print solution.result()
	
	except IOError as e:
		print "IOError: " + str(e)

	except SizeError as e:
		print "SizeError: " + e.msg


	


