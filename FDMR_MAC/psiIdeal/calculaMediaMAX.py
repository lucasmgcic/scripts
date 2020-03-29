import sys

if (len(sys.argv) != 2):
    print ('Bad command line')
    print ('Usage: python script.py FILE_TO_CALCULATE_AVERAGE')
    exit(-1)

f = open(sys.argv[1],"r")
average = 0
Sum = 0
elements = 0
max_gain = 0.0
min_gain = 1000.0
for row in f:
    count_column = 0
    for column in row.split(' '):
        if (count_column == 1):
            n=float(column)
            if (n > max_gain):
                max_gain = n
            if (n < min_gain):
                min_gain = n
            Sum += n
            elements += 1.0
        count_column += 1
f.close()
average = Sum / elements
print ('The average is:') 
print (average)
print ('The MAX is:') 
print (max_gain)
print ('The MIN is:') 
print (min_gain)
