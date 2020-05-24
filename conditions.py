#first program

username =input("Enter Your username :")
password =input("Enter Your Password :")
if username == "kaleem" and password =="123":
    print("welcome to website")
else:
    print("ERROR")

#print("-------------------------------")


#second program
#_______
gender = input("inter your gender: ")
age = int(input("Enter Your Age : "))
if gender == "man":
    if 0 < age <= 18 :
        print("shis man is young man")
    elif 18 < age <=120:
        print("this man is old man ")
    print("he is a man")
elif gender == "woman":
    if 0 < age <= 18 :
        print("shis man is young girl")
    elif 18 < age <=120:
        print("this man is old woman ")
    print("she is a woman")
else:
    print ("ERROR")


