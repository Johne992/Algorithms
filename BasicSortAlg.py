#Python Basic Sorthing Algorithm
#
#Prompt is from ProgrammingPrompts at https://www.reddit.com/r/ProgrammingPrompts/comments/5q80tg/medium_write_a_basic_sorting_algorithm/
# 
#Text:  write a basic sorting algorithm (numbers or letters, however numbers would be a better starting place) which sorts the values 
#        low to high. Must work with varied entry sizes (basically cant rely on your array being 5 in length, and must work while the data is 
#		 even or odd). Bonus points if you can create multiple sorting algorithms, and compare their speeds/efficiencies (consider testing 
#		 them while data is completely sorted and reversed).Have fun!
#
# -- I'm going to limit the length of the randomly generated list to keep this from running extremely long!

from random import randint, sample, shuffle


#Method 1 using a regular Bubble sort
def bubblesort(rlist):
	swaps = 0
	for nextnum in range(len(rlist)-1,0,-1):

		for i in range(nextnum):
		
			if rlist[i] > rlist[i+1]:
				hold = rlist[i]
				rlist[i] = rlist[i+1]
				rlist[i+1] = hold
				swaps = swaps + 1
	return swaps
				

#Method 2 using a Selection sort				
def selectionsort(rlist):
	swaps = 0
	for fill in range(len(rlist)-1,0,-1):
		max = 0
		for loc in range(1, fill+1):
			if rlist[loc]>rlist[max]:
				max = loc
		
		hold = rlist[fill]
		rlist[fill] = rlist[max]
		rlist[max] = hold
		swaps = swaps + 1
	return swaps

#Method 3 Insertion Sort
def insertionsort(rlist):
	swaps = 0
	for index in range(1,len(rlist):
	
		currentvalue = rlist[index]
		pos = index
		
		while pos > 0 and rlist[position-1] > currentvalue:
			rlist[pos] = rlist[pos-1]
			pos = pos - 1
		
		rlist[pos] = currentvalue
		swaps = swaps + 1
	
	return swaps
					
#Method 4 Shell Sort	
def shellsort(rlist):
	swaps = 0
	sublistcount = len(rlist)//2
	while sublistcount > 0:
		
		for startposition in range(sublistcount):
			gapinsertionsort(rlist,startposition,sublistcount)
			swaps = swaps + 1
		
		sublistcount = sublistcount // 2
	return swaps

def gapinsertionsort(rlist, start, gap):
	for i in range(start+gap, len(rlist), gap):
		
		currentvalue = rlist[i]
		position = i
		
		while position >= gap and rlist[position - gap] > currentvalue:
			rlist[position] = rlist[position - gap]
			position = position - gap
			
		rlist[position] = currentvalue

	
	
#Change ints here to make the sample size as large as you want
num1 = randint(-100,100)
num2 = randint(-100,100)
ind = randint(1,25)       
rlist = sample(range(num1,num2), ind)

swaps = bubblesort(rlist)
print("Bubble sort result: ", rlist,"\nNumber of swaps: ", swaps)
shuffle(rlist)

swaps = selectionsort(rlist)
print("Selection Sort result: ", rlist,"\nNumber of swaps:", swaps)
rlist = shuffle(rlist)

swaps = insertionsort(rlist)
print("Insertion Sort result: ", rlist,"\nNumber of Swaps: " , swaps)
rlist = shuffle(rlist)

swaps = shellsort(rlist)
print("Shell Sort result: ", rlist,"\nNumber of Swaps: " , swaps)
rlist = shuffle(rlist)
