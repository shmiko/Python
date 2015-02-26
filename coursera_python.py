#http://www.codeskulptor.org/#user39_d2CpO8fR0c_0.py 

#This is my first CodeSkulptor Python program!
print 'Hello, world!'
print 3, -1, 3.1234, -2.8
print type(-3.23) #float
print int(3.234), int(-2.8) #3,-2
print float(3), float(0.1) #3.0,0.1
print type(float(3)) #float
print type(int("3")) #int
print type(int(float("30.876"))) #int
print 3.1415926535897890998777 #rounds at 12 3.14159265359
print 1.0 / 3, 5.0 / 2.0 #0.3333333333,2.5
print 1/3,5/2 #0,2
print -9/4 #-3
print 1+2*3,4.0-5.0/6.0,7*8+9*10 # 7,3.166666667,146
print 1+(2*3),4.0-(5.0/6.0),(7*8)+(9*10) # 7,3.166666667,146
#based on "Please Excuse My Dear Aunt Sallie"
#Order of precedence Parenthesis,Exponentiation,
#Multiplication,Division,Addition & Subtraction

# variables - placeholders for important values
# used to avoid recomputing values and to
# give values names that help reader understand code


# valid variable names - consists of letters, numbers, underscore (_)
# starts with letter or underscore
# case sensitive (capitalization matters)

# legal names - ninja, Ninja, n_i_n_j_a
# illegal names - 1337, 1337ninja

# Python convention - multiple words joined by _
# legal names - elite_ninja, leet_ninja, ninja_1337
# illegal name 1337_ninja



# assign to variable name using single equal sign =
# (remember that double equals == is used to test equality)

# examples 

my_name = "Joe Warren"
print my_name

my_age = 51
print my_age

# birthday - add one

my_age += 1
print my_age


# the story of the magic pill

magic_pill = 30
print my_age - magic_pill

my_grand_dad = 74

print my_grand_dad - 2 * magic_pill








#http://www.codeskulptor.org/#user39_XH3jtbGJbo_0.py
# Temperature examples

# convert from Fahrenheit to Celsuis
# c = 5 / 9 * (f - 32)
# use explanatory names

temp_Fahrenheit = 113

temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)

print temp_Celsius

# test it! 32 Fahrenheit is 0 Celsius, 212 Fahrenheit is 100 Celsius


# convert from Celsius to Fahrenheit
# f = 9 / 5 * c + 32

temp_Celsius = 45

temp_Fahrenheit = 9.0 / 5.0 * temp_Celsius + 32

print temp_Fahrenheit


# test it!
x = 2
x+=x+1
print x


