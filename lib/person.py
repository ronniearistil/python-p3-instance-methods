#!/usr/bin/env python3

class Person:
    # Instance method to print "Hello World!"
    def talk(self):
        print("Hello World!")

    # Instance method to print "The person is walking."
    def walk(self):
        print("The person is walking.")

# Test the Person class
if __name__ == "__main__":
    john = Person()
    john.talk()  # Output: Hello World!
    john.walk()  # Output: The person is walking.
