class ParentClass_1:
    def __init__(self,a_value):
        self.a_value = a_value

    def feature_1(self):
        print('feature_1 from ParentClass_1 is running...')

    def feature_2(self):
        print('feature_2 from ParentClass_1 is running...')


class ParentClass_2:

    def __init__(self):
        self.b_value = "b from parent 2"

    def feature_2(self):
        print('feature_2 from ParentClass_2 is running...')

    def feature_4(self):
        print('feature_4 from ParentClass_2 is running...')


class ChildClass(ParentClass_1, ParentClass_2):

    def __init__(self, a_value,c_value):
        super().__init__(a_value)
        self.c_value = c_value

    def feature_3(self):
        print('feature_3 from ChildClass is running...')

    def feature_2(self):
        print('feature_2 from ChildClass is running...')

obj = ChildClass("A Value from PArent 1","C Value From Child ")
obj.feature_1()
obj.feature_2()
obj.feature_3()
obj.feature_4()
