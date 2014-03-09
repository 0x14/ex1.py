from time import sleep

print 'Im brewing up. How do you take your coffee?\n'
sleep(2)

print 'How much milk? Input 1 for a little, 2 for lots.\n'
milkinput = raw_input()

#taking what i learned from the modulo program i wrote this from memory
#and then took it to the IDE to try and get it working, only getting the 
#syntax a little wrong, but not having to consult the code from yesterday 
#to fix it. I forgot the two '==' and the ':' on the end and i was putting 
#'then' on the line below the `if` and `elif` (not `else`!) when i only
#needed to define the variable for the action taken/code executed on that
#line below.

if milkinput == '1':
  milk = 'a little'

elif milkinput == '2':
  milk = 'lots of'

sleep(2)

print 'How many tsps sugar?\n'
sugar=int(raw_input())
sleep(2)

print 'How many tsps coffee?\n'
coffee=int(raw_input())
sleep(2)

print 'Several minutes later...\n'
sleep(3)

print 'Heres your coffee, with %s milk, %d tsps sugar, %d tsps coffee.' %(milk, sugar, coffee)
sleep(2)
if coffee>1: print 'Thats a strong coffee!'
sleep(1)
#the rest of the code is pretty much identical, except adding the milk and adding a final timer
#for '5mins later'. The program now flows a little better on the eyes with pauses for input/output
#and new lines formatting the text
