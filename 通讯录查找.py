import xlrd
path=r"D:\我的重要文件\计算机科学\python\python进阶\python趣味工具\python趣味工具代码\python-excel\excel通讯录查找\资料.xlsx"
data=xlrd.open_workbook(path)
table=data.sheets()[0]
phoneList = [18079554579,
         17193972939,
         13005684238,
         18093317586,
         16555817144,
         13652862442,
         17102933315,
         18242988942,
         13254714399,
         15200121523]

allNames=table.col_values(1)[1:]
allNumbers=table.col_values(3)[1:]

name_dic={}
for num in phoneList:
    if num in allNumbers:
        name_dic[num]=allNames[allNumbers.index(num)]
    else:
        name_dic[num]="查无此人"

print(name_dic)