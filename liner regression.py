import numpy
import random
import math


def data_generate(num, m, c):
    matrix = []
    y = []
    for i in range(num):
        data = [1]
        r = random.randint(0, 300) % 2
        if r == 0:
            data.append(random.gauss(m[0][0], c[0]))
            data.append(random.gauss(m[0][1], c[0]))
            y.append([1])
        else:
            data.append(random.gauss(m[1][0], c[1]))
            data.append(random.gauss(m[1][1], c[1]))
            y.append([-1])
        matrix.append(data)
    return matrix, y

def logistic_regression(Mout, yout, num, w0):
    eta = 0.1
    w = w0
    for i in range(500):
        Eg = numpy.array([[0.0], [0.0], [0.0]])
        check = 0
        wt = numpy.transpose(w)
        for j in range(num):
            power = (-1 * yout[j][0] * numpy.dot(wt, numpy.transpose([Mout[j]])))[0]
            power = math.exp(power) / (1 + math.exp(power))
            power = numpy.transpose([Mout[j]]) * power * -1 * yout[j][0]
            Eg = Eg + power
        Eg = Eg / num
        for j in range(len(Eg)):
            if abs(Eg[j][0] - 0) > 1E-5:
                check += 1
        if check == 0:
            break
        w = w - eta * Eg
    return w



mean = [[2, 3], [0, 4]]
cov = [0.6 ** 0.5, 0.4 ** 0.5]
Ein = 0
Eout = 0
ELout = 0
for ex in range(100):

    Min, yin = data_generate(200, mean, cov)     #D generate
    #for i in range(20):                         #16題追加data
        #data = [1]
        #data.append(random.gauss(6, 0.3 ** 0.5))
        #data.append(random.gauss(0, 0.1 **0.5))
        #yin.append([1])
        #Min.append(data)
    MinT = numpy.transpose(Min)          #Ein liner regression
    X = numpy.dot(MinT, Min)
    X = numpy.linalg.inv(X)
    W = numpy.dot(X, MinT)
    W =numpy.dot(W, yin)
    predict = numpy.dot(Min, W)
    error = 0
    for i in range(len(Min)):
        #error += (predict[i][0] - yin[i][0]) * (predict[i][0] - yin[i][0])   13題
        if predict[i][0] * yin[i][0] < 0:       #14題
            error += 1
    Ein += error / len(Min)        #Ein liner regression  結束

    Mout, yout = data_generate(5000, mean, cov)   #Eout liner regression  0/1 error
    predictout = numpy.dot(Mout, W)
    errout = 0
    for i in range(len(Mout)):
        if predictout[i][0] * yout[i][0] < 0:
            errout += 1
    Eout += errout / len(Mout)                 #Eout liner regression  0/1 error 結束

    #WLogistic = logistic_regression(Min, yin, len(Min), numpy.array([[0.0], [0.0], [0.0]]))   #Eout logistic regression  0/1 error
    #print(Wout, WoutL)
    #predictLout = numpy.dot(Mout, WLogistic)
    #errlout = 0
    #for i in range(len(Mout)):
        #if predictLout[i][0] * yout[i][0] < 0:
            #errlout += 1
    #ELout += errlout / len(Mout)          #Eout logistic regression  0/1 error 結束

Ein = Ein / 100
Eout = Eout / 100
ELout = ELout / 100
print(Ein, Eout, ELout)
print(abs(Ein - Eout))  # 14題答案輸出


#13. (d) 2.8
#14. (e) 0.001
#15. (b)(0.058, 0.058)
#16. (c)(0.09, 0.058)