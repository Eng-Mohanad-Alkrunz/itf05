class ParentClass:
    def feature_1(self):
        print('feature_1 from ParentClass is running...')
class ChildClass_1(ParentClass):
    def feature_2(self):
        print('feature_2 from ChildClass_1 is running...')

class ChildClass_2(ChildClass_1):
    def feature_3(self):
        print('feature_3 from ChildClass_2 is running...')
        

obj = ChildClass_2()
obj.feature_1()
obj.feature_2()
obj.feature_3()
