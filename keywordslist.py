import csv
import re
file = 'Indeed_Search_Data_May.csv'
#file2 = 'citylist.csv'
#data2 = csv.reader(open(file2))
fout = csv.writer(open('IndeedLocationMay.csv', 'w'))

test=0

g = ['location']

try:
       for i in g:
            total=0.0
            #print i
            data = csv.reader(open(file), delimiter ='\t')
            for j in data:
              name = j[0]
              value = float(j[1])
              #print name, value
              if re.search(i, name):
                   print name, value
                   fout.writerow([name, value])
                   #total += value 
            #print i, total            
#fout.writerow([i, total])
except IndexError as init:
     print init
     pass
except ValueError as init:
     print init
     pass
except TypeError as init:
     print init
     pass
except StopIteration:
     data = csv.reader(open(file))
     pass

      
       

      
