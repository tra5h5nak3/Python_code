# Bryce Kelly
# COP 2500
# Lab 10
# Nov 30,2022


fileIn = open("Lab10.csv", "r")
lines = fileIn.readlines()
mydict  = {"course_name": "",
           "course_code":"",
           "credit_hours":"",
           "teacher":"",
           "grade":"",}
mylist  = []
mylist.extend(lines)
for i in mylist:
    clean = i.split(",")
    code = clean[0]
    name = clean[1]
    hour = clean[2]
    teach= clean[3]
    grade= clean[4]
    mydict.update({"course_name":name})
    mydict.update({"course_code":code})
    mydict.update({"credit_hours":hour})
    mydict.update({"teacher":teach})
    mydict.update({"grade":grade})
    print(mydict)
fileIn.close()
