def edit_distance(str1, str2):

	

	"""
	case 1: the same length 
	case 2: they are not the same length 

	"""

	# if the strings are the same, edit distance = 0
	if str1 == str2:
		return 0 

	# the case if the strings are the same length 
	# ben, hen 
	if len(str1) == len(str2):
		counter = 0
		for idx, ch in enumerate(str1):
			if ch != str2[idx]:
				counter += 1

		return counter

	if len(str1) != len(str2):
		counter = 0 
		# add the difference 
		# i.e. the then -> 4 - 3 =  1

		larger = None
		smaller = None

		if len(str1) > len(str2):
			larger = str1
			smaller = str2
		else:
			larger = str2 
			smaller = str1


		offset = len(larger) - len(smaller)
		counter += offset


		for idx, ch in enumerate(smaller):
			if ch != larger[idx]:
				counter += 1

		return counter


if __name__ == '__main__':
	wd1 = "the"
	wd2 = "hen"
	wd3 = "ben" 
	wd4 = "then"
	wd5 = "again"
	print(f"The distance of '{wd1}' and '{wd1}' is { edit_distance(wd1, wd1)}")
	print(f"The distance of '{wd2}' and '{wd3}' is { edit_distance(wd2, wd3)}")
	print(f"The distance of '{wd1}' and '{wd4}' is { edit_distance(wd1, wd4)}")
	print(f"The distance of '{wd1}' and '{wd4}' is { edit_distance(wd4, wd1)}")
	print(f"The distance of '{wd1}' and '{wd5}' is { edit_distance(wd1, wd5)}")
