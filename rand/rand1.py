# RANDOM NUMBERS PROGRAM

# Set up the variables
rand_list = [] # Set up random numbr array
steps = 25 # arbitrary amount of steps here. Will be how many random numbers returned 
seed = 3 # arbitrary seed value. Must be between 1 < seed < 2^31 -1 
int_list = [seed] # Set value for seed array
k = 7**5
m_prime = 2**31 - 1

# Build random numbers in array real_list
for i in range(1,steps + 1):
	int_list.extend([int_list[i-1] % m_prime])
	rand_list.extend([int_list[i]/m_prime])
	print "Random number,", i, "is: ", rand_list
	



	
