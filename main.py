#Writing code for project on SPY_CHAT
#Date-18/06/2018
#Author-Lata Jatav
from default1 import spy_name,spy_salutation,spy_age,spy_rating
def start_chat(spy_name,spy_age,spy_rating):
    current_status_msg = None
    if spy_age > 12 and spy_age < 60:
        print("Authentication complete!\n Welcome\n %s\n age - %d and rating %2f" %(spy_name,spy_age,spy_rating))
        show_menu = True                                                                                             #ststus udate statement
        while show_menu == True:                                                                                      #adding a menu bar in chat function
            print("========MENU========\n")
            menu = """what do you want to do?
                    1. update a status
                    2. Add a new friend
                    3. Send a secrate message
                    4. Read a personal a meesage
                    5. Read chat from users
                    6. press '0' for exit"""
            menu_choice = input(menu)
            menu_choice = int(menu_choice)
            if menu_choice == 1:
                current_status_msg = add_status(current_status_msg)
                print("your current status is %s" %current_status_msg)
                #status update module
            elif menu_choice == 2:
                print("add friend")             #add a new meesage
#add a new meesage
            elif menu_choice ==3:
                print("Send a secrate message")
#=================Send a secrate message==================================
            elif menu_choice == 4:
                print("Read a personal a meesage")
#===================Read a personal message
            elif menu_choice == 5:
                print("Read chat from users")
#Read chat from users
            elif  menu_choice == 0:
                show_menu = False
                sys.exit()                                                         #defalut statement
            else :
                print ("ooops! you have enter a wrong choice")
    else:
        print("Sorry! you don't have correct age to be an spy user")

def add_status(current_status_msg):
    if current_status_msg != None:
        print("your current ststus is %s" %current_status_msg )
    else:
        print("you do not have any status right now")
        default = input("Do you want to select status form your older status(y/n)?")
        if default.upper() == 'N':
            new_status_msg = input("Add your new status?")
            if len(new_status_msg)>0:
                updated_status = new_status_msg
                STATUS_MESSAGE.append(new_status_msg)
            else:
                print("you have not enter any status\n please try again")
        elif default.upper() == "Y":
            iteam_pos = 1
            if STATUS_MESSAGE == []:
                print ("you don't have any older status message")
            else:
                for message in STATUS_MESSAGE:
                    print ("%d , %s" %(iteam_pos,message))
                    iteam_pos = iteam_pos + 1

            while True :
                status_slection = int(input("slect choice from above status"))
                if status_slection > len(STATUS_MESSAGE):
                    print("invalid choice\nplease try again")
                else:
                    updated_status = STATUS_MESSAGE[status_slection - 1]
                    break
        else:
            print("invalid entry\ntry again")
    return updated_status
    #===========================main fn start_chat==============================
Question = "welcome to spychat /n are you an default user (y/n)?"                #asking a question from a user side
choice = input(Question)
STATUS_MESSAGE = [" Busy","Can't talk","Gym"]                                    #history previous status list
if choice == "Y" or choice =="y":
    start_chat(spy_name,spy_age,spy_rating)
                                                                                 #status udate statement
elif choice == "N" or choice == "n":                                             #continue with default user info
    spy_name = input("Tell me your Name first: ")
    if len(spy_name)>0:
        spy_salutation = input("Welcome "+spy_name+ " What should I call you Mr./Miss.?")
        spy_name = spy_salutation+ "" +spy_name
        spy_age = input("Ok " + spy_name +" Enter your age: ")
        spy_age = int(spy_age)
        if spy_age>12 and spy_age<60:
            spy_rating = input("How much you like it ")
            spy_rating = float(spy_rating)                                      #typecasting from str to float
            if spy_rating>4.5:
                print("great you are an ace user")
            elif spy_rating<=4.5 and spy_rating>=3.5:
                print("good soon to be an ace")
            elif spy_rating<=3.5 and spy_rating>=2.5:
                print("you are doing good")
            else:
                print("true more u can do better")
                is_online = true
                print("Welcome")
                print(spy_name+ "age:" +str(spy_age)+ "and rating:" + str(spy_rating) + "We are proud to have you onboard")
        else:
                print("Ooops! Sorry,you are not of correct age to be our spy")
    else:
        print("Sorry,you have entered an invalid Name!")
