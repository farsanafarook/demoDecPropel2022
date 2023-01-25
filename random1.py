import random
#print(random.randrange(1,10))
#make a two player Rock paper scissor game
#one of the player is the computer
#5 chances .print out the winner and point earn by the both player
#remember the rule #time 35min
#rock beat scissor
#scissor beats paper
#paper beats rock
'''
userchoice=0
computerchoice=0
flag=0
compScr=0
userScr=0
def comp():
    import random as ra
    randomnum=int(ra.randrange(1,3))
    return randomnum
def compare(userchoice,computerchoice):
    #inorder to use global variale we need give global
    global compScr
    global userScr
    compScr=int(compScr)
    userScr=int(userScr)
    if(userchoice==1 and computerchoice==2):
        compScr=compScr+1
        print("\n one point for computer")
    elif(userchoice==2 and computerchoice==3):
         userScr=userScr+1
         print("\n one point for user")
    elif(userchoice==3 and computerchoice==1):
         userScr=userScr+1
         print("\n one point for user")
    elif(userchoice==3 and computerchoice==2):
        userScr=userScr+1
        print("\n one point for user")
    elif (userchoice == 2 and computerchoice == 1):
        userScr = userScr + 1
        print("\n one point for user")
    elif(computerchoice == userchoice):
        print("\n draw no points")
    else:
        print("invalid input")
print("\n welcome to the game of rock paper scissor")
print("\n For play in the game u should enter"
      "1.Rock"
      "2.Paper"
    "3.Scissor")


for i in range(5):
    userchoice=int(input("\n Rock-------->1"
                         "\n Paper------->2"
                         "\n Scissor----->3"
                         "\nuser value----->" ))
    computerchoice = comp()
    print(" Computer Value--->",computerchoice)
    compare(userchoice,computerchoice)

if userScr> compScr:
    print("The winner is User with", userScr)
elif userScr < compScr:
    print("The winner is computer with", compScr)
elif userScr == compScr:
    print(" Draw match")
else:
    print("exit")

#anonymous function or lambda function
#lambda [arg1, arg2,......]:expression
#lambda function to fund sum of two numbers
sum1= lambda a,b:a+b
#calling the lambda function
print(sum1(3,4))

is_list=[lambda arg=x: arg*5 for x in range(1,5)]

for item in is_list:
    print(item())

#find the GST,CGST and SCGST of the product from its price
#Define a function which accept price and  GST  percentage
#gst=price*gstpercentage/100
#sgst=price*sgstpercentage/100
#cgst=price*cgstpercentage/100
def myfungst(price,percentage):
  x=price*percentage/100
  print(x)
  print("cgst",x/2)
  print("sgst", x / 3)
price=int(input("enter price"))
percentage=int(input("enter percentage"))
print(myfungst(price,percentage))
'''
#telephone directory using phythone
#create a global dictionary
directory={}
def addorUpdate(name,phno):
    directory.update({phno:name})
    print("added",phno,name)
def list():
    print("contacts are")
    for phno,name in directory.items():
        print(phno,name)
def delete(name):
    del directory[name]
    print("deledt",name)
def searchNumber(name):
    print("name search result", directory.get(name))
#function ro getinput from user
def getUserInput():
    userChoice=int(input("Enter your choice:""1.add contact""2.List contact""3.delete "
                         "4.search"))
    if userChoice==1:
        name=input("enter name")
        phno=int(input("enter phone"))
        addorUpdate(name,phno)
    if userChoice == 2:
        list()
    if userChoice == 3:
        name=input('enter name')
        delete(name)
    if userChoice == 4:
        name=input("enter name")
        searchNumber(name)

