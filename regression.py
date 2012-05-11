#!/usr/bin/env python

from numpy import *

def loadDateSet(fileName, feat_idx, delim=','):
    """ Read a csv file in, return the matrices of the features vs
    labels, feat_idx is where the features begin.
    """
    dataMat = []
    labelMat = []
    fr = open(fileName)
    numFeat = len(fr.readline().split(delim)) - feat_idx	# read off the header line
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split(delim)
        for i in range(feat_idx,numFeat):
            val = curLine[i]
            if val == '':
                val = 0.0
            lineArr.append(float(val))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[1]))
    return dataMat, labelMat

def main():
    xArr, yArr = loadDateSet('train.csv', 8)
    ws = linalg.lstsq(xArr, yArr)[0]
    print type(ws), ws.shape

if __name__ == "__main__":
    main()
