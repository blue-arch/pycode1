

'''f = open('OpenMe.mp3',encoding='gb18030', errors='ignore')
for each_line in f:
    print(each_line , end='')
f.close()'''

#编写一个程序，接受用户的输入并保存为新的文件，程序实现如图：
'''def filewrite(filename):
    print('请输入内容【单独输入‘:w’保存退出】：')
    f = open(filename,'w')
    while True:
        a = input('请输入')
        if a != ':w':
            f.write('%s\n' % a)  # 注意这里有换行符
        else:
            break

    f.close()

file_name = input('请输入文件名：')
filewrite(file_name)'''

# 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置，程序实现如图：
'''def file_compare(fil1,fil2):
    f1 = open(fil1)
    f2 = open(fil2)
    count = 0
    differ = []
    for line1 in f1:
        line2  = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ

file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')
differ = file_compare(file1, file2)
if len(differ) == 0:
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：' % len(differ))
    print(differ)
    for each in differ:
        print('第%d行不一样' % each)
'''

#编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上，程序实现如图：

'''def output(file_name,num):
    f = open(file_name,encoding='gb18030', errors='ignore')
    count = 0
    while count < num:
        for line in f:
            count += 1
            print(line)

file_name = input('请输入文件名：')
output(file_name,12)'''


#呃，不得不说我们的用户变得越来越刁钻了。要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。（如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容）
#我的方法
'''def output(file,para):
    (start,end) = para.split(':')
    f = open(file, encoding='gb18030', errors='ignore')
    if start == '' and end == '':
        print('文件%s的从开头到结束的内容如下： % file)
        for line in f:
            print(line.strip())
    elif start == '' and end != '':
        for i in range(1,int(end)+1):
            print(f.readline())
        print('文件%s的从开头到第%d行的内容如下：' % (file, int(end)))
    elif start != '' and end == '':
        count = 0
        for line in f:
            count+=1
            while count>int(start):
                print(line.strip())
        print('文件%s的从%d行到结束的内容如下： % (file, int(start)))
    elif start != '' and end != '':
        for i in range(int(start),int(end)+1):
            print(f.readline())
        print('文件%s的从第%d行到第%d行的内容如下：'% (file, int(start), int(end)))

    f.close()
file_name = input('请输入文件名：')
para = input('请输入需要显示的行数【格式如13：21或：21或21：】：')
while para == '':
    para = input('输入有误，请重新输入：')
output(file_name,para)'''

#other way
'''def file_print(file, paragraph):
    (start, end) = paragraph.split(':')
    if start == '':
        start = 1
    else:
        start = int(start)
    if end == '':
        end = -1
    else:
        end = int(end)

    f = open(file,encoding='gb18030', errors='ignore')
    if start == 1:
        if end == -1:
            print('文件%s的从开头到结束的内容如下：' % file)
        else:
            print('文件%s的从开头到第%d行的内容如下：' % (file, end))
    else:
        if end == -1:
            print('文件%s的从%d行到结束的内容如下： % (file, start))
        else:
            print('文件%s的从第%d行到第%d行的内容如下：' % (file, start, end))

    for i in range(start - 1):
        f.readline()
    num = end - start + 1
    if num < 0:
        print(f.read())
    else:
        for i in range(num):
            print(f.readline())
    f.close()


file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
paragraph = input('请输入需要显示的行数【格式如13：21或：21或21：】：')
while paragraph == '':
    paragraph = input('输入有误，请重新输入：')
file_print(file_name, paragraph)
'''

#编写一个程序，实现“全部替换”功能。
def file_replace(file,old,new):
    content = []
    count = 0
    f = open(file,encoding='gb18030', errors='ignore')
    for line in f:
        if old in line:
            count +=line.count(rep_word)        #有可能一行不止一个呢？
            line = line.replace(old,new)
        content.append(line)

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (file, count, old, old, new))
    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(file_name, 'w',encoding='gb18030', errors='ignore')
        f_write.writelines(content)
        f_write.close()

    f.close()

file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name,rep_word,new_word)









































































































































































































































