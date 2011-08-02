import re
import porter
from numpy import zeros,dot
from numpy.linalg import norm
import urllib2
from BeautifulSoup import BeautifulSoup
from HTMLParser import *
from nltk.corpus import stopwords
import csv

fout1 = csv.writer(open('DupeFrance.csv', 'w'))
f1 = 'France_links.csv'
data = csv.reader(open(f1), delimiter = '\t')
#check = ['http://www.indeed.fr/Emplois-acheteur', 'http://www.indeed.fr/Emplois-agent-commercial']
for link in data:
 try:
  url1 = link[0]
  #fout1.writerow([url1])
  page = urllib2.urlopen(url1).read()
  pageSoup = BeautifulSoup(page)
  s = str(pageSoup)
  u=[]
  url = "http://www.indeed.fr"
  av = 0
  s = 0
  num = 0
  #count = 0

  b = pageSoup.find('div', attrs={"id" : "LOCATION_rbo"})

  while getattr(b, 'name', None) != 'ul':
      b = b.next


  for i in b:

   istr = str(i)
   start = istr.find('href')
   start = start + 6
   end = istr.find('title')
   end = end - 2

   k = url + istr[start:end]
   if url == k:
     check = 1
   else:
     #fout.writerow([k])
     u.append(k)

  c = pageSoup.findAll('h2', attrs={"class" : "jobtitle"})

  z=[]

  for i in c:
    istr = str(i)
    begin = istr.find('id')
    begin = begin + 7
    end = istr.find('class')
    end = end - 2
    ids =  istr[begin:end]
    z.append(ids)
   
#print z   #prints jobIDs on source page
#print u   #prints all location urls on source page

  for i in u: #loop that scrapes each of the URLs on the source page
    locationPage = urllib2.urlopen(i).read()
    locationSoup = BeautifulSoup(locationPage)
    locationString = str(locationSoup)  
    x = locationSoup.findAll('h2', attrs={"class" : "jobtitle"})
    z1 = []
    for j in x: 
        num = num + 1
        jstr = str(j)
        begin = jstr.find('id')
        begin = begin + 7
        end = jstr.find('class')
        end = end - 2
        jds =  jstr[begin:end]
        z1.append(jds)
        count = 0
        for i1 in z1: #where z1 is a list of jobids for each location
            for i2 in z: #where z is a list of jobids for the original source
                if i1 == i2:
                   count += 1
    s = s + count
    rows = len(u)
  av = float(s)/float(rows)        
  fout1.writerow([url1, av, s])   
  print url1, av, s
 except AttributeError as init:
  fout1.writerow([url1, '0'])
  print init
  pass
 except urllib2.HTTPError as init1:
  fout1.writerow([url1, '0'])
  print init1
  pass
