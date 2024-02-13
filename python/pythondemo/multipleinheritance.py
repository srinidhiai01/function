class Parent():
    def __init__(self):
        print("family name is bright services")
        
    def AadharAccess(self):
        print("Need Aadhar Access")
    def classroom(self):
        print("You can access Class room")
    def lab01(self):
        print("you can access lab 01")
    def lab02(self):
        print("you can access lab02")
    def aibatch(self):
        print("you can join AI course")
    def cadbatch(self):
        print("your can join Cloud application developer course")
    def nightshiftwork(self):
        print("you can join to work in the us process for us work timing")

class home():
    def __init__(self):
        print("welcome to home")
    def brother(self):
        print("i a have brother")
    def sister(self):
        print("i have sister")

class student(Parent,home):
    def __init__(self):
        print("this is me")
        super().__init__()
        super().AadharAccess()
        super().lab01()
        super().lab02()
        super().classroom()
        super().cadbatch()
        super().brother()
        super().sister()


s=student()