from time import sleep

print 'Im brewing up. How do you take your coffee?'
sleep(2)

print 'How much milk? Input 1 for a little, 2 for lots.'
milkinput = raw_input()

if milkinput = '1'
  then milk = 'a little'
  
else milkinput = '2'
  then milk = 'lots of'

sleep(2)

print 'How many tsps sugar?'
sugar=int(raw_input())
sleep(2)

print 'How many tsps coffee?'
coffee=int(raw_input())
sleep(2)

print 'Heres your coffee, with %s milk, %d tsps sugar, %d tsps coffee.' %(milk, sugar, coffee)
if coffee>1: print 'Thats a strong coffee!'
