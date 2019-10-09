with open('test.txt', 'rb') as f:
    # for line in f:
    #     print(line,end='')
    # content = f.readline ()
    # print(content)
    #  print (f.read(20),end='')
    #  print(f.read(20),end='')
    #  print(f.read(20),end='')
    #  print(f.read(20),end='')
    with open('copymp3.txt','wb') as f_write:
        size = 100
        context = f.read(size)
        while len(context) > 0:
            f_write.write(context)
            context = f.read(size)
