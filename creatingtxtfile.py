'''opeaning file 'txt1.txt' in write mode
    This mode will rewrite on file 'txt1.txt' if already exist and
    if file 'txt1.txt' was not created before then it will be created.'''
f=open('txt1','w')

#here we started writing
f.write('We are writing in new file txt1.txt now\n')
#writing in a new line
f.write('here we start')