print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("Okay! Let's play :)")
score=0


answer = input("What does “www” stand for in a website browser? ")
if answer.lower() == "World Wide Web":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")


answer = input("Which animal can be seen on the Porsche logo? ")
if answer.lower() == "horse":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")


answer = input("What is the most consumed manufactured drink in the world? ")
if answer.lower() == "tea":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What's the fastest land animal? ")
if answer.lower() == "cheetah":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("How many colors are there in the rainbow? ")
if answer.lower() == "7":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What country is responsible for creating the Olympic Games? ")
if answer.lower() == "greece":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("How many teeth does an adult human have? ")
if answer.lower() == "32":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What year was the very first model of the iPhone released? ")
if answer.lower() == "2007":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("Full form of ODI? ")
if answer.lower() == "one day international":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("Who is known as Run Machine in Cricket? ")
if answer.lower() == "virat kohli":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f'you got {score} questions correct')
print(f'you got {score/10*100}%')