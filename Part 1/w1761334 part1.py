# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 2019394
# UoW number: 17613343/1

# Date: 29/11/2019


def PROCESS():
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
                print("Progress") #prints "Progress"
            elif results1 == 100 and results2+results3==20:
                print("Progress – module trailer") #prints "Progress – module trailer"
            elif 40<=results1<=80 and results2+results3 == 40:
                print("Do not Progress – module retriever") #prints "Do not Progress – module retriever"
            elif results1==60 and results2+results3 == 60:
                print("Do not Progress – module retriever ")#prints "Do not Progress – module retriever"
            elif results1==40 and results2!=0 and results2+results3 == 80:
                print("Do not Progress – module retriever ")#prints "Do not Progress – module retriever"
            elif results1==40 and results2==0 and results2+results3 == 80:
                print("Exclude") #print "Excluded"
            elif results1==20 and 40<=results2<=100 and results2+results3 == 100:
                print("Do not progress – module retriever ") #prints "Do not Progress – module retriever"
            elif results1==20 and results2<40 and results2+results3 == 100:
                print("Exclude") #print "Excluded"
            elif results1==0 and 60<=results2<=120 and results2+results3 == 120:
                print("Do not progress – module retriever ")#prints "Do not Progress – module retriever"
            elif results1==0 and 80<=results3<=120 and results2+results3 == 120:
                print("Exclude") #print "Excluded"
        else:
            print("Range error")
    except ValueError:
        print("Integer required")#prints Integer required if integers are not given for input

PROCESS() #calling the function
