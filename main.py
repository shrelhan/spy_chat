from spy_details import spy_name, spy_salutation, spy_age, spy_rating
print "Let\'s gets started"

user_select = raw_input("Continue as " + spy_salutation + " " + spy_name + "(Y/N)?")

if user_select == "Y":
    print "app starting."
else:
    spy_name = raw_input("Welcome to spyChat app. But first tell me your spyName: ")
    if len(spy_name) > 0:

        # Below we are saving the values of spy like name and printing a statement after getting the value
        spy_name = raw_input("What is your name ?")
        spy_salutation = raw_input("What should we call you (Mr. or Mrs.) ?")
        spy_name = spy_salutation + " " + spy_name
        # print is used to print any statement carrying inputs
        print "Welcome " + spy_name + ". Glad to have you back with us."

        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False

        spy_age = input("What is your age ?")
        if spy_age > 17 and spy_age < 50:
            spy_rating = input("What is your spyRating ?")
            if spy_rating > 4.5:
                print "Great ace!"
            elif spy_rating > 3.5 and spy_rating < 4.5:
                print "You are one of the good ones."
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print "You can always do better."
            else:
                print "We can always use somebody in the office"
                spy_is_online = True
                print "Authentication complete. Welcome %s age: %d and rating of: %.2f Proud to have you onboard" % (
                spy_name, spy_age, spy_rating)

        else:
            print "You are not in condition to be a spy."
    # Below method is called re-assigning the variable value to new one
    else:
        print "A spy need to have valid name. Try again with you name."
