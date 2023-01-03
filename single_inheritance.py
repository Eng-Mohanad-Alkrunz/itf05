class ParentClass:
    def feature_1(self):
        print('feature_1 from ParentClass is running...')
    def feature_2(self):
        print('feature_2 from ParentClass is running...')
class ChildClass(ParentClass):
    def feature_3(self):
        print('feature_3 from ChildClass is running...')


obj = ChildClass()
obj.feature_1()
obj.feature_2()
obj.feature_3()
