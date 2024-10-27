#!/usr/bin/env python3

class Dog:
    # Instance method to print "Woof!"
    def bark(self):
        print("Woof!")

    # Instance method to print "The dog is sitting."
    def sit(self):
        print("The dog is sitting.")

# Test the Dog class
if __name__ == "__main__":
    fido = Dog()
    fido.bark()  # Output: Woof!
    fido.sit()   # Output: The dog is sitting.
