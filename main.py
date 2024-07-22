#Snake ,water, gun game.. 
import random

rnd=int(input("Enter how many round you want to play: "))

mydict={
         "s" : 1 ,
         "w" : 0,
         "g" : -1
       }

rev_dict={
    1 : "Snake" ,
    0 : "Water" ,
    -1: "Gun"
}

my_c=0
com_c=0

for i in range(0,rnd):
    
    print(f"Round {i+1} Start.\n")
    
    computer=random.choice([-1,0,1])
    
    mystr=input("Enter s/w/g : ")
    my=mydict[mystr]
    
    print(f"you chouse {rev_dict[my]} \ncomputer chouse {rev_dict[computer]}")

    if(my==computer):
        print("Draw.")
    else:
        if(my==1 and computer==-1): 
            print("You Lose!")
            com_c=com_c+1
            
        elif(my==1 and computer==0):
            print("You Win!")
            my_c=my_c+1
            
        elif(my==0 and computer==-1):
            print("You Win!")
            my_c=my_c+1
            
        elif(my==0 and computer==1):
            print("You Lose!")
            com_c=com_c+1
            
        elif(my==-1 and computer==0):
            print("You Lose!")
            com_c=com_c+1
            
        elif(my==-1 and computer==1):
            print("You Win!")
            my_c=my_c+1
            
        else:
            print("Something went wrong.")
            
    print(f"\nRound {i+1} Complet.\n")
    
    
print(f"Total score : .\nYour score={my_c}\nComputer score={com_c}")