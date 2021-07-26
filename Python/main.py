import csv

class College:
    def __init__(self,collegeId, collegeName, courseType, city, fees, pinCode):
        self.collegeId=collegeId
        self.collegeName=collegeName
        self.courseType=courseType
        self.city=city
        self.fees=fees
        self.pinCode=pinCode

    def setData(self):
        data=[self.collegeId,self.collegeName,self.courseType,self.city,self.fees,self.pinCode]
        with open('colleges.csv','a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)


while True:
    rows = []
    with open('colleges.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)

    print("\n")
    print("----------------------------------------------------")
    print("FUNCTIONALITIES:")
    print("     1. Register New College")
    print("     2. Display Colleges in Mumbai Who Teach Engineering")
    print("     3. Remove College based on collegeId")
    print("     4. Exit")
    print("\n")
        
    inp1=input("Please Choose Your Function:")
    if inp1.lower()=='1':
        print("\n")
        print("---------Registering New College------------")
        collegeId=input("Please Enter The College ID:")
        collegeName=input("Please Enter The College Name:")
        courseType=input("Please Enter The Course Type:")
        city=input("Please Enter The City:")
        fees=input("Please Enter The Fees:")
        pinCode=input("Please Enter The Pincode:")
        newcollege=College(collegeId, collegeName, courseType, city, fees, pinCode)
        newcollege.setData()
    elif inp1.lower()=='2':
        print("\n")
        print("---------Displaying Colleges in Mumbai who teach Engineering---------")
        for row in rows:
            if row[3].lower()=='mumbai' and row[2].lower()=='engineering':
                print("----------------------------------------------------")
                print('collegeId   :  '+row[0])
                print('collegeName :  '+row[1])
                print('courseType  :  '+row[2])
                print('city        :  '+row[3])
                print('fees        :  '+row[4])
                print('pinCode     :  '+row[5])
    elif inp1.lower()=='3':
        print("\n")
        print("---------Removing College based on College ID---------")
        collegeId=input("Enter The College ID:")
        for row in rows:
            if row[0]==collegeId:
                rows.remove(row)
        with open('colleges.csv',"w",newline="") as f:
            Writer=csv.writer(f)
            Writer.writerows(rows)
            print("College Has been Deleted From The File")

    elif inp1.lower()=='4':
        print("Thank You For Using This Service")
        break

