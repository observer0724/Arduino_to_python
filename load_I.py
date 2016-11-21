from __future__ import division
import cPickle as cp
import numpy
import csv



la = open('label_2.pkl')
csvf = file('label_2.csv','wb')
writer = csv.writer(csvf)
a = cp.load(la)

n,m = numpy.shape(a)

for i in range(m):
    s = (a[0,9999]-a[0,0])-(a[0,9999]-a[0,i])
    num = int(s/(1/15))
    writer.writerow([a[0,i],a[1,i],s,num])

csvf.close()
