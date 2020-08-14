import time
import os

timestamp = time.strftime("%Y%m%d%H%M%S")
#timestamp2 = time.strftime("%Y/%m/%d %H:%M:%S")
executionTime = []

currentPath = os.path.dirname(os.path.realpath(__file__))
path = currentPath + '\\Log'

if not os.path.isdir(path):
    os.mkdir(path)

for order in range(30000):
    executionTime.append(order)

num = 0

"""
def exportLog(content, name):
    global num
    print(content)
    executionTime[num] = time.strftime("%Y/%m/%d %H:%M:%S: ")
    file = open(path + "\\" + name + '(' + timestamp + ').txt', 'a', encoding='utf-8')
    file.writelines(executionTime[num])
    num += 1
    file.writelines(content)
    file.writelines('\n')
"""


def exportLog(content, logName):
    global num
    print(content)
    executionTime[num] = time.strftime("%Y/%m/%d %H:%M:%S: ")
    file = open(path + "\\" + logName + '(' + timestamp + ').txt', 'a', encoding='utf-8')
    file.writelines(executionTime[num])

    num += 1
    if type(content) != list:
        #如果content不是list，那基本上就是字串跟數字。可以直接寫入txt，並且在寫完後換行
        file.writelines(str(content))
        file.writelines('\n')
    elif type(content) == list:
        #如果content是list，那就將content[order]一個一個寫入txt，不然如果直接file.writelines(str(content))的話，list的裡的每個字都會自動換行，讓整個log變得很長
        for order in range(len(content)):
            if order == 0:
                #第一的字的前面不用加逗號
                file.writelines(str(content[0]))
            else:
                file.writelines(', ' + content[order] )
        file.writelines('\n')       


"""無法使用日文及簡體中文
def exportLog(content, name):
    global num
    print(content)
    executionTime[num] = time.strftime("%Y/%m/%d %H:%M:%S:")
    print(executionTime[num], file = open(path + "\\" + name + '(' + timestamp + ').txt', 'a'), encoding='utf-8')
    num += 1
    print(content, file = open(path + "\\" + name + '(' + timestamp + ').txt', 'a'), encoding='utf-8')
    print(' ', file = open(path + "\\" + name + '(' + timestamp + ').txt', 'a'), encoding='utf-8')
"""

"""list會被轉變為sting
def exportLog(content, name):
    global num
    print(content)
    #log = open(name + '(' + timestamp + ').txt', 'a')
    executionTime[num] = time.strftime("%Y/%m/%d %H:%M:%S: ")
    file = open(path + "\\" + name + '(' + timestamp + ').txt', 'a')
    file.writelines(executionTime[num])
    num += 1
    file.writelines(content)
    file.writelines('\n')
"""

#exportLog('content', 'name')