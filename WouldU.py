import io

# https://www.buzzfeed.com/javiermoreno/the-toughest-game-of-would-you-rather-you-will-ever-play


def main():

    while True:
        q1 = input(
            "Would you rather:\nA) Be forced to wear wet socks for the rest of your life? \nB) Or be allowed to wash your hair only once a year? \nQ) Im Chicken and want to quit playing!\n>> "
        ).upper()
        if q1 == "A":
            print("62% want moldy feet over the dirtiest hair!")
        elif q1 == "B":
            print("32% want the dirtiest hair over moldy feet!")
        elif q1 == "Q":
            print("Im Done!")
            break
        else:
            print("play fair, its a easy question!")
        print("")

        q2 = input(
            "Would you rather: \nA) Have a finger as a tongue? B) Or tongues as finger? \nQ) Im Chicken and want to quit playing!\n>>"
        ).upper()
        if q2 == "A":
            print("71% want a finger face!")
        elif q2 == "B":
            print("29% prefer to lick everything they touch!")
        elif q2 == "Q":
            print("Im Done!")
            break
        else:
            print("Sucks, you're not play fair!")
        print("")

        q3 = input(
            "Would you rather: \nA) Always have to tell the truth?? B) \n Or Always have to lie? \nQ) Im Chicken and want to quit playing!\n>>"
        ).upper()
        if q3 == "A":
            print("81% accepted to be truth tellers!")
        elif q3 == "B":
            print("19% accepted to be liars!")
        elif q3 == "Q":
            print("Im Done!")
            break
        else:
            print("I do alittle of both, so what!")
        print("")

        q4 = input(
            "Would you rather: \nA) Run your tongue down a New York City sidewalk?? B) Or press your tongue into a stranger's nostril? \nQ)Im Chicken and want to quit playing!\n>>"
        ).upper()
        if q4 == "A":
            print("38% chose this as a option!")
        elif q4 == "B":
            print("62% chose this as a option!")
        elif q4 == "Q":
            print("Im Done!")
            break
        else:
            print("WoW, Your that guy?")
        print("")

        q5 = input(
            "Would you rather: \nA) Find true love? B) Or win the lottery? \nQ) Im Chicken and want to quit playing!\n>>"
        ).upper()
        if q5 == "A":
            print("64% believe in love!")
        elif q5 == "B":
            print("36% believe, its all about the Benjemans, baby!")
        elif q5 == "Q":
            print("Im Done!")
        else:
            print("I bet you'll not answer the last question!")
        print("")

        q6 = input(
            "Would you rather: \nA) Never have internet access again? B) Or Pee yourself in public once a week? \nQ) Im Chicken and want to quit playing!\n>>"
        ).upper
        if q6 == "A":
            print("34% choose off the internet!")
            break
        elif q6 == "B":
            print("25% Accepted this choice!")
            break
        elif q6 == "Q":
            print("Im Done!")
            break
        else:
            print("TOLD YOU, sore player!")
        break

    print("\nGAME OVER!")
    exit


main()
