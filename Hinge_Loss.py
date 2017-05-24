import sys
import random

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
    wInitialization(data,traininglabels)

###############
#INITIALIZE W #
###############

def wInitialization(data,traininglabels):
    rows = len(data)
    cols = len(data[0])
    w=[]
    #for j in range(cols):
        #w.append(0.00002 * random.uniform(0,1) - 0.00001)
        #w.append(0.02 * random.uniform(0, 1) - 0.01)
    w.append(1)
    w.append(0)
    w.append(-2)
    gradeient_descent(data,traininglabels,w)

#############################
#calculating gradient desent#
#############################
def gradeient_descent(data, traininglabels, w):
    eta = 0.01
    # eta= 0.0001
    diff = 1
    rows = len(data)
    cols = len(data[0])
    error = rows + 10
    a=10000
    # iteration over gardient_decent
    # for k in range(40000):
    # stopping condition
    for i in range(2):
    #while (diff > 0.001):
        delf = [0] * cols
        normw = calculatenormw(w, (cols - 1))
        print("normw:",normw)
        for i in range(rows):
            if (traininglabels.get(i) != None):
                dotprod = dot_product(w, data[i])
                hinge = traininglabels.get(i) * dotprod
                for j in range(cols):
                    if(hinge < 1):
                        # error function
                        delf[j] += -(traininglabels.get(i) * float(data[i][j]))
                        print(float(data[i][j]),delf[j])

         # update taking small step to find globle minima
        for i in range(cols):
            w[i] = w[i] - eta * delf[i]
        print("wi:",w)

        # compute error
        prev = error
        error = 0
        for i in range(rows):
            if (traininglabels.get(i) != None):
                hing = traininglabels.get(i) * dot_product(w, data[i])
                if(hing < 1):
                    error += (1 - hing )
        print("error:",error)
        diff = prev - error
        #print("diff:",diff)
    # Finding distance to origin
    # print("w=:",w)
    normw = 0
    for j in range(cols - 1):
        normw += w[j] ** 2
        # print(w[j])
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

######################
#calculating normw ###
######################
def calculatenormw(w,cols):
    normw = 0
    for j in range(cols):
        normw += w[j] ** 2
        # print(w[j]) normw = normw ** 0.5
    #print("||w|| =", normw)
    return  normw

#########################
# calculating predication#
#########################

def Calculating_pediction(data, traininglabels, w):
    rows = len(data)
    for i in range(rows):
        if (traininglabels.get(i) == None):
            dotprod = dot_product(w, data[i])
            #print(dotprod)
            if (dotprod > 0):
                print("1", i)
            else:
                print("0", i)

creatingDataset()


