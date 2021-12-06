delhi=open("people_places.txt","r")
# data=delhi.read()
for i in delhi:
    if  "delhi" in i:
        delhi=open("delhi.txt","a")
        delhi.write(i)
        # delhi.close()
    elif "shimla" in i:
        shi=open("shimla.txt","a")
        shi.write(i)
        # shi.close()
    else:
        other=open("other.txt","a")
        other.write(i)
        # other.close()
delhi.close()

