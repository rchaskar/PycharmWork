

student={"rahul":["python","google cloud","power bi"] , "tushar":["ML","AWS"], "vaibhav":["Amazon" , "SQl"]}

key_st=student.keys()

for eachkey in key_st:
    print("courses taken by",eachkey)
    for eachvalue in student[eachkey]:
        print(eachvalue)
