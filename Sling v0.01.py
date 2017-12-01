#Welcome to Sling v1.0
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

startinstruct = """
  Type start to begin the game. For more info 
      on the game production and credits
            type info or visit us on
                our Github page
"""

storyline1 = """

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
#Basic Functions List Start
def startmenu():
  print mainlogo
  print startinstruct
def infopage():
  print infopagelogo
  print infopagetext
#Function List End

#Game Functions Start
def rungame():
  print storyline1
#Game Functions End

#Menu Start
print mainlogo

print startinstruct
#take in input
startans = raw_input()

if startans == 'start':
  rungame()
elif startans == 'info':
  infopage()
elif startans == 'handsup':
  minigame()

#Menu End


