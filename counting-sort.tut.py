
## === accepts all int
def cs_all(arr=[]):
	highest = max(arr)
	lowest = min(arr)

	if highest > 0:
		counter = [0] * (highest + 1)
	else:
		counter = [0]

	if lowest < 0:
		counter_neg = [0] * (abs(lowest) + 1)
	else:
		counter_neg = [0]

	## count the occurence
	for i in arr:
		if i >= 0:
			counter[i] += 1
		else:
			counter_neg[ abs(i) ] += 1

	## current index of the original arr
	curr_index_arr = 0

	## ignore 0 to avoid duplication with +ve
	for i in reversed(range( 1, len(counter_neg) )):
		count = counter_neg[i]
		while count > 0:
			arr[curr_index_arr] = i * -1
			curr_index_arr += 1
			count -= 1

	## go thru each index in counter (+ve)
	for i in range( len(counter) ):
		count = counter[i]
		while count > 0:
			## an i in counter array represents the actual value in arr
			arr[curr_index_arr] = i
			curr_index_arr += 1
			count -= 1
	return arr

arr2 = [4,3,1,-4,3,4,-1,3,4,6,3,7,5,8,5]

# arr2 = [4,3,1,0,3,4,6,3,7,5,8,5]
# arr2 = [4,3,1,3,4,6,3,7,5,8,5]

# arr2 = [-4,-3,-1,0,-4,-3,-4,-1]
# arr2 = [-4,-3,-1,-4,-3,-4,-1]
print(cs_all(arr2))
## === accepts all int




## === only accepts positive int from 0
def cs(arr=[]):
	highest = max(arr)
	# lowest = min(arr)
	counter = [0] * (highest + 1)

	## count the occurence
	for i in arr:
		counter[i] += 1

	## current index of the original arr
	curr_index_arr = 0

	## go thru each index in counter
	for i in range( len(counter) ):
		count = counter[i]
		while count > 0:
			## an i in counter array represents the actual value in arr
			arr[curr_index_arr] = i
			curr_index_arr += 1
			count -= 1
	return arr

arr1 = [4,3,1,4,3,4,3,4,6,3,7,5,8,5]
print(cs(arr1))
## === only accepts positive int from 0