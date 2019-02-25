
def mainmenu():
    print("=============================================================")
    print("Welcome to the Student and Assessment Managment System")
    print("<A> add details of a student")
    print("<I> insert assignment marks of a student")
    print("<S> search assessment marks for a student")
    print("<Q> quit")     
    print("=============================================================")
    chosenoption=input("Please select an option from the above: ")
    if chosenoption=='<A>':
        optiona()
    if chosenoption=='<I>':
        optioni()
    if chosenoption=='<S>':
        options()
    if chosenoption=='<Q>':
        exit()
    else:
        print("---------------------------------------------------------")
        print("Please enter the valid option")
        print("---------------------------------------------------------")
        mainmenu()
    
    
def optiona():
    studentid=input("Please enter the student ID: ")
    studentname=input("Please enter the student name: ")
    studentcourse=input("Please enter the course: ")
    file=open("students.txt","r")
    for line in file:
        if studentid in line:
            print("Student already exist please enter another student detail")
            optiona()
    print()
    print("Thank You!")
    print()
    print("The details of the student you entered are as follows:")
    print("Student ID: ",studentid)
    print("Student name: ",studentname)
    print("Course: ",studentcourse)
    file=open("students.txt", "a" )
    file.write('{} {} {} \n'.format(studentid,studentname,studentcourse))
    file.close()
    print()
    print("The record has been successfully added to the students.txt file.")
    print()
    def yesnoa():
        yesno=input("Do you want to enter details for another student (Y/N)? ")
        if yesno == 'Y':
            optiona()
        if yesno== 'N':
            mainmenu()
        else:
            yesnoa()
    yesnoa()
    
def optioni():
    studentid=input("Please enter the student ID: ")
    studentsubcode=input("Please enter the subject code: ")
    studentassno=input("Please enter the assessment number: ")
    studentassmarks=input("Please enter assessment marks: ")
    if int(studentassno)<1 or int(studentassmarks)<0:
        print("Please enter valid assignment number or marks ")
        optioni()
    file=open("assessments.txt", "r" )
    
    for line in file:
        if studentid in line:
            if studentsubcode in line:
                print("Student assissement details already exist choose another assessment for the student:")
                optioni()
                file.close()
                break
            
    file=open('assessments.txt','r')
    dta=file.readlines()
    file.close()
    for i in range(len(dta)):
        if studentid==dta[i]:
            dta[i]=" "+studentsubcode+" "+studentassno+" "+studentassmarks
    file=open('assessments.txt','w')    
    file.writelines(dta)                  
    file.close()
    filea=open("assessments.txt",'a')
    file=open("assessments.txt",'r')
    if studentid in file:
        file.close()
        filea.close()
    if filea.closed==False:    
        filea.write('{} {} {} {} \n'.format(studentid,studentsubcode,studentassno,studentassmarks))
        filea.close()
    print()
    print("Thank You!")
    print()
    print("The details of the student you entered are as follows:")
    print("Student ID: ",studentid)
    print("Subject code: ",studentsubcode)
    print("Assessment number: ",studentassno)
    print("Assessment marks: ",studentassmarks)
    print()
    print("The record has been successfully added to the students.txt file.")
    print()
    def yesnoi():
        yesno=input("Do you want to enter details for another student (Y/N)? ")
        if yesno == 'Y':
            optioni()
        if yesno== 'N':
            mainmenu()
        else:
            yesnoi()
    yesnoi()
    
def options():
    studentid=input("Please enter the student ID you want to assessment marks for: ")
    print()
    print("Thank You!")
    print()
    file=open("students.txt", "r" )
    filea=open("assessments.txt", "r" )
    for line in file:
        if studentid in line:
            print("A student has been found")           
            print("Student ID: ",studentid)           
            course=line.split()          
            name=line.split()
            print("Student name: ",''.join(name[1:-1]))
            print("Course: ",course[-1])
            print();print()
            for line in filea:
                if studentid in line:
                    print("Subject Code | Assessment Number | Marks")
                    data=line.split()
                    for i in range(1,len(data),3):
                        print('{}\t\t{}\t\t   {}'.format(data[i],data[i+1],data[i+2]))
        else:
            print("No student found with the ID")
    file.close()
    filea.close()
    def yesnos():
        yesno=input("Do you want to enter details for another student (Y/N)? ")
        if yesno == 'Y':
            options()
        if yesno== 'N':
            mainmenu()
        else:
            yesnos()
    yesnos()
    
mainmenu()


              