
var = input("Enter the state name :")
States = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
          "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
          "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
          "Rajasthan","Sikkim", "Tamil Nadu", "Hyderabad", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

class state:
    def __init__(self):
        Start = []

        for i in States:
    
            if i[0] == var:
                Start.append(i)
        print(Start)
s1= state()
print(s1)