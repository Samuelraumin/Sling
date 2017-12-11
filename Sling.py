#Welcome to Sling v1.02
#Interactive Fiction
#Created by Sam Raumin and Cody Schieferstine

#Startup and Setup vars
mainlogo = """

                 _____ ___            
                / ___// (_)___  ____ _
                \__ \/ / / __ \/ __ `/
               ___/ / / / / / / /_/ / 
              /____/_/_/_/ /_/\__, /  
                             /____/   
              A Western Story
"""

infopagelogo = """

         ██╗███╗   ██╗███████╗ ██████╗ 
         ██║████╗  ██║██╔════╝██╔═══██╗
         ██║██╔██╗ ██║█████╗  ██║   ██║
         ██║██║╚██╗██║██╔══╝  ██║   ██║
         ██║██║ ╚████║██║     ╚██████╔╝
         ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                    ___ 
                 __|___|__  
                  ('o_o')     D r a w
                  _\~-~/_    ______.  
                 //\__/\ \ ~(_]---' 
                / )O  O( .\/_)  
                \ \    / \_/  
                )/_|  |_\ 
               // /(\/)\ \  
               /_/      \_\ 
              (_||      ||_)  
                \| |__| |/  
                 | |  | | 
                 | |  | | 
                 |_|  |_| 
                 /_\  /_\ 
"""

infopagetext = """
        CREATORS: Sam Raumin and Cody
Interested in contributing or getting in contact?
        Visit our public Github at
    https://github.com/Samuelraumin/Sling
    Type back to go back to the main menu
"""

startinstruct = """
  Type start to begin the game. For more info 
      on the game production and credits
            type info or visit us on
                our Github page
"""

undefinedinput = """
      I do not understand what you said,
    please type one of the options please. 
"""

storyline1 = """
It's 1865, your name is Carson Smith, a simple man. You live on a farm not too far off from the main town, Yorkshire Creek, about twenty miles from Houston in the state of Texas. But today you're partaking in a part time job at a bar in Yorkshire, just a way to make more money for your mother and you. (type c to continue the story)
"""

storyline2 = """
You see a bumbling man sitting at the edge of the bar muttering to himself, saying blurs like "I'll get that addle-headed fool" or "That McDonald took everthing from me". He rose his head and yelled for a drink. What do you do? (Hint: Your job is to make the decision for our character, Carson. Consider your options wisely. For a list of commands, type help)
"""
#help code for the very start to give the total lines of commands, can only be called for at the
#beginning of the game
helplinestart = """
You will be making the decisions for Carson. In this case, you have a couple options:
"""

helpline1 = """
You can walk up to the man (walk), or you can ignore the man and continue with your business (ignore). Make your choice. 
"""

walkuptocon = """
You walk up to the man, frankly annoyed with him, "My apoligizes sir, but I believe you have had enough. The man begins to argue with you, calling you names, but after the man vents, he steps out of the saloon. Soon after the he steps out of the building, you hear a loud thud and some dust kicked though the door. Go help the man (help the man) or ignore (ignore)
"""

ignorecon = """
You ignore the man, figuring that he is just being a drunk idiot. Soon the man became louder though, commanding a drink this time. 
"""

endingA = """
You instead decided to have someone else help the man, you asked a stranger to help the man home. You continue to live your normal life without a worry. 
"""
falseending = """
THIS IS THE END OF THE STORY. But there are others... Restart the game and take a different path.
"""
trueending = """
THIS IS THE TRUE ENDING.
"""
takeconhome = """
You went to the man and decide to help him home. Tapping on him, you tell him, "Hey sir, tell me where you live. I will take you home."
The man compiles with little arguement. You beginning your journey to take the man home. On your way home, the man introduces himself as Bill Conagher. Conagher continues telling you about him being a a Mexican-American war veteran living in the heart of Copper Falls, Texas. In the town, a gang known only as the Copper Fall Riders , which has been causing trouble in the town for as long as Conagher can rememeber. You recognize the name, being the group that has been causing troubles that people in the bar have been taking about for ages. So many people have been ripped off by this gang, and they needed to be stopped. (Type c to continue)
"""
firstmeetup = """
On your way into the town of Copper Falls, you follow the instructions that Conagher gives to his house. As you go, a loud gunshot is heard just across to the next street. Conagher, who was asleep at the time, was awoken by this, and starts yelling, "YOU DIRTY THEIVES. Someone ought to show you some good old butt kicking." You quickly muffle Conagher responses with a blanket you had in the cart and you continue on the house. When you get there, you drop off the still drunk Conagher an leave. On your way back, you notice that a set of three men take the purse of a young women outside of the bank. Do you want to intervene? (Yes or no)
"""

