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
   Restart the game to get back to the menu
"""

startinstruct = """
  Type start to begin the game. For more info 
      on the game production and credits
            type info or visit us on
                our Github page
"""

storyline1 = """
It's 1865, your name is Carson Smith, a simple man. You live on a farm not too far off from the main town, Yorkshire Creek, about twenty miles from Houston in the state of Texas. But today you're partaking in a part time job at a bar in Yorkshire, just a way to make more money for your mother and you. (type c to continue the story)
"""

storyline2 = """
You see a bumbling man sitting at the edge of the bar muttering to himself, saying blurs like "I'll get that addle-headed fool" or "That McDonald took everthing from me". He rose his head and yelled for a drink. What do you do? (Hint: Your job is to make the decision for our character, Carson. Consider your options wisely.)
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
    rungame()
  elif startans == 'info' or startans == 'Info' or startans == 'i' or startans == 'I':
    infopage()
  elif startans == 'handsup':
    minigame()
  elif startans =='back' or backans == 'Back' or backans == 'b' or backans == 'B':
    startmenuop()
#Function List End

#Game Functions Start
def rungame():
  print storyline1
  continueans=raw_input()
  if continueans =='C' or continueans == 'c' or continueans == 'continue' or continueans == 'Continue':
    print storyline2
#Game Functions End

#Beginning of Program Starts Here
#Print Main Logo
print mainlogo
#Print Start Instructions
print startinstruct

startmenuop()
#take in input
