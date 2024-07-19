import sys

type = sys.argv[1]

if type == ("t2.micro"):
    print ("It charges 2 dollars per day")
elif type == ("t2.medium"): 
    print ("It charges 4 dollar per day")
elif type == ("t2.xlarge"):
    print ("It charges 8 dollar per day")
else:
    print("please provide the valid instance type")