# Takes an email address as an CLA and checks if it is valid.

import sys, re

# Check for one CLA only:
if len(sys.argv) > 2:
    print("Please enter just one email address.")
    quit()
elif len(sys.argv) < 2:
    print("Usage: emailChecker.py [email address].")
    quit()
    
# Constructs a regex expression to compare with email:
emailRegex = re.compile(r'\w+@\w+\.\w+(\.\w+)?')
mo = emailRegex.search(sys.argv[1])

if not mo:
    print(sys.argv[1] + " is not a valid email address. Please try again.")
else:
    print(mo.group() + " is a valid email address.")
