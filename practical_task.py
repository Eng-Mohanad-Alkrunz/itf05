# max_number = 0
# while True:
#     number = int(input("Enter New Number or 0 to Exit"))
#     if number > max_number:
#         max_number = number
#     if number == 0:
#         break
# print(max_number)
# my_list = [2,10,3,1,4,2,3,1.5]
# min_num = my_list[4]
# j = 0
# my_list = []
# marks_count = int(input("Enter Marks Number:"))

# total = 0
# marks_list = []
# for i in range(marks_count):
#     mark = float(input("Enter Mark "+str(i+1)+" : "))
#     marks_list.append(mark)
#
# average = sum(marks_list) / len(marks_list)
# print(average)
#     print(j,"***")
#     print(i,"---")
#     j += 1
#     if i < min_num:
#         min_num = i
# print(min_num)

marks_list =[]
while True:
    mark = float(input("Enter Mark Please or -1 to exit :"))
    if mark == -1:
        break
    marks_list.append(mark)
print(marks_list)
average = sum(marks_list) / len(marks_list)
print(average)