import random

# This function will provide (return) a random capitalized
# letter of the alphabet. Hint: create a letters string
# variable like this one in your main method when you need 
# to check to make sure the entered a capital letter.
def randomletter():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[random.randrange(len(letters))]

def main():
    secretletter = randomletter()
    print("(Shhh! My secret letter is " + secretletter + ")")
    
main()

