# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 2019394
# UoW number: 17613343/1

# Date: 28/11/2019

def PROCESS():
    
    Progress=0 
    Trailing=0
    Retreiver=0
    Excluded=0
    End=0

    while End!="q": #while loop begins

        
        try:
            results1=int(input("Enter number of credit at pass : "))#input pass credit
            results2=int(input("Enter number of credit at defer : "))#input defer credit
            results3=int(input("Enter number of credit at fail : "))#input fail credit

                
            total=results1+results2+results3
            
            if results1 + results2 + results3 != 120:#total should be equal to 120
                print("Total incorrect")#prints Total incorrect if total is equal to 120

            credit=(0,20,40,60,80,100,120)#ranges of values that should be entered
            if results1 in credit and results2 in credit and results3 in credit:
                if results1 == 120 and results2+results3 == 0:
                    print("Progress")
                    Progress += 1
                elif results1 == 100 and results2+results3==20:
                    print("Progress – module trailer")
                    Trailing += 1
                elif 40<=results1<=80 and results2+results3 == 40:
                    print("Do not Progress – module retriever ")
                    Retreiver += 1
                elif results1==60 and results2+results3 == 60:
                    print("Do not Progress – module retriever ")
                    Retreiver += 1
                elif results1==40 and results2!=0 and results2+results3 == 80:
                    print("Do not Progress – module retriever ")
                    Retreiver += 1
                elif results1==40 and results2==0 and results2+results3 == 80:
                    print("Exclude")
                    Excluded += 1
                elif results1==20 and 40<=results2<=100 and results2+results3 == 100:
                    print("Do not progress – module retriever ")
                    Retreiver += 1
                elif results1==20 and results2<40 and results2+results3 == 100:
                    print("Exclude")
                    Excluded += 1
                elif results1==0 and 60<=results2<=120 and results2+results3 == 120:
                    print("Do not progress – module retriever ")
                    Retreiver +=1
                elif results1==0 and 80<=results3<=120 and results2+results3 == 120:
                    print("Exclude")
                    Excluded += 1
                End=input('If you want to end this press "q", else press ENTER : ')#loop ends when 'q' is entered
            else:
                print("Range error")#Range error is displayed when input is out of credit
        except ValueError:
            print("Integer required")#prints Integer required if integers are not given for input

    print("\n""----------------------------------------","\n")
        
    #starts printing horizontal histogram  
    print("Progress", Progress, end=" : ")
    print(Progress*"*")

    print("Trailing", Trailing, end=" : ")
    print(Trailing*"*")

    print("Retreiver", Retreiver, end=" : ")
    print(Retreiver*"*")

    print("Excluded", Excluded, end=" : ")
    print(Excluded*"*")
    print(" ")

    print(Progress + Trailing + Retreiver + Excluded, "outcomes in total.")

PROCESS() #calling the function

