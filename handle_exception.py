# import datetime
#
# DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# def is_leap(year):
#     "year -> 1 if leap year, else 0."
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
#
# def days_in_month(year, month):
#     "year, month -> number of days in that month in that year."
#     assert 1 <= month <= 12, month
#     if month == 2 and is_leap(year):
#         return 29
#     return DAYS_IN_MONTH[month]
#
# try:
#     while True:
#         year = int(input("Enter Year"))
#         if datetime.MAXYEAR <= year or year <= datetime.MINYEAR:
#             print("Invalid Year")
#             continue
#         break
#     while True:
#         month = int(input("Enter Month"))
#         if not 1 <= month <= 12:
#             print("Invalid Month")
#             continue
#         break
#     while True:
#         day = int(input("Enter Day"))
#         dim = days_in_month(year, month)
#         if not 1 <= day <= dim:
#             print("Invalid Day")
#             continue
#         break
#     date = datetime.date(year,month,day)
#     print(date)
# except:
#     print("Invalid Input")
#
# a = 10
# b = 30
# print(a+b)
#
num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter Number 2 :"))
try:
    result_div = num1 / num2
    print("Div = ", result_div)
except:
    print("Div = ","Error Occurred")

result_sum = num1 + num2
print("Sum = ",result_sum)

result_sub = num1 - num2
print("Sub = ",result_sub)

result_mul = num1 * num2
print("Mul = ",result_mul)


