import random 

valu = ["r", "p", "s"]
print('''Rules:
      r means Rock
      p means Paper and
      S means scissors''')


game = input("Enter your choice")
computer = random.choice(valu)
if not game in valu:
    print("Bhai, Tu to yaha see jaa")
print(computer)

#my own algorithm to do this
if game != computer:
    if game=="r" and computer=="p":
        print("hahaha, Humans are bad")
    if game=="r" and computer=="s":
        print("shit, how can u be smart!")

    if computer=="r" and game=="paper":
        print("tchhh. How !??")
    if computer=="r" and game=="s":
        print("Jalwa hai hamara")

if game==computer:
    print("We are friends -> Tie!")