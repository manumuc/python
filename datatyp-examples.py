

list = ['Booboo', 10, 'Orestis', 5, 'Homer', 7, 'Asterix', 9] 
list...#Output:...['Booboo', 10, 'Orestis', 5, 'Homer', 7, 'Asterix', 9] 

dict = {'Booboo':10, 'Orestis': 5, 'Hommer': 7, 'Asterix': 9} 
dict
#Output:...{'Asterix': 9, 'Hommer': 7, 'Orestis': 5, 'Booboo': 10} 
dict['Hommer']
#Output:...7 
dict.keys()
#Output:...['Asterix', 'Hommer', 'Orestis', 'Booboo'] 
dict.values()
#Output:...[9, 7, 5, 10] 
math.fsum(dict.values()) / len(dict)
#Output:...7.75 

# ------------ 

#!/usr/python 

Import sys
# the sys module helps to handle the user args 

If len(sys.argv) < 3: 
   Sys.exit( '\n' + 'Usage' + sys.argv[0] + ' <num1> <num2> +  '\n') 

num1 = int(sys.argv[1]) 
num2 = int(sys.argv[2]) 
the_sum = num1 + num2 
print  '\n' + str(the_sum) + '\n' 
