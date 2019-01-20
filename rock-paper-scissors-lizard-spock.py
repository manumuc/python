<pre>[cc escaped="true" lang="python"] 
# source: https://www.unixmen.com/rock-paper-scissors-lizard-spock-python/  
#Include 'randrange' function (instead of the whole 'random' module 

from random import randrange 

# Setup a dictionary data structure (working with pairs efficientlyconverter = ['rock':0,'Spock':1,'paper':2,'lizard':3,'scissors':4] 
# retrieve the names (aka key) of the given number (aka value) 

def number_to_name(number): 
   If (number in converter.values()): 
      Return converter.keys()[number] 
   else: 
      print ('Error: There is no "' + str(number) + '"  in ' + str(converter.values()) + '\n') 

# retrieve the number (aka value) of the given names (aka key) 
def name_to_number(name): 
   If (name in converter.keys()): 
      Return converter[name] 
   else: 
      print ('Error: There is no "' + name + '"  in ' + str(converter.keys()) + '\n') 

def rpsls(name): 
 player_number = name_to_number(name) 
 # converts name to player_number using name_to_number 
 comp_number = randrange(0,5) 
 # compute random guess for comp_number using random.randrange() 
 result = (player_number - comp_number) % 5 
 # compute difference of player_number and comp_number modulo five 
# Announce the opponents to each other 
 print 'Player chooses ' + name 
 print 'Computer chooses ' + number_to_name(comp_number) 

# Setup the game's rules 
 win = result == 1 or result == 2 
 lose = result == 3 or result == 4 

# Determine and print the results 
 if win: 
print 'Player wins!\n' 
 elif lose: 
 print 'Computer wins!\n' 
 else: 
 print 'Player and computer tie!\n' 

# Main Program -- Test my code 
 rpsls("rock") 
 rpsls("Spock") 
 rpsls("paper") 
 rpsls("lizard") 
 rpsls("scissors") 

# Check my Helper Function reliability in case of wrong input 
 #number_to_name(6)  
# Error in case of wrong number 
 #name_to_number('Rock')  
# Error in case of wrong name 
 [/cc]</pre> 
