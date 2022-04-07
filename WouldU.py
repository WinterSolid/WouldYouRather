from contextlib import ExitStack
import io
from re import A

# https://www.buzzfeed.com/javiermoreno/the-toughest-game-of-would-you-rather-you-will-ever-play


def main():

    while True:
        q1 = input(
            "Would you rather:\nA) Be forced to wear wet socks for the rest of your life? \nB) Or be allowed to wash your hair only once a year? \nQ) Im Chicken and want to quit playing!\n>> "
        ).upper()
        if q1 == "A":
            print("62% agree with this choice!")
        elif q1 == "B":
            print("32% agree with this choice!")
        elif q1 == "Q":
            print("Im Done!")
            break
        else:
            print("play fair!")
        print("")

        q2 = input(
            "Would you rather: \n A) Have a finger as a tongue? B) Or be allowed to wash your hair only once a year? Q) Im Chicken and want to quit playing!\n>>"
        ).upper()
        if q2 == "A":
            print("71% agree with this choice!")
        elif q2 == "B":
            print("29% agree with this choice!")
        elif q2 == "Q":
            print("Im Done!")
            break
        else:
            print("play fair!")
        print("")

        q3 = input(
            "Would you rather: \n A) Always have to tell the truth?? B) \n Or Always have to lie? Q) Im Chicken and want to quit playing!\n>>"
        ).upper()
        if q3 == "A":
            print("81% agree with this choice!")
        elif q3 == "B":
            print("19% agree with this choice!")
        elif q3 == "Q":
            print("Im Done!")
            break
        else:
            print("play fair!")
        print("")

        q4 = input(
            "Would you rather: \n A) Run your tongue down a New York City sidewalk?? B) Or press your tongue into a stranger's nostril? Q)Im Chicken and want to quit playing!\n>>"
        ).upper()
        if q4 == "A":
            print("38% agree with this choice!")
        elif q4 == "B":
            print("62% agree with this choice!")
        elif q4 == "Q":
            print("Im Done!")
            break
        else:
            print("play fair!")
        print("")

        q5 = input(
            "Would you rather: \n A) Find true love? B) Or win the lottery? Q) Im Chicken and want to quit playing!\n>>"
        ).upper()
        if q5 == "A":
            print("64% agree with this choice!")
        elif q5 == "B":
            print("36% agree with this choice!")
        elif q5 == "Q":
            print("Im Done!")
        else:
            print("play fair!")
        print("")

        q6 = input(
            "Would you rather: \n A) Never have internet access again? B) Or Pee yourself in public once a week? Q) Im Chicken and want to quit playing!\n>>"
        ).upper
        if q6 == "A":
            print("34% agree with this choice!")
            break
        elif q6 == "B":
            print("25% agree with this choice!")
            break
        elif q6 == "Q":
            print("Im Done!")
            break
        else:
            print("play fair!")
        break

    print("\nGAME OVER!")
    exit


main()
