#Allyssa Dalton
#Date Started 09-15-2021

'''
Random Dice Roller
'''

#creates empty val 
#imports random for random num gen
es=" "
import random 

#asks for the amount of dice & how many sides
aod=int(input("How many dice would you like to roll? "))
aos=int(input("How many sides would you like your dice to have?"))
aot=int(input("How many times would you like to roll the dice? "))

#creates loops for # of dice & times
#prints sequence of numbers in order rolled
for i in range(aot):
  for i in range(aod):
    random.randrange(1,aos)
    num=random.randrange(1,aos)
    num=str(num)
    es=es+num+","+" "
print("Every number rolled in order:")
print(es)
