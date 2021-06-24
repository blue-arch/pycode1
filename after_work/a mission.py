f = open('record.txt','r',encoding='utf-8')
#问本里面全是乱码
boy = []
girl = []
count = 1

for line in f:
    # 进行字符串分割
    #line = line.strip('\n')
    # 切片更好，感觉
    #(role,role_spoken) = line.split(':',1)
    if line[:6]!='======':
        if line[0:3] == '小甲鱼':
            boy.append(line[4:])
        if line[0:2] == "客服":
            girl.append(line[3:])


    else:
        #进行文件保存操作
        file_name_boy = 'boy_'+str(count)+'.txt'
        file_name_girl = 'girl_'+str(count)+'.txt'
        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        count += 1

file_name_boy = 'boy_'+str(count)+'.txt'
file_name_girl = 'girl_'+str(count)+'.txt'
boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()
f.close()