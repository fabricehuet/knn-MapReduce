from numpy import *

def file2matrix(filename,nb,sep):
    print(filename)
    fr = open(filename)
    numberofLines = len(fr.readlines())-1
    returnMat=zeros((numberofLines,nb))
    classLabelVector=[]
    fr = open(filename)
    index =0
    cpt=0
    for line in fr.readlines():
        if(cpt==0):
            classLabelVector.append(line.split(sep))
            cpt=cpt+1
            continue
        line = line.strip()
        listFromLine=line.split(sep);
        print listFromLine
        returnMat[index,:]=listFromLine[0:nb]
        index+=1
    return classLabelVector,returnMat
        
        