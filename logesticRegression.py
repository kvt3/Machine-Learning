import sys
import random
import math
#import standerdation

######################
#CREATING DATA MATRIX#
######################

def creatingDataset():
    '''''
    data = []
    data, traininglabels = standerdation.creatingDataset()
    #print(data)
    #print(traininglabels)
    '''
    # opening files
    file1 = sys.argv[1]
    datafile = open(file1)
    data = []
    data_line = datafile.readline()
    # reading dataset files
    while (data_line != ''):
        data_line = data_line.replace("[", '')
        data_line = data_line.replace("]", '')
        data_line = data_line.replace(",", '')
        data_value = data_line.split()
        data_value.append('1')
        data_value_no = []
        for i in range(len(data_value)):
            data_value_no.append(float(data_value[i]))
        # creating data matrix
        data.append(data_value)
        data_line = datafile.readline()
    datafile.close()
    #print(data)
    # reading traininglabels file
    file2 = sys.argv[2]
    lablefile = open(file2)
    traininglabels = {}
    lable_line = lablefile.readline()
    while (lable_line != ''):
        lable_values = lable_line.split()
        traininglabels[int(lable_values[1])] = int(lable_values[0])
        #if (traininglabels[int(lable_values[1])] == 0):
            #traininglabels[int(lable_values[1])] = -1
        lable_line = lablefile.readline()
    lablefile.close()
    #print(traininglabels)
    #'''
    wInitialization(data,traininglabels)

###############
#INITIALIZE W #
###############

def wInitialization(data,traininglabels):
    rows = len(data)
    cols = len(data[0])
    w=[]
    for j in range(cols):
        #w.append(0.00002 * random.uniform(0,1) - 0.00001)
        w.append(0.02 * random.uniform(0, 1) - 0.01)

    gradeient_descent(data,traininglabels,w)

#############################
#calculating gradient desent#
#############################
def gradeient_descent(data, traininglabels, w):
    #eta = 0.00000001
    #eta= 0.0001
    eta = 0.01
    diff = 1
    rows = len(data)
    cols = len(data[0])
    error = rows + 10

    # stopping condition
    #for i in range(10):
    while (abs(diff) > 0.0001):
        delf = [0] * cols
        for i in range(rows):
            if (traininglabels.get(i) != None):
                dotprod = dot_product(w, data[i])
                for j in range(cols):
                        # error function
                        delf[j] += ((traininglabels.get(i) - logestic_fun(dotprod)) * float(data[i][j]))

         # update taking small step to find globle minima
        for i in range(cols):
            w[i] = w[i] + eta * delf[i]

        # compute error
        prev = error
        error = 0
        err1=0
        err2=0
        for i in range(rows):
            if (traininglabels.get(i) != None):
                dotprod = dot_product(w, data[i])
                hypo = logestic_fun(dotprod)
                if (hypo == float(0)):
                    hypo = 0.001
                    err1 = -1 * (traininglabels.get(i) * math.log(hypo))
                else:
                    err1 = -1 * (traininglabels.get(i) * math.log(hypo))
                if (hypo == float(1)):
                    hypo = 0.99
                    err2 = -1 * ((1 - traininglabels.get(i)) * math.log((1 - hypo)))
                else:
                    err2 = -1 * ((1 - traininglabels.get(i)) * math.log((1 - hypo)))
                error += (err1 + err2)
        diff = prev - error
        #print("diff:",diff)
    # Finding distance to origin
    # print("w=:",w)
    normw = 0
    for j in range(cols-1):
        normw += w[j] ** 2
        # print(w[j])
    normw = normw ** 0.5
    #print("||w|| =",normw)
    distance_origin= abs(w[len(w)-1])/normw
    #print("distance to origin:", distance_origin,w,normw)
    Calculating_pediction(data,traininglabels,w)

#########################
#CALCULATING DOT PRODUCT#
#########################

def dot_product(w,data):
    cols = len(data)
    dotproduct = 0
    for i in range(cols):
        dotproduct += w[i] * float(data[i])
    return dotproduct


#######################
#calculating logestic #
#######################

def logestic_fun(dotprod):
    logistic = float(1) / (float(1) + math.exp(-1 * dotprod))
    return logistic
#########################
# calculating predication#
#########################

def Calculating_pediction(data, traininglabels, w):
    rows = len(data)
    for i in range(rows):
        if (traininglabels.get(i) != None):
            dotprod = dot_product(w, data[i])
            print(dotprod)
            hypo = logestic_fun(dotprod)
            print(hypo)
            if (dotprod > 0):
                print("1", i)
            else:
                print("0", i)

creatingDataset()