intervene = """
You walk up to the three men and say, "Why don't you pick on someone your own size?". The men turn around, the middle one most likely being the leader, as he was better suited than the other two. The middle man steps forward. "You shouldn't be test the waters around these parts. Go home, kid, before you get yourself into trouble." The man processes to pull out a gun out of his holster, but you back off. Without a word, you turn around and go home. "I'll show them", you say to yourself. (Type c to continue to the next day)
"""
dontintervene = """
You decided not to intervene with the group, but you assume that the middle man was the leader of the Copper Falls gang. As you walk home, you imagine what life would be like without the gang existing in the town anymore. "It would make the town better again, to what it use to be before all the chaos. Carson rememebers his mom talking about how great Copper Falls was before it became overrun with chao. (Type c to continue to the next day)
"""
thenextday = """
The next day, after the long night of returning Conagher, you can't take your mind off of what happened last night. The bar was slow today, and you are just tending to methodically clean the bar, even when no one had sat in the area. All of the sudden, the door bust open, and you are confronted with none other than Conagher himself. He walks up to the bar add starts talking. "Listen kid, that fool Cain McDonald has been tormenting Copper Falls for years and it doesn't seem to be stopping. It's risky right now, but we can get the right equipment and weapons, find another person to help, and have a plan, I believe we can do it." 
"Why are you asking me", you asked concerned. 
"You seem like a tough guy and I need as much help as I can get, again I know it's risky but if it's done, a whole lotta help will come the the town and you can get a good amount of pay on his head. So what says you, you willing to join me?" (yes or no)
"""
notohelpcon = """
You say no to Conagher, and with a sad look on his face, he leaves without word. You finish the shift until the end of the day and go home. When you come home, you are walking up the door step right until you hear someone say, "Please."
You turn around the and you are confronted with Conagher. "Please, you need to help me."
"Why would I help you. You are a drunk maniac!"
"Because you will be bring a lot of good to Copper Falls. Face it, that gang is not going to leave. Someone needs to take this issue into there own hands.  We need to stop them."
You stand and think. You imagine how great Copper Falls would be without those thugs. 
"Fine."
"Prefect, we ride tommorow. I will set everything up in the meantime."
"""

yestohelpcon = """
Ok, We start tommorow. Be ready.
"""
showtimemorning = """
The next morning, you walk out of our house, and Conagher is sitting outside with a wagon. You notice a blanket is covering some equipment in the back of the wagon.
"Let's go." urges Conagher
You hop in the wagon and start on the way. Conagher explains that he knows the gang's leader does a routine path through Copper Falls. He continues that their is a rooftop that is the prefect place to get the shot. He warns that there are always two men on both side of the leader, and that we need to shoot them as well.
You get to the rooftop and set down the blanket full of equipment. You open the cover of the blanket and are confronted with the rifle you will be using. You set up and you are ready to go. (This part of the game is simple, you have a role above a 5 to get the hit. If you role an 8 or higher, you get a hit without the other gang members knowing.) (Type c to shoot)
"""

death = """
 ____  ____                 ______     _               __ 
|_  _||_  _|               |_   _ `.  (_)             |  ]
  \ \  / / .--.   __   _     | | `. \ __  .---.   .--.| | 
   \ \/ // .'`\ \[  | | |    | |  | |[  |/ /__\\/ /'`\' | 
   _|  |_| \__. | | \_/ |,  _| |_.' / | || \__.,| \__/  | 
  |______|'.__.'  '.__.'_/ |______.' [___]'.__.' '.__.;__]
                                                          

"""
deathbygang = """
YOU GOT CAUGHT AFTER MISSING THE SHOT. 


"""

shotbutheard = """
YOU GOT THE SHOT, BUT THEY HEARD YOU.
The gang starts to fire at the rooftop. Bullets are wizzing passed by your ear. You continue to try to make the shots, but the chances of hit have decreased. 
"""

