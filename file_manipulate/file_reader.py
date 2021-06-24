file_path = 'D:\pycode1\mycode\pi_didits.txt'
with open(file_path) as file_object:
    #contents = file_object.read()
    #print(contents.rstrip())
    lines = file_object.read()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string[:52]+'......')

print(len(pi_string))
birthday = input('please enter your birthday:')
if birthday in pi_string:
    print('yes!')
else:
    print('no!')











































