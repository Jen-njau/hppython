class students:
    def __init__(self, name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age

    def display(self):
        print("name: %s \ncourse: %s \ngender: %s \nage: %d"
              %(self.name,self.course,self.gender,self.age))
myobj=students("Jane","computer science","female",28)
myobj.display()