shotbutnotheard = """
YOU GOT THE SHOT, AND THEY DIDN'T HEAR YOU.
Nice shot, they didn't hear you. You proceed to the next person.
"""

chooseformcdon = """
You have the choice to take you chances and kill McDonald, or you can let him live. 
"""

letmcdonlive = """
You understood that killing McDonald would absolutely make to town safe, but you also want to be the higher man and give McDonald a chance in jail. "No, we're not killing him, let'm live" While angered, Conagher accepted your decision, both of you picked up McDonald and tossed him into jail. Days later the county police came over to give you two a handsome reward, Congaher declined the bounty and let you keep it all. A couple of months in McDonald's sentence, he somehow broke out and ran off somewhere. Unfortunately, your dream to McDonald to change his lfe is broken, Congaher utilized this opportunity to hunt him down. You never saw Bill Conagher ever again, you simply continued with your life with a lotta money.
"""

finalending = """
Thinking hard, you realize what Conagher said before, that killing McDonald will make to town a better place, a safer place. "Yeah, finish him off Conagher. I wnat this town safer.""Thanks Carson, it's a real pleasure." snickered Conagher. then a loud bang came. Days after this fight, people started to flow into the town more often, the town also began to have more shops popping up. After the shoot-out, you and Conagher got quiet a handsome reward from the local county police for what you two did, but Conagher let you have all of the money. Apparently after killing McDonald, Conagher was satified with life after gaining redemption.
"""

theend = """
 ______  __                                     __     
/\__  _\/\ \                                   /\ \    
\/_/\ \/\ \ \___      __          __    ___    \_\ \   
   \ \ \ \ \  _ `\  /'__`\      /'__`\/' _ `\  /'_` \  
    \ \ \ \ \ \ \ \/\  __/     /\  __//\ \/\ \/\ \L\ \ 
     \ \_\ \ \_\ \_\ \____\    \ \____\ \_\ \_\ \___,_\
      \/_/  \/_/\/_/\/____/     \/____/\/_/\/_/\/__,_ /
                                                       
"""

#Basic Functions List Start
#For Start Menu GI
def startmenu():
  mainlogoanime()
  print startinstruct
#For info page GI
def infopage():
  print infopagelogo
  print infopagetext
#Function created for options in Start Menu (Intended for Navigation)
def startmenuop():
  startans = raw_input()
  if startans == 'start' or startans == 'Start' or startans == 's' or startans == 'S':
    introgame()
  elif startans == 'info' or startans == 'Info' or startans == 'i' or startans == 'I':
    infopage()
    startmenuop()
  elif startans == 'handsup':
    startmenuop()
  elif startans =='back' or startans == 'Back' or startans == 'b' or startans == 'B':
    startmenu()
    startmenuop()
  elif startans != 'start' or startans != 'Start' or startans != 's' or startans != 'S' or startans != 'info' or startans != 'Info' or startans != 'i' or startans != 'I' or startans !='back' or startans != 'Back' or startans != 'b' or startans != 'B':
    print undefinedinput
    print startinstruct
    startmenuop()
#for logo animation
def mainlogoanime():
  import sys
  from time import sleep
  for char in mainlogo:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()
#Function List End

#Story Functions Start
def introgame():
  storyone()

def storyone():
  print storyline1
  continueans=raw_input()
  if continueans =='C' or continueans == 'c' or continueans == 'continue' or continueans == 'Continue':
    storytwo()
  else:
    print undefinedinput
    storyone()

def storytwo():
  print storyline2
  helpans1()

def storythree():
  print takeconhome
  continueans = raw_input()
  if continueans =='C' or continueans == 'c' or continueans == 'continue' or continueans == 'Continue':
    print firstmeetup
    dec3()
  else:
    print undefinedinput
    storythree()
    
def storyfour():
  print thenextday
  dec4()

def storyfive():
  print showtimemorning
  continueans = raw_input()
  if continueans =='C' or continueans == 'c' or continueans == 'continue' or continueans == 'Continue':
    dicerolegang1()
  elif continueans =='killme':
    storysix() #backdoor, for test purposes
  else:
    print undefinedinput
    storyfive()

