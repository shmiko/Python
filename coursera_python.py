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

#http://www.codeskulptor.org/#user39_wKvI7648Jc8i7cV.py
print "It's a beautiful day."
print "Hello, world."
print 'Hello, world.'
print 7/+4
print 5-1-3-7-0
print (8+(1+(2*4) -3))
#ounces = 0.035274
grams = 0.035274
mass_in_ounces = 28.349 
number123 = mass_in_ounces*2
MYnumber = 5
print MYnumber
print 2/number123
__number__ = 7
print __number__
x = 2
y = 2
y+=x
print x

#1st assignment http://www.codeskulptor.org/#user39_sb9Vw7IFtw_0.py
Hi David

Thank you for your help today, I am sorry that i bug you with such unclear requests, if i knew more about what it is I am doing I could not doubt phrase my questions far more appropriately.

I really do appreciate all the help you have given me and as you probably have guessed I am rather fond of a steep learning curve.

Anyway just thought I would let you know that SCP command worked albeit some strange syntax not normally used within a unix environ. but nonetheless it worked.

Now i thought i would also elaborate ( breifly ) what it is I am doing.

I have a DB service providor who provisions database clusters onto AWS on my behalf Then AWS using an EC2 storage component with a ubuntu server facilitates my SSH connection to then enable normal unix installs and environment setup and configuration.

The scenario is that 4 clusters each having a set of load balancers and database servers with partitioned DB spaces across all nodes, which incidentally have been geographically spread to enable more information about my query explains and from what server is being hit, and from that i can determine latency and in turn rework my queries to increase performance.

As for the sizing I was wrong, when the database is fully restored across all nodes the total capacity in use ( including provisional space for horizontal dynamic scaling ) is in total about 7 TB. Howvever the actual database should it sit in a standalone server would only be around 200GB. So my actual starting json file is 1.7GB, this is the file I will be invoking via my shell script which will cause the actual data import to take place.

Looks like AWS throttle speed going up at around 700kb/s, so pretty slow. Because of the time to process I doubt i will have a working environment to test on before I sit my final exam which is going to start at about 7am tomorrow.

So I am taking a shortcut. I have purposley taken a json dump of a much smaller dataset and will attempt the same thing. Problme might be that in order to maximise the pertition tables they need to be in use, without all the data i might not have the requirement to scale. 

