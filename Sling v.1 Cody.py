#Welcome to the story of Sling
#Interactive
#Created by Cody Schieferstine and Samuel Ramuin

print "Sling"

print "Type Start to begin the game"
answer=raw_input()

if answer == 'Start' or 'start' : 
  print "It's 1865, your name is Carson Smith, a simple man. You live on a farm not too far off from the main town, Yorkshire Creek, about twenty miles from Houston in the state of Texas. But today you're partaking in a part time job at a bar in Yorkshire, just a way to make more money for your mother and you. (type 'continue' to continue with the story)"
  answer=raw_input()
  
  if answer == 'Continue' or 'continue' : 
  print """You see a bumbling man sitting at the edge of the bar muttering to himself, saying things like 'I'll get that addle-headed fool' or 'That McDonald took everthing from me'. He rose his head and yelled for a drink."""
    answer=raw_pinput()
  
  if answer == 'Approach' or 'approach' or "Go to the man" :
  print "You walk up to the man; frankly annnoyed with him, 'Apoligizes sir, but I believe you've had enough.'"
  
  if answer == 'Begin' or 'begin' :
  print "You see a bumbling man sitting at the edge of the bar muttering to himself, saying things like 'I'll get that addle-headed fool' or 'That McDonald took everthing from me'. He rose his head and yelled for a drink."
  answer=raw_pinput()
  
  if answer == 'Go to the man' or 'Walk to the man' :
  print "You walk up to the man; frankly annnoyed with him, 'Apoligizes sir, but I believe you've had enough.'"
  
  #So I found the issue we were having
  #As it turns out, you do in fact have to state the variable with each or statement being used
  #For example, take if answer == 'Start' or 'start' on line 10
  #this has to be added to make the program consider BOTH options
  #if answer == 'Start' or answer == 'start' :
  
  

