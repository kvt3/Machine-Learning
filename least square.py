import sys
import random
#import standerdation
######################
#CREATING DATA MATRIX#
######################

def creatingDataset():
    '''data = []
    data, traininglabels = standerdation.creatingDataset()
    print(data)
    print(traininglabels)
    '''
    # opening files
    data = []
    file1 = sys.argv[1]
    datafile = open(file1)

    data_line = datafile.readline()
    # reading dataset files
    while (data_line != ''):
        data_value = data_line.split()
        data_value.append('1')
        data_value_no = []
        for i in range(len(data_value)):
            data_value_no.append(float(data_value[i]))
        # creating data matrix
        data.append(data_value)
        data_line = datafile.readline()
    datafile.close()
    print(data)
    # reading traininglabels file
    file2 = sys.argv[2]
    lablefile = open(file2)
    traininglabels = {}
    lable_line = lablefile.readline()
    while (lable_line != ''):
        lable_values = lable_line.split()
        traininglabels[int(lable_values[1])] = int(lable_values[0])
        if (traininglabels[int(lable_values[1])] == 0):
            traininglabels[int(lable_values[1])] = -1
        lable_line = lablefile.readline()
    lablefile.close()
    print(traininglabels)
    wInitialization(data,traininglabels)


###############
#INITIALIZE W #
###############

def wInitialization(data,traininglabels):
    rows = len(data)
    cols = len(data[0])
    w=[]
    #for j in range(cols):
    '''for i in range(cols-1):
        mean1 = float(0)
        mean2 = float(0)
        for j in range(rows):
            if (traininglabels.get(j) is not None and traininglabels.get(j) == -1):
                mean1 += float(data[j][i])
            if(traininglabels.get(j) != None and traininglabels.get(j)==1):
                mean2 += float(data[j][i])

        val = (mean1 - mean2)
        w.append(val)
    val = ((mean1 ** 2 - mean2 ** 2)/2)
    '''
    #for j in range(cols):
        # w.append(0.00002 * random.uniform(0,1) - 0.00001)
        #w.append(0.02 * random.uniform(0, 1) - 0.01)
    #w.append(val)
    #print(len(w))
    w.append(1)
    w.append(0)
    w.append(-10)
    gradeient_descent(data,traininglabels,w)

#############################
#calculating gradient desent#
#############################

def gradeient_descent(data,traininglabels,w):
    eta= 0.01
    #eta=0.0001
    #eta= 0.0001
    diff = 1
    rows = len(data)
    cols = len(data[0])
    #error = rows+10
    prevobj = 1000000
    obj = prevobj-10
    #stopping condition
    for i in range(1):
    #while(prevobj - obj> 0.001):
        prevobj = obj
        delf=[0] * cols
        for i in range(rows):
            if(traininglabels.get(i) != None):
                dotprod = dot_product(w, data[i])
                for j in range(cols):
                    #error function
                    print("dl", delf[j],(traininglabels.get(i) - dotprod),traininglabels.get(i),dotprod)
                    delf[j] += ((traininglabels.get(i) - dotprod)* float(data[i][j]))

    #update taking small step to find globle minima
        print("delf:",delf)
        for i in range(cols):
            w[i] = w[i] + eta * delf[i]
        print("wi:",w[i])
        #compute error
        #prev = error
        error = 0
        for i in range(rows):
            if(traininglabels.get(i) != None):
                error += (traininglabels.get(i) - dot_product(w,data[i]))**2
        print("error:",error)
        #diff = prev - error
        obj = error
        #print("diff:",obj - prevobj)
    #Finding distance to origin
    #print("w=:",w)
    normw = 0
    for j in range(cols-1):
        normw += w[j]**2
        print(w[j])
    normw = normw ** 0.5
    #print("||w|| =",normw)
    distance_origin= abs(w[len(w)-1])/normw
    print("distance to origin:", distance_origin)
    Calculating_pediction(data,traininglabels,w)

#########################
#CALCULATING DOT PRODUCT#
#########################

def dot_product(w,data):
    cols = len(data)
    dotproduct=0
    for i in range(cols):
        dotproduct += w[i] * float(data[i])
    return dotproduct

#########################
#calculating predication#
#########################

def Calculating_pediction(data,traininglabels,w):
    rows = len(data)
    for i in range(rows):
        if(traininglabels.get(i) == None):
            dotprod = dot_product(w,data[i])
            if(dotprod > 0):
                print("1",i)
            else:
                print("0",i)


creatingDataset()