def storysix():
  print finalending
  print theend
#Story Functions end

#Game Functions Start
#help for first answer when you meet Conhag  
def helpans1():
  helpans = raw_input()
  if helpans == 'help' or helpans == 'h' or helpans == 'Help' or helpans == 'H':
    print helplinestart
    print helpline1
    dec1()
  else: 
    print undefinedinput
    print helpline1
    dec1()
    
#first command decision made by player
def dec1():
  storytwoans1 = raw_input()
  if storytwoans1 == 'walk' or storytwoans1 == 'Walk' or storytwoans1 == 'w' or storytwoans1 == 'W':
    walk1()
  elif storytwoans1 == 'ignore' or storytwoans1 == 'Ignore' or storytwoans1 == 'i' or storytwoans1 == 'I':
    print ignorecon
    print helpline1
    dec1()
  else:
    print undefinedinput
    dec1()
    
def walk1():
  print walkuptocon
  dec2()

def dec2():
  dec2ans = raw_input()
  if dec2ans == 'help the man' or dec2ans == 'helptheman':
    storythree()
  elif dec2ans == 'ignore' or dec2ans == 'Ignore' or dec2ans == 'i' or dec2ans == 'I':
    print endingA
    print falseending
  else:
    print undefinedinput
    dec2()
    
def dec3():
  interveneans = raw_input()
  if interveneans == 'yes' or interveneans == 'y' or interveneans == 'Yes' or interveneans == 'Y':
    print intervene
    continueans=raw_input()
    if continueans =='C' or continueans == 'c' or continueans == 'continue' or continueans == 'Continue':
        storyfour()
  elif interveneans == 'no' or interveneans == 'n' or interveneans == 'No' or interveneans == 'N':
      print dontintervene
      continueans=raw_input()
      if continueans =='C' or continueans == 'c' or continueans == 'continue' or continueans == 'Continue':
        storyfour()
  else:
      print undefinedinput
      dec3()

def dec4():
  helpconans = raw_input()
  if helpconans == 'yes' or helpconans == 'Yes' or helpconans == 'y' or helpconans == 'Y':
    print yestohelpcon
    storyfive()
  elif helpconans == 'no' or helpconans == 'No' or helpconans == 'n' or helpconans == 'N':
    print notohelpcon
    storyfive()
  else:
    print undefinedinput
    dec4()

def dec5():
  print chooseformcdon
  finalans = raw_input()
  if finalans == 'yes' or finalans == 'Yes' or finalans == 'y' or finalans == 'Y':
    print letmcdonlive
    print theend
  elif finalans == 'No' or finalans == 'no' or finalans == 'N' or finalans == 'n':
    dicerolefinal()
#Game Functions End

#Dice role program Starts
def dicerole():
  import random
  randomnumber = random.randint(1, 10)
  print "           Your random number is: " + str(randomnumber)
#Dice role program Ends

#Shootout Starts

def dicerolegang1():
  import random
  hitguy1 = random.randint(1,10)
  print "You rolled a " + str(hitguy1)
  if hitguy1 <= 5:
    print death
    print deathbygang
  elif hitguy1 > 5 and hitguy1 <=7:
    print shotbutheard
    dicerolegang2heard()
  elif hitguy1 >=8:
    print shotbutnotheard
    dicerolegang2notheard()

def dicerolegang2notheard():
  import random
  hitguy2 = random.randint(1,10)
  print "You rolled a " + str(hitguy2)
  if hitguy2 <= 4:
    print death
    print deathbygang
  elif hitguy2 >=4:
    print shotbutheard
    dec5()

def dicerolegang2heard():
  import random
  hitguy2 = random.randint(1,10)
  print "You rolled a " + str(hitguy2)
  if hitguy2 <= 6:
    print death
    print deathbygang
  elif hitguy2 >= 7:
    print shotbutheard
    dec5()

def dicerolefinal():
  import random
  finalguy = random.randint(1,10)
  print "You rolled a " + str(finalguy)
  if finalguy < 5:
    print death
    print deathbygang
  elif hitguy2 >= 5:
    storysix()
  
#Shootout End

#Beginning of Program Starts Here
#Print Main Logo
startmenu()
#test for dice role function
dicerole()
#menu loop for navigation
startmenuop()
#take in input
