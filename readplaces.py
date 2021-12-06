f=open("people.txt","r")
data=f.read()
# print(data)
# f.close()
# f.close()
for i in data:
    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
        # f.close()
    elif "shimla" in i:
        sh=open("shimla.txt","a")
        sh.write(i)
        # sh.close()
    else:
        other=open("other.txt","a")
        other.write(i)
        # other.close()
f.close()

