from operator import itemgetter
from collections import Counter
import sys

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
            data_value_no.append(float(data_value[i]))
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

    touple_list =[]
    for i in range(len(data[0])):
        data_list=[]
        for j in range(len(data)):
            data_list.append((float(data[j][i]),traininglabels.get(j)))
        touple_list.append(data_list)

    #print(data)
    #print(traininglabels)
    #print(touple_list)
    findGini(touple_list)

def findGini(touple_list):

    sorted_list=[]
    rows = len(touple_list[0])
    for i in range(len(touple_list)):
        temp= sorted(touple_list[i], key = itemgetter(0))
        sorted_list.append(temp)
    #print(sorted_list,rows)
    list_no =len(sorted_list)
    tup_no = len(sorted_list[0])

    low_Gini =[]
    Gini_split =[]
    Gini_value = []
    for i in range(list_no):
        cnt = 1
        Gini = []
        while(cnt<tup_no):
            left_list = []
            right_list = []
            j = 0
            while(0 <= j and j<cnt):
                left_list.append(sorted_list[i][j])
                j += 1
            while(j<tup_no):
                right_list.append(sorted_list[i][j])
                j +=1
            cnt += 1

            count_map = {}
            for t,l in left_list:
                count_map[l] = count_map.get(l, 0) + 1

            count_map1 = {}
            for t,l in right_list:
                count_map1[l] = count_map1.get(l, 0) + 1

            rp = count_map1.get(1)
            lp = count_map.get(1)
            ll=len(left_list)
            lr = len(right_list)
            if(rp == None):
                rp = 0
            if(lp == None):
                lp = 0
            #print("left list :", left_list)
            #print("right list:", right_list)
            #print("count of letf:", count_map)
            #print("count of right:", count_map1)
            #print(rp,lr,lp,ll)
            temp = (ll/rows)*(lp/ll) *(1-(lp/ll))+(lr/rows)*(rp/lr) *(1-(rp/lr))
            Gini.append(temp)
        Gini_split.append(Gini)
        low_Gini.append(min(Gini))
    lowest_Gini= min(low_Gini)
    lowest_index =low_Gini.index(min(low_Gini))
    #print(Gini_split)
    index = Gini_split[lowest_index].index(lowest_Gini)
    #print(index)
    #print(sorted_list[lowest_index])
    lf=sorted_list[lowest_index][index]
    rg =sorted_list[lowest_index][index+1]
    best_split = (lf[0] + rg[0] )/2
    #print(lf[0],rg[0])
    #print(low_Gini)
    print("coulmn:",lowest_index)
    print("lowest Gini Value:",lowest_Gini)
    print("best split is:",best_split)

creatingDataset()