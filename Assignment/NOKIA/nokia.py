phonebook_menu = """
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
0. Back
"""

phonebook_options_menu = """
1. Type of view
2. Memory status
0. Back
"""

messages_menu = """
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
0. Back
"""

message_settings_menu = """
1. Set 1
2. Common
0. Back
"""

set_1_menu = """
1. Message centre number
2. Messages sent as
3. Message validity
0. Back
"""

common_menu = """
1. Delivery reports
2. Reply via same centre
3. Character support
0. Back
"""

call_register_menu = """
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call list
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
0. Back
"""

call_duration_menu = """
1. Last call duration
2. All calls' duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers
0. Back
"""

call_cost_menu = """
1. Last call cost
2. All calls' cost
3. Clear counters
0. Back
"""

call_cost_settings_menu = """
1. Call cost limit
2. Show costs in
0. Back
"""

tones_menu = """
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
0. Back
"""

settings_menu = """
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
0. Back
"""

call_settings_menu = """
1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
0. Back
"""

phone_settings_menu = """
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Lights
6. Confirm SIM service actions
0. Back
"""

security_settings_menu = """
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Phone security
6. Change access codes
0. Back
"""

clock_menu = """
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
0. Back
"""

while True:
    print("""
	MENU
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
0. Exit
""")

    main_choice = input("Enter choice: ")

    if main_choice == "0":
        print("Exiting menu...")
        break

    elif main_choice == "1":
        while True:
            print("\nPHONE BOOK")
            print(phonebook_menu)
            phonebook_choice = input("Enter choice: ")

            if phonebook_choice == "0":
                break
            elif phonebook_choice == "1":
                print("Search")
            elif phonebook_choice == "2":
                print("Service Nos.")
            elif phonebook_choice == "3":
                print("Add name")
            elif phonebook_choice == "4":
                print("Erase")
            elif phonebook_choice == "5":
                print("Edit")
            elif phonebook_choice == "6":
                print("Assign tone")
            elif phonebook_choice == "7":
                print("Send b'card")
            elif phonebook_choice == "8":
                while True:
                    print("\nPHONE BOOK OPTIONS")
                    print(phonebook_options_menu)
                    phonebook_option_choice = input("Enter choice: ")

                    if phonebook_option_choice == "0":
                        break
                    elif phonebook_option_choice == "1":
                        print("Type of view")
                    elif phonebook_option_choice == "2":
                        print("Memory status")
                    else:
                        print("Invalid choice")
            elif phonebook_choice == "9":
                print("Speed dials")
            elif phonebook_choice == "10":
                print("Voice tags")
            else:
                print("Invalid choice")

    elif main_choice == "2":
        while True:
            print("\nMESSAGES")
            print(messages_menu)
            messages_choice = input("Enter choice: ")

            if messages_choice == "0":
                break
            elif messages_choice == "1":
                print("Write messages")
            elif messages_choice == "2":
                print("Inbox")
            elif messages_choice == "3":
                print("Outbox")
            elif messages_choice == "4":
                print("Picture messages")
            elif messages_choice == "5":
                print("Templates")
            elif messages_choice == "6":
                print("Smileys")
            elif messages_choice == "7":
                while True:
                    print("\nMESSAGE SETTINGS")
                    print(message_settings_menu)
                    message_settings_choice = input("Enter choice: ")

                    if message_settings_choice == "0":
                        break
                    elif message_settings_choice == "1":
                        while True:
                            print("\nSET 1")
                            print(set_1_menu)
                            set_1_choice = input("Enter choice: ")

                            if set_1_choice == "0":
                                break
                            elif set_1_choice == "1":
                                print("Message centre number")
                            elif set_1_choice == "2":
                                print("Messages sent as")
                            elif set_1_choice == "3":
                                print("Message validity")
                            else:
                                print("Invalid choice")
                    elif message_settings_choice == "2":
                        while True:
                            print("\nCOMMON")
                            print(common_menu)
                            common_choice = input("Enter choice: ")

                            if common_choice == "0":
                                break
                            elif common_choice == "1":
                                print("Delivery reports")
                            elif common_choice == "2":
                                print("Reply via same centre")
                            elif common_choice == "3":
                                print("Character support")
                            else:
                                print("Invalid choice")
                    else:
                        print("Invalid choice")
            elif messages_choice == "8":
                print("Info service")
            elif messages_choice == "9":
                print("Voice mailbox number")
            elif messages_choice == "10":
                print("Service command editor")
            else:
                print("Invalid choice")

    elif main_choice == "3":
        print("\nChat")

    elif main_choice == "4":
        while True:
            print("\nCALL REGISTER")
            print(call_register_menu)
            call_register_choice = input("Enter choice: ")

            if call_register_choice == "0":
                break
            elif call_register_choice == "1":
                print("Missed calls")
            elif call_register_choice == "2":
                print("Received calls")
            elif call_register_choice == "3":
                print("Dialled numbers")
            elif call_register_choice == "4":
                print("Erase recent call list")
            elif call_register_choice == "5":
                while True:
                    print("\nSHOW CALL DURATION")
                    print(call_duration_menu)
                    call_duration_choice = input("Enter choice: ")

                    if call_duration_choice == "0":
                        break
                    elif call_duration_choice == "1":
                        print("Last call duration")
                    elif call_duration_choice == "2":
                        print("All calls' duration")
                    elif call_duration_choice == "3":
                        print("Received calls' duration")
                    elif call_duration_choice == "4":
                        print("Dialled calls' duration")
                    elif call_duration_choice == "5":
                        print("Clear timers")
                    else:
                        print("Invalid choice")
            elif call_register_choice == "6":
                while True:
                    print("\nSHOW CALL COSTS")
                    print(call_cost_menu)
                    call_cost_choice = input("Enter choice: ")

                    if call_cost_choice == "0":
                        break
                    elif call_cost_choice == "1":
                        print("Last call cost")
                    elif call_cost_choice == "2":
                        print("All calls' cost")
                    elif call_cost_choice == "3":
                        print("Clear counters")
                    else:
                        print("Invalid choice")
            elif call_register_choice == "7":
                while True:
                    print("\nCALL COST SETTINGS")
                    print(call_cost_settings_menu)
                    call_cost_settings_choice = input("Enter choice: ")

                    if call_cost_settings_choice == "0":
                        break
                    elif call_cost_settings_choice == "1":
                        print("Call cost limit")
                    elif call_cost_settings_choice == "2":
                        print("Show costs in")
                    else:
                        print("Invalid choice")
            elif call_register_choice == "8":
                print("Prepaid credit")
            else:
                print("Invalid choice")

    elif main_choice == "5":
        while True:
            print("\nTONES")
            print(tones_menu)
            tones_choice = input("Enter choice: ")

            if tones_choice == "0":
                break
            elif tones_choice == "1":
                print("Ringing tone")
            elif tones_choice == "2":
                print("Ringing volume")
            elif tones_choice == "3":
                print("Incoming call alert")
            elif tones_choice == "4":
                print("Composer")
            elif tones_choice == "5":
                print("Message alert tone")
            elif tones_choice == "6":
                print("Keypad tones")
            elif tones_choice == "7":
                print("Warning and game tones")
            elif tones_choice == "8":
                print("Vibrating alert")
            elif tones_choice == "9":
                print("Screen saver")
            else:
                print("Invalid choice")

    elif main_choice == "6":
        while True:
            print("\nSETTINGS")
            print(settings_menu)
            settings_choice = input("Enter choice: ")

            if settings_choice == "0":
                break
            elif settings_choice == "1":
                while True:
                    print("\nCALL SETTINGS")
                    print(call_settings_menu)
                    call_settings_choice = input("Enter choice: ")

                    if call_settings_choice == "0":
                        break
                    elif call_settings_choice == "1":
                        print("Automatic redial")
                    elif call_settings_choice == "2":
                        print("Speed dialling")
                    elif call_settings_choice == "3":
                        print("Call waiting options")
                    elif call_settings_choice == "4":
                        print("Own number sending")
                    elif call_settings_choice == "5":
                        print("Phone line in use")
                    elif call_settings_choice == "6":
                        print("Automatic answer")
                    else:
                        print("Invalid choice")

            elif settings_choice == "2":
                while True:
                    print("\nPHONE SETTINGS")
                    print(phone_settings_menu)
                    phone_settings_choice = input("Enter choice: ")

                    if phone_settings_choice == "0":
                        break
                    elif phone_settings_choice == "1":
                        print("Language")
                    elif phone_settings_choice == "2":
                        print("Cell info display")
                    elif phone_settings_choice == "3":
                        print("Welcome note")
                    elif phone_settings_choice == "4":
                        print("Network selection")
                    elif phone_settings_choice == "5":
                        print("Lights")
                    elif phone_settings_choice == "6":
                        print("Confirm SIM service actions")
                    else:
                        print("Invalid choice")

            elif settings_choice == "3":
                while True:
                    print("\nSECURITY SETTINGS")
                    print(security_settings_menu)
                    security_settings_choice = input("Enter choice: ")

                    if security_settings_choice == "0":
                        break
                    elif security_settings_choice == "1":
                        print("PIN code request")
                    elif security_settings_choice == "2":
                        print("Call barring service")
                    elif security_settings_choice == "3":
                        print("Fixed dialling")
                    elif security_settings_choice == "4":
                        print("Closed user group")
                    elif security_settings_choice == "5":
                        print("Phone security")
                    elif security_settings_choice == "6":
                        print("Change access codes")
                    else:
                        print("Invalid choice")

            elif settings_choice == "4":
                print("Restore factory settings")
            else:
                print("Invalid choice")

    elif main_choice == "7":
        print("\nCall divert")

    elif main_choice == "8":
        print("\nGames")

    elif main_choice == "9":
        print("\nCalculator")

    elif main_choice == "10":
        print("\nReminders")

    elif main_choice == "11":
        while True:
            print("\nCLOCK")
            print(clock_menu)
            clock_choice = input("Enter choice: ")

            if clock_choice == "0":
                break
            elif clock_choice == "1":
                print("Alarm clock")
            elif clock_choice == "2":
                print("Clock settings")
            elif clock_choice == "3":
                print("Date setting")
            elif clock_choice == "4":
                print("Stopwatch")
            elif clock_choice == "5":
                print("Countdown timer")
            elif clock_choice == "6":
                print("Auto update of date and time")
            else:
                print("Invalid choice")

    elif main_choice == "12":
        print("\nProfiles")

    elif main_choice == "13":
        print("\nSIM services")

    else:
        print("Invalid choice")
