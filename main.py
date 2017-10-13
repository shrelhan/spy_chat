from spy_details import spy
from steganography.steganography import Steganography
from datetime import datetime

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

friends = []

print "Let\'s gets started"

user_select = "Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)?"
existing = raw_input(user_select)

def read_message():
    sender = select_a_friend()

    output_path = input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friend[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"

def send_message():
    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friend[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready!"

def select_a_friend():
    item_number = 0

    for friend in friends:
        print "%d. %s %s age %d with rating %.2f is online" % (item_number +1, friend.salutation,friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose a friend from your friends")
    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to choose from older status (y/n)?")

    if default.upper() == 'N':
        new_status_message = raw_input("What status you want to set?")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print '%d.%s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You did not update your status message'

    return updated_status_message


def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print "Friend Added."
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)



def start_chat(spy):

    current_status_message = None

    spy['name'] = spy['salutation'] + " " + spy['name']

    if spy['age'] > 12 and spy['age'] < 50:
        print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(spy['rating']) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = int(raw_input(menu_choices))

            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                read_message()
            else:
                show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

    current_status_message = add_status(current_status_message)


if existing == "Y":
    start_chat(spy)
else:
    spy['name'] = ''
    spy['salutation'] = ''
    spy['age'] = 0
    spy['rating'] = 0.0
    spy['is_online'] = False

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

        spy['age'] = input("What is your age?")

        spy['rating'] = input("What is your spy rating?")

        spy['is_online'] = True

        start_chat(spy)
    else:
        print 'Please add a valid spy name'