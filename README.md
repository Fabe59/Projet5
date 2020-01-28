# Projet5
This program was made to complete the Project 5 of the « D.A. - PYTHON » path from OpenClassrooms. The purpose is to use the public data from the OpenFoodFacts website. In brief, this program gives to the user some substitute type of food for a given chosen one, with better nutrition score and the place where to buy it.

# How to configure and install this program
To setup the program for localhost, one first need to install :
* Python 3
* Mysql  

Then, you must indicate login and password of your database in `connection.py` module  
Next, initialize the virtual environment with : `pipenv install`  
Finally, position yourself in the virtual environment : `pipenv shell`

# How to use it
First step, to configure this program for the first time, you must execute `python dbinstall.py` to create database and all tables.  
Finally, to run the main program, everytime one wants, just run `python interface.py`.
