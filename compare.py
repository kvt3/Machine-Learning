import  sys

def cmp():
    # reading traininglabels file
    file1 = sys.argv[1]
    lablefile1 = open(file1)
    traininglabels1 = {}
    lable_line1 = lablefile1.readline()
    while (lable_line1 != ''):
        lable_values1 = lable_line1.split()
        traininglabels1[int(lable_values1[1])] = int(lable_values1[0])
        lable_line1 = lablefile1.readline()
    lablefile1.close()
    print(traininglabels1)

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
    print(traininglabels)

    cntT = 0
    cntF = 0
    print(len(traininglabels))
    row = len(traininglabels)
    for i in range(row):
        if(traininglabels.get(i) == traininglabels1.get(i)):
            cntT += 1
        else:
            cntF +=1

    acc = (cntT/row)*100
    print("true:",cntT)
    print("False:", cntF)
    print("accuracy:",acc)

cmp()