class Marks(object):
    def __init__(self, out_of_20, out_of_40, out_of_60):
        self.out_of_20 = out_of_20
        self.out_of_40 = out_of_40
        self.out_of_60 = out_of_60

    def feedback(self):
        if self.out_of_20 > 15:
            print("Very Good")
        else:
            print("Work Hard")

Student = Marks(17, 39, 55)
print(Student.feedback())