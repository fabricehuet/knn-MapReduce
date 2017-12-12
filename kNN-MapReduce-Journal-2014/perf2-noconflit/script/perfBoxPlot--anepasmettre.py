import numpy as np
import pylab as plt
from readfile import *
totfigs = 5

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))
plt.hold = True
# Create an axes instance
fig.subplots_adjust(bottom=0.2, left=0.12, top = 0.85, right=0.9)
fig.suptitle('HVDKNNJ : BAD BALANCED\n', fontsize=18,fontweight="bold")
path     = "../../../../datares/hvdknnj/"


def trace(path,coord,txt,ylab):
    ax = fig.add_subplot(coord)
    label,mat = file2matrix(path,120,';')
    
    resmat = []
    l = []
    boxes = []
    for m in mat:    
        tmp = []
        l.append(str(int(m[0]))+'*$10^{3}$')
        for i in range(1,len(m)): 
            tmp.append(m[i])
        resmat.append(tmp)
    
    for i in np.arange(len(mat)):    
        boxes.append(resmat[i])
    
    print l
    
    ax.set_xticklabels(l)
    
    ax.set_xlabel("#data by file")
    ax.set_ylabel(ylab)
    ax.yaxis.grid()
    # Create the boxplot
    bp = ax.boxplot(boxes,notch=True, patch_artist=True)
    
    title(txt)
    
    fig.subplots_adjust(hspace=0.5)
    figtext(.02, .02, "\n\nWe can see that the number element of S by bucket isn't well balanced\n")
    for box in bp['boxes']:
        # change outline color$
        # change fill color
        box.set( facecolor = 'gray' ,alpha=0.5)

    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='r', linewidth=0.5)
        
    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='r', linewidth=2)
    
    
    for flier in bp['fliers']:
        flier.set(marker='D', color='r', alpha=0.9)
#----


trace(path+"balancedS.txt",211,"#data/bucket","#element of S ")
trace(path+"balancedTimeS.txt",212,"time/bucket","time(ms)")

fig.savefig('../../../graph/hvdknnj/loadbalancing2.png',dpi=200)
    
show()