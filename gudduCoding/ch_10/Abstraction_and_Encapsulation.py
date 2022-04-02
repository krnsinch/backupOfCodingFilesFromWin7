#  Abstraction:
'''--> Abstraction is the process of hiding the real implementation of an application from the user and  only on usage of it.
 For example, consider you have bought a new electronic gadget. Along with the gadget, you follow instruction you don't matter that 
 how this gadgets works, and also abstraction work in coding Example: . Abstraction has methods.'''
class Remote:
    pass
class player:
    pass
remote1 = Remote()
player1 = player()
if (remote1.isLeftPressed()):     #  HERE WHEN THE USER PLAYED THIS GAME AND USER MOVE THE PLAYER LEFT SO, THE PLAYER MOVED LEFT
# THE USER NEVER INSTRESED IN THAT HOW THE PLAYER MOVE LEFT , so real implement of this application is hide from the user
    player1.moveLeft()     
'''Another example is, when you use TV remote, you do not know how pressing a key in the remote changes the channel internally on the TV.
 You just know that pressing + volume key will increase the volume.'''

# ----------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


#  Encapsulation :
'''--> Encapsulation is a type of capsule that holds the imformation. 
Example:'''

class player:               # ---
    pass                    #    |
    def moveRight(self):    #    |
        pass                #    |--
    def moveLeft(self):     #    |--This is capsule that holds or store the imformation about a player.
        pass                #    |
    def moveRight(self):    #    |
        pass                #----