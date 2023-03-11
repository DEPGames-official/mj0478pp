#create class called Parcel which is our object
class Parcel:
    #the function that automatically runs when making a new object
    def __init__(self):
        #list of parameters needed
        self.length = 0
        self.width = 0
        self.height = 0
        self.weight = 0

    #determining if the sizes are valid
    def is_valid(self):
        if self.length > 80:
            return False
        #remember to have a return True or return False in case the condition is invalid
        return True