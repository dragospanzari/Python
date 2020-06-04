biscuits = 17
if biscuits >= 5:
    print("It's time for tea!")

print("---------------------------------------------------------------------------------------------------------------------")
rainbow = "red, orange, yellow, green, blue, indigo, violet"
warm_colors = "red, yellow, orange"
my_color = "orange"

if my_color in rainbow:
    print("Wow, your color is in the rainbow!")
    if my_color in warm_colors:
        print("Oh, by the way, it's a warm color.")

print("---------------------------------------------------------------------------------------------------------------------")
# Charon the Ferryman carries souls across the river Styx to the world of the dead but does so only for a fee. It's a business after all.
# Check whether the recently deceased has a coin, if any, print Welcome to Charon's boat!
# The variable coin stores a Boolean value, so it qualifies as a condition. If coin has False value, alas! There's nothing to be done about it.
# The variable coin is already defined. So you DON'T need to read its value from the input.
# Lastly, let's warn everyone in the underworld (both those in the boat and those overboard) by printing the message There is no turning back.
coin = bool
if coin:
    print("Welcome to Charon's boat!")
print("There is no turning back.")

print("---------------------------------------------------------------------------------------------------------------------")
# There is a program that should print the maximum value of two numbers, a and b. Put its lines in the right order and add indents to make this program work.
# Rearrange the lines to make the code valid. One horizontal shift corresponds to one indentation level.
maximum =  a
if b > maximum:
    maximum = b
print(maximum)
