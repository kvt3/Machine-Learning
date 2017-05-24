import sys
import random
import math


######################
#CREATING DATA MATRIX#
######################

def creatingDataset():

    # opening files
    file1 = sys.argv[1]
    datafile = open(file1)
    data = []
    data_line = datafile.readline()
    # reading dataset files
    while (data_line != ''):
        data_value = data_line.split()
        data_value_no = []
        col_data =[]
        for i in range(len(data_value)):
            data_value_no.append(data_value[i])
        # creating data matrix
        data.append(data_value)
        data_line = datafile.readline()
    datafile.close()

    # reading traininglabels file
    file2 = sys.argv[2]
    lablefile = open(file2)
    traininglabels = {}
    lable_line = lablefile.readline()
    while (lable_line != ''):
        lable_values = lable_line.split()
        traininglabels[int(lable_values[1])] = int(lable_values[0])
        lable_line = lablefile.readline()
    lablefile.close()
    checkUniqueVal(data, traininglabels)
    #'''


def checkUniqueVal(data, traininglabels):
    datarows = len(data)
    datacols = len(data[0])
    column = [[0 for i in range(datarows)] for j in range(datacols)]

    #creating list of columns
    for i in range(datacols):
        for j in range(datarows):
            column[i][j] = data[j][i]
    #print(column)

    #countng unique number in list
    uniqset = [0] * datacols
    uniqlist = [0] * datacols
    for i in range(datacols):
        uniqset[i] = set(column[i])
        uniqlist[i] = list(uniqset[i])
    #print(uniqlist)

    #counting unique numbers in trainlabels
    lenlabels = len(traininglabels)
    label = []
    for i in range(lenlabels):
        label.append(traininglabels.get(i))
    #print(label)
    labelset = set(label)
    labellist = list(labelset)
    #print(labellist)

    rows = len(uniqlist)
    cols = len(uniqlist[0])
    totalcount = []
    #calculating left and right split
    for i in range(rows):
        cnt=0
        count_dict = []
        for j in range(cols):
            cnt=column[i].count(uniqlist[i][j])
            count_dict.append({uniqlist[i][j]:cnt})
        totalcount.append(count_dict)
    #print(totalcount)

    dict = []

    row = len(column)
    col = len(column[0])
    #print(row , col)
    for i in range(row):
        dict1 = []
        for j in range(col):
            dict1.append((column[i][j],label[j]))
        dict.append(dict1)
    #print(dict)

    count =[]
    for i in range(row):
        count_map = {}
        for t in dict[i]:
            count_map[t] = count_map.get(t, 0) + 1
        count.append(count_map)
    #print(count)

    CalculatingGini(totalcount,count,uniqlist,labellist,datarows,datacols)


def CalculatingGini(totalcount,count,uniqlist,labellist,rows,cols):
   print(totalcount)
   print(count)
   print(uniqlist)
   print(labellist)
   print(rows)
   print(cols)

   listrow = len(uniqlist)
   print(listrow)
   GiniIndex = []
   for i in range(len(uniqlist)):
       Gini = 0
       totalsplit = 0
       for j in range(len(uniqlist[i])):
           splitmul =1
           print(uniqlist[i][j] ,totalcount[i][j].get(uniqlist[i][j]))
           t = totalcount[i][j].get(uniqlist[i][j])
           if(t != None):
               for k in range(len(labellist)):
                   print(count[i],uniqlist[i][j],labellist[k],count[i].get((str(uniqlist[i][j]),labellist[k])))
                   p = count[i].get((str(uniqlist[i][j]), labellist[k]))
                   if( p == None):
                       p = 0
                   splitmul *= (p/t)
                   print(splitmul)
               if(t == None):
                   t = 0
               Gini += (t/rows)*splitmul
               print(Gini)
       GiniIndex.append(Gini)
   print(GiniIndex)
   minGini = min(GiniIndex)
   Bcoulmn = GiniIndex.index(minGini)
   print("column ",(Bcoulmn+1),"give the best split",minGini)





creatingDataset()