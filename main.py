my_list = [75, 32, 40, 70, 100, 80]
count = 0
# for item in my_list:
#     count += 1
#     if item >= 60:
#         print('Student Number', count,'Congratulation! You pass the exam!')
#     else:
#         print('Student Number', count,"Don't worry! You try your best!")

for index, item in enumerate(my_list, start=1):
    if item >= 60:
        print('Student Number', index,'Congratulation! You pass the exam!')
    else:
        print('Student Number', index,"Don't worry! You try your best!")