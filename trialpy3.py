sp=1500
cp=1200
if sp<cp:
    print("congrats")
    print("you have made an profit",sp-cp,"bucks")
elif sp>cp:
    print("oops u loose")
    print("you have made an loss", cp - sp, "bucks")
else:
    print("you dont make any profit or loss")
