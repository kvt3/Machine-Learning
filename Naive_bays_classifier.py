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
    # reading files
    while (data_line != ''):
        data_value = data_line.split()
        data_value_no = []
        for i in range(len(data_value)):
            data_value_no.append(float(data_value[i]))
        # creating data matrix
        data.append(data_value)
        data_line = datafile.readline()
    datafile.close()

    file2 = sys.argv[2]
    lablefile = open(file2)
    traininglabels = {}
    lable_line = lablefile.readline()
    while (lable_line != ''):
        lable_values = lable_line.split()
        traininglabels[int(lable_values[1])] = int(lable_values[0])
        lable_line = lablefile.readline()

    lablefile.close()
# calling calculateMean function
    calculateMean(traininglabels, data)


##################################
# CALCULATING MEAN OF BOTH CLASSES#
#################################

def calculateMean(traininglabels, data):
    rows = len(data)
    cols = len(data[0])
    mean_class0 = []
    mean_class1 = []

    # FINDING MEAN FOR CLASS0
    for i in range(cols):
        mean1 = float(0)
        count = 0
        for j in range(rows):
            if (traininglabels.get(j) is not None and traininglabels.get(j) == 0):
                mean1 += float(data[j][i])
                count = count + 1
        if (count != 0):
            mean1 = mean1 / count
        mean_class0.append(mean1)

    # FINDING MEAN FOR CLASS1
    for i in range(cols):
        mean2 = float(0)
        count = 0
        for j in range(rows):
            if (traininglabels.get(j) is not None and traininglabels.get(j) == 1):
                mean2 += float(data[j][i])
                count = count + 1
        if (count != 0):
            mean2 = mean2 / count
        mean_class1.append(mean2)
    # calling function for finding standerd devation
    findStanderd_deviation(mean_class0, mean_class1, data, traininglabels)


################################################
# CALCULATING STANDERD DEVIATION OF BOTH CLASSES#
################################################

def findStanderd_deviation(mean_class0, mean_class1, data, traininglabels):
    rows = len(data)
    cols = len(data[0])
    deviation_class0 = []
    deviation_class1 = []
    # FINDING THE STANDERD DEVIALTION FOR CLASS0
    for i in range(cols):
        deviation1 = float(0)
        count = 0
        for j in range(rows):
            if (traininglabels.get(j) is not None and traininglabels.get(j) == 0):
                deviation1 += (float(data[j][i]) - float(mean_class0[i])) ** 2
                count = count + 1
        if (count != 0):
            deviation1 = deviation1 / count
            deviation1 = (deviation1) ** (0.5)
        deviation_class0.append(deviation1)

    # FINDING THE STANDERD DEVIATION FOR CLASS1
    for i in range(cols):
        deviation2 = float(0)
        count = 0
        for j in range(rows):
            if (traininglabels.get(j) is not None and traininglabels.get(j) == 1):
                deviation2 += (float(data[j][i]) - float(mean_class1[i])) ** 2
                count = count + 1
        if (count != 0):
            deviation2 = deviation2 / count
            deviation2 = (deviation2) ** (0.5)
        deviation_class1.append(deviation2)

    # CALLING FUNCTION FOR LABEL PREDICTION
    labelPredication(mean_class0, mean_class1, deviation_class0, deviation_class1, data, traininglabels)


######################################
# PEDICICTING THE CLASS LABELS OF DATA#
######################################

def labelPredication(mean_class0, mean_class1, deviation_class0, deviation_class1, data, traininglabels):
    rows = len(data)
    cols = len(data[0])
    datafile = open("/home/kalyani/PycharmProjects/machine learning/prediction.txt",'w')
    # CALCULATION THE VALUE OS CLASSES CLOSEST TO THE MEAN
    for i in range(rows):
        class0_value = 0
        class1_value = 0
        #if (traininglabels.get(i) == None):
        for j in range(cols):
            # TAKING DIFFERENCE AND FINDING CLASS VALUES
            if (deviation_class0[j] != 0 and deviation_class1[j] != 0):
                class0_value += ((float(data[i][j]) - float(mean_class0[j])) / deviation_class0[j]) ** 2
                class1_value += ((float(data[i][j]) - float(mean_class1[j])) / deviation_class1[j]) ** 2
            # ASSINING THE LABELS
        k=str(i)
        if (class0_value <= class1_value):
            datafile.write('0 '+k+'\n')
        else:
            datafile.write('1 '+k+'\n')

