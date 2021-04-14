class student(object):
    # use def to deal with, learning from the internet
    def speak(self):
        print("full name:%s,%s  Undergraduate programme:%s"%(self.first_name,self.last_name,self.programme))
A = student()
# as an example
A.first_name = "Cai"
A.last_name = "Xinyi"
A.programme = "BMI"
A.speak()
# as the input
A.first_name = input('please write the first name here:')
A.last_name = input('please write the last name here:')
A.programme = input('please write the programme here:')
A.speak()
