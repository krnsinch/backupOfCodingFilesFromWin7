class Robot:
    color = "white"         #  This class holds the whole data about what is the color of robot and what is the height or name etc..
    height = "5 ft."
    name = "chitti"

    def walk(self):
        return "I am walking..."
    
    def run(self):
        return "I am running..."
    
    def see(self):
        return "I am seeing.."

    def intro_yourself(self):
        return f"My name is {self.name}"
chitti = Robot()

print(chitti.color)
print(chitti.height)
print(chitti.run())
print(chitti.intro_yourself())
chitti.name = "guddu"
print(chitti.intro_yourself())


# -------------------------------------------------------------------------------------------------------------------



#  Explain oops [objects,class] by railways form and by game:
class RailwayForm:     
    formtype = "RailwayForm"
    def printtheData(self):
        print(f"Name is {gudduApplication.name}")          # also the code {self.name} the result is same.
        print(f"The train  is {gudduApplication.train}")
        print(f"The address is {self.address}")
   
gudduApplication = RailwayForm()   # Make new empty form
gudduApplication.name = "Guddu"    # Take name by variable becauseInside class has some methods and variables.
gudduApplication.train = "Rajdhani Express"  # Train name 
gudduApplication.address = "jodhpur junction"
gudduApplication.printtheData()  

# -----------------------------------------------------------------------------------------------------------------------


#  Game as an example:
class Remote:
    pass
class player:
    pass
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveRight(self):
        pass
remote1 = Remote()
player1 = player()
if (remote1.isLeftPressed()):      # agar remote1 equal hai remote class ke toh agar remote left hau toh player ko left move karo
    player1.moveLeft()         
#    ITS JUST AN EXAMPLE: