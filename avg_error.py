import sys

import subprocess
import Balance_error

def avg_error():
    data = sys.argv[1]
    predictions = []
    predict="/home/kalyani/PycharmProjects/machine learning/prediction.txt"
    cnt =0
    for i in range(10):
        cnt = cnt +1
        #print("python3 '/home/kalyani/PycharmProjects/machine learning/SNP/SVC.py' "+
              #" '"+data+"'"+" '/home/kalyani/Desktop/MS-Fall-2016/dataset/test/SNP/labels"+str(i)+"' > '/home/kalyani/PycharmProjects/machine learning/prediction.txt'")
        subprocess.call("python3 '/home/kalyani/PycharmProjects/machine learning/SNP/SVC.py' "+
              " '"+data+"'"+" '/home/kalyani/Desktop/MS-Fall-2016/dataset/test/SNP/labels"+str(i)+"' > '/home/kalyani/PycharmProjects/machine learning/prediction.txt'",shell = True)

        predictions.append(Balance_error.balance_error("/home/kalyani/Desktop/MS-Fall-2016/dataset/test/SNP/trainlabels",
                                                       "/home/kalyani/PycharmProjects/machine learning/prediction.txt"))

    mean = sum(predictions)/cnt
    accu = (1-mean)*100
    print("mean error is :",mean)
    print("accuracy error is :",accu )

avg_error()