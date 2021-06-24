#filename = 'alice.txt'

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except:
        #print('can not find the ' + filename + ' file!')
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words')


filenames = ['alice.txt','sddsvsd.txt','svv.txt']
for n in filenames:
    count_words(n)



