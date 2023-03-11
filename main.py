#Remember from parcel (name of script) import Parcel (name of class in script)
from parcel import Parcel

#Main function used to start the process of running the code
def main():
    #create new object called parcel1 from Parcel() class
    parcel1 = Parcel()
    #assigning a bool (true or false) variable called isValid when running is_valid function in Parcel class
    isValid = parcel1.is_valid()
    #printing the returned variable of isValid that was saved
    print(isValid)


#running the main() function which everything is in
main()
