#Exercise extracted from Crash Courser on Python (Google/Cousera). 
#I just found it interesting and am putting this code here.

'''Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.
'''

def skip_elements(elements):
	# code goes here
	list = []
	for index, element in enumerate(elements):
		if int(index) % 2 == 0:
			list.append(element)
	return list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
