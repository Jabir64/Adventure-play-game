def welcome():
    print("A WARM WELCOME TO THE ADVENTURE PLAY!")
    name = input("Game: May i know your name:")
    print("That's great", name)
    start_game = input("Shall we start the game now?...YES or NO:")
    if start_game == "yes":
        print("*phone rings*")
        call = input("Type c to get the call:")
        if call == "c":
            print("PHONE: Good evening sir,Am i speaking to mr.jabir?")
            ans = input("type YES/NO: ")
            if ans == "yes":
                print("-PHONE: Sir,Your name has been selected as coupon winner for 10000rs\n"
                      "So that we need to know about your bank details")
                print("-PHONE: Are u willing to share it with us sir? ")
                ans = input("type YES/NO: ")
                if ans == "yes":
                    print("-PHONE: thank you sir,You can tell now")
                    acc = input("-PHONE: May i know your account number:")
                    ifsc = input("-PHONE: your IFSC code:")
                    branch = input("-PHONE: the branch name:")
                    print("-PHONE: Thank you for the details sir!,")
                    print("-PHONE: Your 10000rs voucher will reach you within 2days sir,thank you for the cooperation!")
                    print("*call hanged*")
                    print("---------------------------------------------------------")
                    print("######## now your getting into the serious part ", name, " #########")
                    print("---------------------------------------------------------")
                    print("***** A message from the bank *****")
                    print("""THIRTY THOUSAND HAS BEEN DEBITED FROM YOUR ACCOUNT \n
                    AS CLEARANCE FROM YOU, THE REFERENCE ID:3878949444""")
                    print("")
                    print("-GAME: You want complaint about this issue to the police?")
                    ans = input("type YES/NO:")
                    if ans == "yes":
                        print("*you were in police station*")
                        print("-POLICE: yes sir,whats your problem")
                        you = input("YOU: ")
                else:
                    print("Otherwise you can't get that 10000rs voucher sir.")
            else:
                print("sorry for the wrong call,sir")
    else:
        print("move out from the game")
