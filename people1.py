name=["rishabh - meerut",
"imtiyaz - delhi",
"nilima - cochin",
"rati - shimla",
"ayishah - delhi",
"raghu - shimla",
"naseer - kanpur",
"karthikeyan - delhi",
"salma - jaipur",
"pankaj - delhi",
"brijesh - delhi",
"govind - delhi",
"puneet - shimla",
"siddhi - delhi",
"suman - jaipur",
"rajeev - shimla",
"mohinder - delhi",
"rajendra - jaipur",
"priyanka - shimla",
"neela - delhi",
"sashi - jaipur",
"sarika - delhi",
"deepti - shimla",
"harshad - delhi",
"trishna - raipur",
"pradeep - jaipur",
"sekhar - delhi",
"nand - delhi",
"anoop - delhi",
"balwinder - tokyo",]
names_file=open("students_name.html","w")
count=0
for people in name:
    count+=1
    print(count)
    names_file.write(""+ people +"\n")
names_file.close()












