spy_name = input(" Welcome To spychat Tell me you name first: ")
if len(spy_name)>0:
       spy_salatation = input(" welcome " + spy_name + " what should I call you Mr./Miss.? ")
       spy_name = spy_salatation  +  " "  +  spy_name
       spy_age = input(" okey " +  spy_name  +  "  Enter your age: ")
       spy_age =int(spy_age)
       if spy_age>12 and spy_age<60 :
          spy_rating =input(" rating: ")
          spy_rating = float(spy_rating)    #typecasting from str to float
          if spy_rating>=4.5:
             print('great!you are an ace user')
          elif spy_rating<4.5 and spy_rating>=3.5:
             print('good,soon to be ace')
          elif spy_rating<3.5 and spy_rating>=2.5:
             print('you are doing good')
          else:
             print('you can do better')
             is_online = true
             print(spy_name + " age: " + str(spy_age) + " and rating: " + spy_rating + " We are proud to have you onboard")
       else:
          print("Ooops! sorry ,you are not of correct age to be our spy")

else:
       print("sorry you have entered an invalid name!")
