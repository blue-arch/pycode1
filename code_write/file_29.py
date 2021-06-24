'''def file_write(file_name):
    print('请输入内容【单独输入‘：w’保存退出】')
    f = open(file_name,'w')

    while True:
        a = input()
        if a!=':w':
            f.write('%s\n' %a)
        else:
            break
    f.close()

file_name = input('请输入文件名：')
file_write(file_name)'''





'''def file_write(fil1,fil2):
    f1 = open(fil1)
    f2 = open(fil2)
    count = 0
    differ = []
    for each1 in f1:
        each2 = f2.readline()     #for each2 in f2:
        count+=1
        if each1 != each2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ


file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')
differ = file_write(file1,file2)
if len(differ) == 0:
    print('文件完全一样：')

else:
    
    print('两个文件共有【%d】处不同：' % len(differ))
    print(differ)
    for each in differ:
        print('第%d行不一样' % each)'''


'''def output(filename,num):
    f = open(filename,num)
    while num:
        for i in f:
            print(i)
            num-=1
            
    f.close()
filename = input('请输入文件名：')
num = input('请输入行数：')
output(filename,num)'''

'''def file_print(file, num):
    f = open(file)
    print('文件%s的前%d行的内容如下：' % (file, num))
    for i in range(num):
        print(f.readline())
    f.close()


file_name = input('请输入要打开的文件（C:\\test.txt）：')
num = int(input('请输入需要显示该文件前几行：'))
file_print(file_name, num)'''


'''def file_print(file,paargraph):
    (start,end) = paargraph.split(':')

    if start == '':
        start = 1
    else:
        start = int(start)

    if end == '':
        end = -1
    else:
        end = int(end)
    f = open(file)
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
    f.close()'''

'''def file_replace(filename,rep_word,new_word):
    f = open(filename)
    count = 0
    content = []
    for each in f:
        if rep_word in each:
            count+=each.count(rep_word)
            each = each.replace(rep_word,new_word)
        content.append(each)

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (filename, count, rep_word, rep_word, new_word))
    if decide in ['YES','Yes','yes']:
        f_write = open(filename,'w')
        f_write.writelines(content)
        f_write.close()
    f.close()

file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)'''

def save_file(boy,girl,count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open('%s' %(file_name_boy),'w')
    girl_file = open('%s' % (file_name_girl), 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    count = 1
    boy = []
    girl = []

    f = open(file_name)
    for each in f:
        (a,b) = each.split(':')
        if each[:6] != '======':
            if a == '小甲鱼':
                boy.append(b)
            else:
                girl.append(b)
        else:
            save_file(boy, girl, count)
            count += 1
            boy = []
            girl = []
    save_file(boy, girl, count)
    f.close()

split_file('record.txt')





