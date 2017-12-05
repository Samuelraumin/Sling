#Welcome to Sling v1.02
#Interactive Fiction
#Created by Sam Raumin and Cody Schieferstine

#Startup and Setup vars
mainlogo = """\

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
You walk up to the man, frankly annoyed with him, "My apoligizes sir, but I believe you have had enough. The man begins to argue with you, calling you names, but after the man vents, he steps out of the saloon. Soon after the he steps out of the building, you hear a loud thud and some dust kicked though the door. 
        Go help the man (help the man) or ignore (ignore)
"""

ignorecon = """
You ignore the man, figuring that he is just being a drunk idiot. Soon the man became louder though, commanding a drink this time. 
"""
randomnumbertest = """
            Your random number is:
"""

#Basic Functions List Start
#For Start Menu GI
def startmenu():
  print mainlogo
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
#Function List End

#Story Functions Start
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
#Story Functions end

#Game Functions Start
def introgame():
  storyone()
#help for first answer when you meet Conhag  
def helpans1():
  helpans = raw_input()
  if helpans == 'help' or helpans == 'h' or helpans == 'Help' or helpans == 'H':
    print helplinestart
    print helpline1
    dec1()
  else: #helpans != 'help' or helpans != 'h' or helpans != 'Help' or helpans != 'H':
    print undefinedinput
    print helpline1
    helpans1()
    
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
    print "wow"
  elif dec2ans == 'ignore' or dec2ans == 'Ignore' or dec2ans == 'i' or dec2ans == 'I':
    print "ok"
  else:
    print undefinedinput
#Game Functions End

#Dice role program Starts
def dicerole():
  print randomnumbertest
  import random
  randomnumber = random.randint(1, 10)
  print randomnumber


#Dice role program Ends

#Beginning of Program Starts Here
#Print Main Logo
print mainlogo
#Print Start Instructions
print startinstruct

dicerole()

#menu loop for navigation
startmenuop()
#take in input
