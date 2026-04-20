phonebookmenu = """
1. Search 
2. Search nos 
3. Add Name 
4. Erase 
5. Edit 
6. Assign tone 
7. Send b'card 
8. options 
0 = back
"""

phoneoptions = """
1. Type of view 
2. Memory status 

0 = back
"""

menumessages = """
1.Write messages 
2. Inbox 
3. Outbox 
4. Picture Message 
5. Templates 
6. Smileys 
7. Messages settings 

0 = back
"""

messagesettings = """
1.Message center number 
2. Message sent as 
3. Message validity 
4. Delivery report 

0 = back 
"""

callregisters = """
1.Missed calls 
2. Received calls 
3. Dialled Numbers 
4. Erase recent call list 
5. Show call duration 
6. Show call cost 
7. Call cost setting 

0 = back
"""

callduration = """
1.Last call duration 
2. All call duration 
3. Received call duration 
4. Dialled call duration 
5. Clear timers 

0 = back
"""

callcost = """
1.Last call costs 
2. All call cost 
3. Clear counters 

0 = back
"""

callcostsetting = """
1.Call cost limit 
2. Show costs in 

0 = back
"""

tonesettings = """
1. Ringing tone 
2. Ringing volume 
3. Incoming call alert 

0 = back
"""

menusettings = """
1. Call setting 
2. Phone setting 
3. Security setting 

0 = back
"""

clockmenu = """
1. Alarm clock 
2. Clock settings 
3. Date settings 

0 = back
"""

while True:
    print("""
            Menu
    1.  Phonebook
    2.  Messages
    3.  Chat
    4.  Call Registers
    5.  Tones
    6.  Settings
    7.  Call Divert
    8.  Games
    9.  Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. Sim Services
    0. Exit
    """)

    menuchoice = int(input())

    if menuchoice == 0:
        break

    # PHONEBOOK
    elif menuchoice == 1:
        while True:
            print("\nPhone book")
            print(phonebookmenu)
            submenuchoice = int(input("Enter choice: "))

            if submenuchoice == 0:
                break

            if submenuchoice == 8:
                while True:
                    print("\n" + phoneoptions)
                    option = int(input("Enter option: "))
                    if option == 0:
                        break

    # MESSAGES
    elif menuchoice == 2:
        while True:
            print("\nMessages")
            print(menumessages)
            submenuchoice = int(input("Enter choice: "))

            if submenuchoice == 0:
                break

            if submenuchoice == 7:
                while True:
                    print("\n" + messagesettings)
                    option = int(input())
                    if option == 0:
                        break

    # CHAT
    elif menuchoice == 3:
        print("\nChat")

    # CALL REGISTERS
    elif menuchoice == 4:
        while True:
            print("\nCall Registers")
            print(callregisters)
            submenuchoice = int(input("Enter choice: "))

            if submenuchoice == 0:
                break

            if submenuchoice == 5:
                while True:
                    print("\n" + callduration)
                    if int(input()) == 0:
                        break

            elif submenuchoice == 6:
                while True:
                    print("\n" + callCost)
                    if int(input()) == 0:
                        break

            elif submenuchoice == 7:
                while True:
                    print("\n" + callcostsetting)
                    if int(input()) == 0:
                        break

    # TONES
    elif menuchoice == 5:
        while True:
            print("\nTones")
            print(tonesettings)
            if int(input("Enter choice: ")) == 0:
                break

    # SETTINGS
    elif menuchoice == 6:
        while True:
            print("\nSettings")
            print(menusettings)
            if int(input("Enter choice: ")) == 0:
                break

    # OTHERS
    elif menuchoice == 7:
        print("\nCall divert")

    elif menuchoice == 8:
        print("\nGames")

    elif menuchoice == 9:
        print("\nCalculator")

    elif menuchoice == 10:
        print("\nReminders")

    elif menuchoice == 11:
        while True:
            print("\nClock")
            print(clockmenu)
            if int(input("Enter choice: ")) == 0:
                break

    elif menuchoice == 12:
        print("\nProfiles")

    elif menuchoice == 13:
        print("\nSim Services")
