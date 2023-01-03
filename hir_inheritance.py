class ParentClass_1:
    def feature_1(self):
        print('feature_1 from ParentClass_1 is running...')
class ChildClass_2(ParentClass_1):
    def feature_2(self):
        print('feature_2 from ChildClass_2 is running...')

    def feature_1(self):
        print('feature_1 from ChildClass_2 is running...')
class ChildClass(ParentClass_1):
    def feature_3(self):
        print('feature_3 from ChildClass is running...')



class ChildClass3(ChildClass_2,ChildClass):

    def feature_4(self):
        print('feature_4 from ChildClass3 is running...')


obj = ChildClass3()
obj.feature_1()
obj.feature_3()
