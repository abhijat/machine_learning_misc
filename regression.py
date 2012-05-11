#!/usr/bin/env python

from numpy import *

def loadDateSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    numFeat = len(fr.readline().split(',')) - 8	# read off the header line
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split(',')
        for i in range(8,numFeat):
            val = curLine[i]
            if val == '':
                val = 0.0
            lineArr.append(float(val))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[1]))
    return dataMat, labelMat

def main():
    xArr, yArr = loadDateSet('train.csv')
    ws = linalg.lstsq(xArr, yArr)[0]
    print type(ws), ws.shape

if __name__ == "__main__":
    main()
