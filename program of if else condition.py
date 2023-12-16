password=input("Enter password")
if 7<=len(password)<=15:
    if "1" in password or "2" in password:
        if "@" in password or "#" in password:
            print ("password has all the three required values/conditions")
        else:
            print("password has no special characters")
    else:
        print("password has no digits")
else:
    print("the length is not up to mark")
