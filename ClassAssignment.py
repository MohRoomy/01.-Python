class ClassAssignment():
    def Subfields():
        print ("Sub-fields in AI are:")
        lists = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for SAI in lists:
            print (SAI)

    def OddEven():
        num1 = int(input("Enter a Numebr to Check: "))
        if (num1%2)==1:
            print (num1, "is ODD Numebr")
        else:
            print (num1,"is EVEN Numebr")

    
    def Elegible():
        gender = input("Enter Your Gender: ")
        age = int(input ("Enter Your Age: "))
        if (gender=="MALE" or gender == "male"):
            if (age >=21):
                print ("ELEGIBLE")
            else:
                print ("NOT ELEGIBLE")
        elif (gender=="FEMALE" or gender == "female"):
            if (age >=18):
                print ("ELEGIBLE")
            else:
                print ("NOT ELEGIBLE")
        else:
            print ("Invalid Input !!!!!!")
    
            
        
    def percentage():
        mk1 = int(input("Subject1= "))
        mk2 = int(input("Subject2= "))
        mk3 = int(input("Subject3= "))
        mk4 = int(input("Subject4= "))
        mk5 = int(input("Subject5= "))
        tot = mk1+mk2+mk3+mk4+mk5
        print ("Total: ",tot)
        avg = (tot/500)*100
        print ("Percentage: ",'%.14f'%avg)

    
    def triangle():
        height = int(input("Height: "))
        breadth = int(input("Breadth: "))
        area = (height*breadth)/2
        print("Area formula: (Height * Breadth)/2")
        print("Area of Triangle: ","%.2f" %area)
        height1= int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        per = height1+height2+breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",per)

        