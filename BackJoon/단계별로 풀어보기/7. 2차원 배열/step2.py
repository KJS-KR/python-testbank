# <그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

# sub_list1 = [[3, 23, 85, 34, 17, 74, 25, 52, 65],
#         [10, 7, 39, 42, 88, 52, 14, 72, 63],
#         [87, 42, 18, 78, 53, 45, 18, 84, 53],
#         [34, 28, 64, 85, 12, 16, 75, 36, 55],
#         [21, 77, 45, 35, 28, 75, 90, 76, 1],
#         [25, 87, 65, 15, 28, 11, 37, 28, 74],
#         [65, 27, 75, 41, 7, 89, 78, 64, 39],
#         [47, 47, 70, 45, 23, 65, 3, 41, 44],
#         [87, 13, 82, 38, 31, 12, 29, 29, 80]]

total = []
for i in range(9):
    sub_list = list(map(int, input().split()))
    total.append(sub_list)

max_list = []
for row in total:
    max_num = max(row)
    max_list.append(max_num)
    
total_max = max(max_list)
row_index = max_list.index(total_max)
column_index = total[row_index].index(total_max) 
print(total_max)
print(row_index+1, column_index+1)