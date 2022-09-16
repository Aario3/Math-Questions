import random
print("hello welcome to math question,\n to practice to your math.")

additionorsubtraction = input("would you like to have addition or subtraction\n")

questions = input("How many questions do you want?\n")


if additionorsubtraction == "addition":
    for w in range(int(questions)):
        num_1 = (random.randrange(1,1000))
        num_2 = (random.randrange(1,1000))
        print("what is " + str(num_1) + "+" + str(num_2))
        #while loop starts here and then everything else is indented
        while True:
            answer = input()
            if int(answer) == num_1 + num_2:
                print("corect")
                break
            else:
                print("wrong")
                print("what is " + str(num_1) + "+" + str(num_2))
        

elif additionorsubtraction == "subtraction":
     for w in range(int(questions)):
        num_1 = (random.randrange(1,1000))
        num_2 = (random.randrange(1,1000))
        print("what is " + str(num_1) + "-" + str(num_2))
        #while loop starts here and then everything else is indented
        while True:
            answer = input()
            if int(answer) == num_1 - num_2:
                print("corect")
                break
                
            else:
                print("wrong")
            print("what is " + str(num_1) + "-" + str(num_2))
    
        
#for print(int(random.randrange(1, 1000) + (int(random.randrange(1, 1000)range(int(question
