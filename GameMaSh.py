from random import *

wives =["Gwyneth Paltrow", "You don't have one she left.",
 "Polygamy, buddy Beyonce and Taylor Swift",
  "You have an internet girlfirend, but your probably being catfished"]

jobs = ["Your a college droput, you live on the street between the alley and the chinese store",
 "You handout newspapers by the L on 14th street.",
 "You got hired by All Star Code to hack Goldman and steal their money"]

cars =["Got reposessed you have to buy a weekly metrocard",
 "Your whippin a toyota hybrid, you need a tax break",
 "You have a butler named Alfred who drives you in a Uber "]
 
homes = ["Mansion","Apartment","Shack","House"]
 
x = raw_input("Who do you want to be your wife")
wives.append(x)     

y = raw_input("What job do you want to have")
jobs.append(y) 

z = raw_input("What car do you want")
cars.append(z)

print("Welcome to Anthony's game of chance") 

print("Your wife will be", choice(wives))

print("Your job will be", choice(jobs))

print("Your car will be", choice(cars))

print("Your form of residency will be",choice(homes))

print("Thanks for playing") 