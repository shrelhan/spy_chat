from spy_details import spy_name, spy_salutation, spy_age, spy_rating

print "Let\'s gets started"

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []

def add_friend():
    new_name = input("Please add your friend's name:")
    new_salutation = input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = input("Age?")
    new_rating = input("Spy rating?")

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_status.append(True)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends_name)

def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to choose from older status (y/n)?")

    if default.upper == "N":
        new_status_message = input("What status you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print '%d.%s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("Select from above status."))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES(message_selection - 1)

        return updated_status_message


def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    current_status_message = None

    while show_menu:
        menu_choices = "What do you want to do? \n1.Add a status update.\n2. Close app"
        menu_choice = input(menu_choices)
        if menu_choice == 1:
            current_status_message = add_status(current_status_message)
        elif menu_choice == 2:
            show_menu = False
        else:
            print "You did'nt choose any option."
    current_status_message = add_status(current_status_message)


user_select = raw_input("Continue as " + spy_salutation + " " + spy_name + "(Y/N)?")

if user_select == "Y":
    start_chat(spy_name, spy_age, spy_rating)
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
            start_chat(spy_name, spy_age, spy_rating)

        else:
            print "You are not in condition to be a spy."
    # Below method is called re-assigning the variable value to new one
    else:
        print "A spy need to have valid name. Try again with you name."
