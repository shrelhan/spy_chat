print "Let\'s gets started"

spy_name = raw_input("Welcome to spyChat app. But first tell me your spyName: ")

if len(spy_name) > 0 :

# Below we are saving the values of spy like name and printing a statement after getting the value
    spy_name = raw_input("What is your name ?")
    spy_salutation = raw_input("What should we call you (Mr. or Mrs.) ?")

# Below method is called re-assigning the variable value to new one
    spy_name = spy_salutation + " " + spy_name

# print is used to print any statement carrying inputs
    print "Welcome " + spy_name + ". Glad to have you back with us."

else :
    print "A spy need to have valid name. Try again with you name."