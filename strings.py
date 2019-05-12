for x in range(20):
    t=""
    for y in range(20):
        t+=(chr(30+x+y))
    print(t)


print("symbol of 90:" +chr(256))

testStr = "Hello World!"
# Make it upper case 
print(testStr.upper())
# Make it lower case 
print(testStr.lower())
# Get the length 
print(len(testStr))
# Insert string to another string 
print("*".join(testStr))
# Use join to reverse a string 
print("".join(reversed(testStr)))
# Replace a string 
print(testStr.replace("o", chr(210)))
# Split a string into an array 
print(testStr.split(" "))