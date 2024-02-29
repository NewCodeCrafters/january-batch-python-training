# Exercise 1:
# Create a multiline string containing a poem. Print the number of lines in the poem.
poem = "The Poetry Foundation recognizes the power of words to transform lives. We work to amplify poetry and celebrate poets by fostering spaces for all to create, experience, and share poetry."
total = len(poem)
print(f"The total number of character in the poem variable is {total}")
# poem has 186 character values

print(f"the poem contains {total}  character values")

# Define a string variable that contains a mix of uppercase, lowercase, and numeric characters. Convert only the alphabetic characters to uppercase.
variable1 = "DEbugging123"
print(variable1.upper())
variable2 = "DEBUGGING IS FUN"
print(variable2.lower())

variable3 = "DEbugging123 is my mifi password"
print(variable3.title())

# Create two strings containing DNA sequences. Concatenate them and then print the length of the resulting string. Ensure that the DNA sequences are at least 20 characters long.

DNA1 = "blueblood29is" 
DNA2 =  "postive"
DNA3 = DNA1+DNA2
print(f"The length of DNA3 is {len(DNA3)}")

varDNA1= "wdd1344bjjdxcsvxrtrAA+"
varDNA2= "njhju77mn0934nmolAS+"
sumDNA= varDNA1 + varDNA2

print(f"The length of sumDNA is {len(sumDNA)}")
