# lambdata-ndow33

## What is it?

lambdata-ndow33 is a collection of simple python programs that are meant to help
teach students at lambda how to use a local environment in conjunction with test PyPi
and GitHub. 

Within these files, we've practiced inheritance, object oriented programming, writing 
functions, creating classes, and writing unittests.

## Installation

pip install -i https://test.pypi.org/simple/ my-lambdata-ndow33

## Usage

From the 'home_class.py' file, one can create a 'Home' object with attributes such as
what type of home it is, how many square feet it is, what city the home is in, and 
how much the home cost. Below is an example of its usage

```py

# A simple test to make sure the package has been imported correctly
# Import the Home object
# Pass it a type, square footage, location, and price. 
# Call these attributes on the home function and they should return successfully

from my_lambdata.home_class import Home

house = Home('House', 3000, 'New York City', 3000000)
print(house.kind)
print(house.sq_ft)
print(house.city)
print(house.price)

# You should also be able to run the price per square foot function as follows:

ppsf = Home.price_sq_ft(Home)

#This should give you the price divided by the square footage of the home

print(ppsf)

```