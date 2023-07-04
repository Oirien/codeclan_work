# Starting with powering on the computer
password = "admin"
print("Booting PC...")
boot_pc = input("Did the PC power on? Y/N: ").capitalize()
# Does the computer boot?
if boot_pc == "Y":
    password_request = input("PC is turned on, please enter password: ")
    if password_request == password:
        print("You are now logged in!")
    else:
        print("Wrong password!")
    
elif boot_pc == "N":
    print("PC has failed to power up")
    power_on = input("Is the power connected? Y/N: ").capitalize()
    if power_on == "Y":
        print("The power is now connected.")
        powercheck = input("Is your device now working? Y/N: ").capitalize()
        if powercheck == "Y":
            password_request = input("PC is turned on, please enter password: ")
            if password_request == password:
                print("You are now logged in!")
            else:
                print("Wrong password!")
        else:
            print("Your device may not be working.")
    elif power_on == "N":
        print("Please connect the power.")
    else:
        print("Incorrect input")
        exit()
else:
    print("Incorrect input")
    exit()
# If it does login with password, if not check if the computer is plugged in.

# If it is not plugged in, then plug it in. 
# If it is plugged in and still not working the the computer is broken.