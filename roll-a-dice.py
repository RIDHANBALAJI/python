import random
response=input("Do you want to roll the dice or not? if yes press y if no press n")
response=="y"
no="Thank you see you again!"
yes=random.randint(1,6)
if(response=="y"):
    print(yes)
else:
    print(no)
