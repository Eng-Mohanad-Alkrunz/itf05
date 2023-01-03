# # def say_hello(name,last_name=None):
# #     print("Hello!",name,last_name)
# #     return 10
# #
# #
# # x = say_hello("Mohanad")
# # print(x)
#
# total = 0
# marks_count = int(input("Enter Marks Count"))
# for mark in range(0,marks_count):
#     while True:
#         mark_int = float(input("Enter Mark " + str(mark + 1) + " :"))
#         if mark_int >= 0:
#             break
#         else:
#             print("Enter Valid Mark")
#     total += mark_int
#
# average = total / marks_count
# print(average)
# if average > 100 or average < 0:
#     print("المعدل غير صالح")
# elif 100 >= average >= 90 :
#     if average > 95:
#         print("ممتاز مع مرتبة الشرف")
#     else:
#         print("ممتاز")
# elif 90 > average >= 80:
#     print("جيد جداً")
# elif 80 > average >= 70:
#     print("جيد")
# elif 70 > average >= 60:
#     print("مقبول")
# elif 60 > average >= 50:
#     print("تحتاج إلى رفع")
# else:
#     print("راسب ولا يرفع")
#
#
# print("Completed")
import  redis


r = redis.Redis()
print(r.get('gsg_items').decode())