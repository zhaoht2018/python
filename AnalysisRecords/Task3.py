"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
numeber_set = {'7', '8', '9'}  # 7,8,9 移动电话
telephone_list = []
bangalore_counts = 0

for telphone in calls:
    area_code1 = telphone[0][0:5]  # 080 班加罗尔固话
    area_code2 = telphone[1][0:2]  # (0 固话
    area_code3 = telphone[1][0:1]  # 7,8,9 移动电话
    area_code4 = telphone[1][0:5]  # 080 班加罗尔固话

    if area_code1 == '(080)':
        if area_code2 == '(0':
            index = telphone[1].find(')')
            telephone_list.append(telphone[1][1:index])
        elif area_code3 in numeber_set:
            telephone_list.append(telphone[1][0:4])

print("The numbers called by people in Bangalore have codes:")
_telephone_list = list(set(telephone_list))
_telephone_list.sort(key=telephone_list.index)

for telephone_prefix in _telephone_list:
    print(telephone_prefix)

for telephone_prefix in _telephone_list:
    if telephone_prefix == '080':
        bangalore_counts += 1

percent = bangalore_counts / len(_telephone_list) * 100
print("%.2f%% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % (percent))
