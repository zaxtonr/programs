# RANDOM NUMBERS PROGRAM

print "Enter seed value: " 
seed = raw_input() # arbitrary value. Must be between 1 < seed < 2^31 -1
print "Enter number of wanted random numbers: "
steps = raw_input()

# Set up the variables
rand_list = [] # Set up random number array
int_list = [float(seed)] # Set value for seed array
k = 7**5
m_prime = 2**31 - 1

# Build random numbers in array real_list
for i in range(1,steps + 1):
	int_list.append((k*int_list[i-1]) % m_prime)
	rand_list.append(int_list[i]/m_prime)
	

print "Your random numbers are: ", rand_list
	



	
