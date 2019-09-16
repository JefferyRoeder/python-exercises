#checkbook app notes

#read from txt file

with open('balance_storage_test.txt','r') as bs:
    for line in bs:
        print(line,end = '')


#append to bottom of text file.
with open('balance_storage_test.txt','a') as bs:
    bs.write('\n420')


#brings back most recent (bottom) line from file
with open('balance_storage_test.txt','r') as bs:
    for line in bs:
        last_line = line
    print(line)

#brings back current sum (of all lines)

with open('balance_storage_test.txt','r') as bs:
    amt = 0
    for line in bs:
       # print(line,end = '')
        amt = int(line) + amt
    print(amt)
        