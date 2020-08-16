import sys
import random

question = input("Ask the magic 8 ball a question: ")

answers = random.randint(1, 20)

if answers == 1:
    print("As I see it, yes.")

elif answers == 2:
    print("Ask again later.")

elif answers == 3:
    print("Better not tell you now.")

elif answers == 4:
    print("Cannot predict now.")

elif answers == 5:
    print("Concentrate and ask again")

elif answers == 6:
    print("Don’t count on it.")

elif answers == 7:
    print("It is certain.")

elif answers == 8:
    print("It is decidedly so.")

elif answers == 9:
    print("Most likely.")

elif answers == 10:
    print("My reply is no.")

elif answers == 11:
    print("My sources say no.")

elif answers == 12:
    print("Outlook not so good.")

elif answers == 13:
    print("Outlook good.")

elif answers == 14:
    print("Reply hazy, try again.")

elif answers == 15:
    print("Signs point to yes.")

elif answers == 16:
    print("Very doubtful.")

elif answers == 17:
    print("Without a doubt.")

elif answers == 18:
    print("Yes.")

elif answers == 19:
    print("Yes – definitely.")

elif answers == 20:
    print("You may rely on it.")
