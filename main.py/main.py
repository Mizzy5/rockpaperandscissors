import random

#Rock beats Scissors
#Paper beats Rock
#Scissors beats Paper


answer =""
choices = ['R','P','S']
random_answer= random.choice(choices)
def repeat():
        global answer
        answer = input("pick R for rock, P for paper or S for scissors:  ")
repeat()        

while(answer not in choices):
    print("not amongst our options\n")
   
    repeat()    
else:
    while(answer ==  random_answer):#for a tie
        
        print("A tie \n")
        print("Player {} : CPU {}".format(answer,random_answer))
        repeat()

    else:
         if(answer =="R" and random_answer=="S"): #rock beats Scissors
            
            print("Player Wins {} : CPU {}".format(answer,random_answer))
         elif(answer =="S" and random_answer=="R"):#rock beats Scissors
             print("Player  {} : CPU  wins{}".format(answer,random_answer))
         elif(answer =="S" and random_answer=="P"):#Scissors beats paper
             print("Player wins  {} : CPU  {}".format(answer,random_answer))  
         elif(answer =="P" and random_answer=="S"):
             print("Player  {} : CPU  wins {}".format(answer,random_answer))  
         elif(answer =="P" and random_answer=="R"):
             print("Player Wins {} : CPU  {}".format(answer,random_answer)) 
         elif(answer =="R" and random_answer=="S"):
             print("Player  {} : CPU  wins {}".format(answer,random_answer))



