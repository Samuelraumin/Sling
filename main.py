#Welcome to the story of Sling
#Interactive
#Created by Cody Schieferstine and Samuel Ramuin

def introduction():
  print "Sling"
  startup()

def startup():
  print "Type Start to begin the game"
  answer=raw_input()
  
  if answer == 'Start' or answer== 'start' : 
    print """It's 1865, your name is Carson Smith, a simple man. You live on a farm not too far off from the main town, Yorkshire Creek, about twenty miles from Houston in the state of Texas. But today you're partaking in a part time job at a bar in Yorkshire Creek, just a way to make more money for your mother and you. (type 'continue' to continue with the story)"""
    firstcomment()

def firstcomment():
  answer=raw_input()
  if answer == 'Continue' or answer == 'continue' or answer == 'C' or answer == 'c' : 
    print """You see a bumbling man sitting at the edge of the bar muttering to himself, saying things like 'I'll get that addle-headed fool' or 'That McDonald took everthing from me'. He rose his head and yelled for a drink."""
    decision1()
    
      

def decision1():
  answer=raw_input()
  if answer == 'Approach' or answer == 'approach' or answer == 'Go to the man' or answer == 'Walk to the man' or answer == 'walk' or answer == 'Walk':
    print """You walk up to the man; frankly annnoyed with him, 'Apoligizes sir, but I believe you've had enough.'"""
    firstresponse()
    
  elif answer == 'Ignore' or answer == 'ignore':
    print """You ignore the man, figuring he's being a drunk idiot. Soon the man became louder though, commanding a drink this time."""
    firstresponse()
    
  
def firstresponse():
  print """The man began to argue with you, calling you names, cursing at you, but after the man vented himself out, he stepped out of the saloon. (type 'c' to continue)"""
  narrative2()

def narrative2():
  answer=raw_input()
  if answer == 'C' or answer == 'c' or answer == 'Continue' or answer == 'continue':
    print """Soon after he stepped out of the building, you heard a loud thud and some dust kicked in through the door. (type 'c' to continue)"""
  decision2()

def walktonoise():
  answer=raw_input()
  if answer == 'Walk' or answer == 'walk' or answer == 'Approach' or answer == 'approach':
    print """You decided to walk to noise. When you stepped out to see what made the noise, you find the man drunk on the ground both moaning and sighing."""
    
  decision2()
  
def decision2():
  answer=raw_input()
  if answer == 'Help' or answer == 'help' or answer == 'Help the man' or answer == 'help the man':
    print """You went to the man and decide to help him home.Tapping on him you tell him, 'Hey sir, tell me where you live. I'll help you home. (type 'c' to continue)'"""
    narrative3()

  elif answer == 'Ignore' or answer == 'ignore' or answer == 'Ask for help' or answer == 'ask for help':
    print """You instead decide to have someone else help the man, you asked a stranger to help the man home. You continue to live your normal life without a worry. THIS IS THE END OF THE STORY"""
    
def narrative3():
  answer=raw_input()
  if answer == 'C' or answer == 'c' or answer == 'Continue' or answer == 'continue':
    print """The man accepts the offer without objection, you pick him up and bring him home. On the way the man introduces himself as Bill Conagher, a Mexican-American war veteran who lives in Copper Falls, Texas. Conager added that a gang is in the town of Copper Falls, known simply as the Copper Fall gang, their leader is Cain McDonald; that man killed Conahger's wife a couple of years ago and the gang still torments the town since. Conagher finished off stating that the gang needed to be stopped at all costs. (type 'c' to continue)"""
    narrative4()
def narrative4():
  answer=raw_input()
  if answer == 'C' or answer == 'c' or answer == 'Continue' or answer == 'continue':
    print """When you reached Conagher's home to drop him off, you hear a gunshot go off around 200 yards away. Congaher commented, 'That's probably the Copper Falls gang, took care of another person by the sounds of it. I suggest you avoid those boys at all costs right now, we don't have the equipment yet.'"""
  decision3
    
    
def decision3():
  answer=raw_input()
  if answer == "Avoid the gang" or answer == 'avoid the gang' or answer == 'Avoid' or answer == 'avoid' or answer == 'Ignore' or answer == 'ignore' or answer == 'Ignore the gang' or answer == 'ignore the gang':
    print """You listen to Congaher's advice and chose to avoid the gang, before you left Congaher said he wants the two of them to talk a little bit more tommorrow.(type 'c' to continue the story)"""  
    
  elif answer == 'Confront the gang' or answer == 'confront the gang' or answer == 'fight the gang' or answer == 'Fight the gang' or answer == 'fight' or answer == 'Fight':
    print """You got Congaher to his home and you build up the courage to confront the gang. Walking over there, Congaher commands you stop and come back, but you ignore and continue on. As you come up to the group of men, you spot a dead man sprawled on the ground with the red hole in the center of his back. 'Hey you reckon your little gang should step off this place, you have no right to oppress others.' you exclaim puffing up your chest. The man in the middle wearing a black hat chuckled and responded, 'I don't think so kid, you try to tell me off, thats a real consequnce.' The man then lifted up his revolver and shot you straight in the chest, you fell on the ground clenching your chest, soon your vision became fuzzy and black outright, you unfornutely have died. THIS IS THE END OF THE STORY"""
    
    
def narrative4():
  answer=raw_input()
  if answer == 'Continue' or answer == 'continue' or answer == 'C' or answer == 'c':
  print """In the next morning, you found Congaher walking into the saloon. He came up to you and sat down, he started off by saying,'Listen kid, that fool Cain McDonald has been tormenting Copper Falls for years and it does seem to be stopping. It's risky right now, but we can get the right equipment and weapons, find another person to help, and have a plan, I believe we can do it.''Why'd you go to me first?'  you asked concerned. 'You seem like a tough guy and I need as much help as I can get, again I know it's risky but if it's done, a whole lotta help will come the the town and you can get a good amount of pay on his head. So what says you, you willing to join me?'"""
 
    
def decision4():
  answer=raw_input()
  if answer == 'Join' or answer == 'join' or answer == 'Join Conagher' or answer == 'join Conagher' or answer == 'join conagher'
  print 
    
  
  
  


  
introduction()
  
  
  
  

