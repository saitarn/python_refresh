# str1 = "Hello"
# str2 = "Saitarn"
#
# name = "jojo"
# age = 31
#
# # F String
# print("using F String")
# print(f"{str1} , {str2}")
# print(f"My name is {str2}")
# print("===============")
#
# # .format template
#
# print("By format: My name is {}".format(str2))
# print("This is str1:{}, and str2:{}".format(str1, str2))
#
# print("My name is {}, I'm {}".format(name, age))
# print("My name is {0}, I'm {1}".format(name, age))
# print("I'm {1},My name is {0}".format(name, age))
# print("I'm {fname},My name is {fage}".format(fname=name, fage=age))
# print("===============")
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price=49.1))
#
# print('I designed this rhyme to explain in due time\nAll I know')
# print('Time is a \tvaluable thing')
# print("Watch it fly by\\as the pendulum swings")
# print('It doesn\’t even matter how hard you try')
# print('\a')

print("%30s" % ('geeksforgeeks', ))
print("%35s" % ('geeksforgeeks', ))
print("%-20s" % ('Interngeeks', ))
print("%-25s" % ('Interngeeks', ))
print("%.5s" % ('Interngeeks', ))



match = 12000

site = 'amazon'

print("%s is so useful. I tried to look\
up mobile and they had a nice one that cost %d rupees." % (site, match))


print("This site is {0:f}% securely {1}!!".
	format(100, "encrypted"))

# To limit the precision
print("My average of this {0} was XX.XX% {1:.2f}%"
	.format("semester", 78.234876))

# For no decimal places
print("My average of this {0} was XX% {1:.0f}%"
	.format("semester", 78.234876))

# Convert an integer to its binary or
# with other different converted bases.
print("The {0} of 100 is {1:b}"
	.format("binary", 100))

print("The {0} of 100 is {1:o}"
	.format("octal", 100))


introduction: str = 'My name is {first_name} {middle_name} {last_name} AKA the {aka}.'
full_name = {
	'first_name': 'Tony',
	'middle_name': 'Howard',
	'last_name': 'Stark',
	'aka': 'Iron Man',
}

# Notice the use of "**" operator to unpack the values.
print(introduction.format(**full_name))


# Python code to truncate float
# values to 2 decimal digits.

# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]

# Using format
Output = ['{:.2f}'.format(elem) for elem in Input]

# Print output
print(Output)
print(type(Output))



