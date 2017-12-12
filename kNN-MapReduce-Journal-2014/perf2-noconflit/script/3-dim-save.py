#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

inter=0
#-------------------------------------------------------------------------------
rc('font', size=27)
rc('legend', fontsize=25)
rc('legend', columnspacing=1)
rc('lines', linewidth=5)
rc('lines',markersize=20)
#tab = ["hzknnj","lsh","hvdknnj","hbnlj","hbknnj"]
tab  = ["hzknnj","lsh","hvdknnj","hbnlj","hbknnj"]
tab2 = ["H-zkNNJ","RankReduce","PGBJ","H-BNLJ","H-BkNNJ"]
#mark = ['o','d','s','*','v']
#-------------------------------------------------------------------------------

HEIGHT=8
#----------------------------------------1-------

def figg():
    fig = figure( figsize=(12, 8), dpi=80)
    fig.subplots_adjust(bottom=0.1,top = 0.8, left=0.15, right=0.85,wspace=0.1,hspace=0.5)
    return fig

def bbox(ax,nb=2):
    ax.tick_params(axis='x', which='major', labelsize=15)
    ax.tick_params(axis='y', which='major')#, labelsize=25)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25),
                  fancybox=True, shadow=True, ncol=nb)

def acc(mat,mat2,cc):
        k=20
        ratioresult=mat2[:,cc]
        recall=mat[:,cc]
        datasetS=50000
        datasetR=datasetS
        nbknnwait=datasetR*k#20*|S|
        result=ratioresult*nbknnwait

        TP=recall*nbknnwait
        print "TP"
        print TP

        TN=datasetS*k-result
        print "TN"
        print TN
        FP=result-TP
        print "FP"
        print FP
        FN=nbknnwait-TP
        print "FN"
        print FN
        accuracy=(TP+TN)/(TP+TN+FP+FN)
        return accuracy

def tracer_graph_dimension(name,notisrand):

    path="../data/dim/"+name+".txt"

    fig =figg()

    #if (notisrand==True):
    nb=5
    #else:
    #   nb=6
    label,mat = file2matrix(path,nb,';')

    ax = fig.add_subplot(1,1,1)
    ax.tick_params(axis='both', which='major', labelsize=20)
    taillebar=5
    if (notisrand):
        # tablabel = ["H-BNLJ","PGBJ-Geo Grouping","RankReduce","H-zkNNJ"]
        tablabel = ["H-zkNNJ","RankReduce","PGBJ-Geo Grouping","H-BNLJ"]
    else:
        # tablabel = ["H-BNLJ","PGBJ-Geo Grouping","PGBJ-Greedy Grouping","RankReduce","H-zkNNJ"]
        #tablabel = ["RankReduce","H-zkNNJ","PGBJ-Greedy Grouping","PGBJ-Geo Grouping","H-BNLJ"]
        #index of colors in reverse order
        tablabel = ["H-zkNNJ","RankReduce","PGBJ-Geo Grouping","H-BNLJ"]
        #tabcolor = [3,5,2,1,0]
    #pour reverse on veut garder le meme ordre
    #tablabel = tablabel[::-1]#pour reverse on veut garder le meme ordre
    #mat = mat[::-1]
    deb=1
    x = range(deb,size(mat[:,1])+deb)

    #if notisrand :
    cpt=4
    cptc=0
    #else :
    #   cpt=5
    #   cptc = 0

    for tla in tablabel :
        print tla
        print mat[:,cpt]
        #if not notisrand :
        #   cptc = tabcolor[cpt-1]
        #   print "---", tla, "cptc=",cptc

        ax.plot(x,mat[:,cpt],c=colors[cptc],marker=mark[cptc],label=tla);
        # we go down because data in the mat array are in reverse order
        cpt -=1
        cptc+=1


    ax.set_xlim(deb-0.5,size(mat[:,1])+deb-0.5+inter)
    bbox(ax)

    if (notisrand):
        tabtick=["2-osm","9-elninos","28-higgs","77-twitter","128-surf","281-blog","386-axial-axis"];
        plt.xticks(x,tabtick)
        ax.set_xlabel("Dimension-File");
    else:
        tabtick=["2","9","28","77","128","281","386"];
        plt.xticks(x,tabtick)
        ax.set_xlabel("Dimension");

    if (notisrand):
        ax.set_yticks(np.arange(20,90,20))
        ax.set_ylim(0,90)
    else:
        ax.set_yticks(np.arange(15,80,15))
        ax.set_ylim(0,65)
    ax.set_ylabel("Time(min)")

    grid(True)
    show()
    fig.savefig('../../img-perf/dim/'+name+'time.pdf',dpi=400)

#--->accuracy
    path="../data/dim/"+name+"-acc.txt"
    label,mat = file2matrix(path,3,';')
    path2="../data/dim/"+name+"-ratio.txt"
    label,mat2 = file2matrix(path2,3,';')
    print path
    fig2 =figg()

    ax2 = fig2.add_subplot(1,1,1)
    ax2.set_xlim(deb-0.5,size(mat[:,1])+deb-0.5+inter)
    ax2.tick_params(axis='both', which='major', labelsize=20)

    cpt=1
    cptc=1
    cc = 1;
    #ax2.set_ylim(1.5)

    #ax2.set_ylim(1.05)
    x = np.array(range(deb,size(mat[:,1])+deb))

    # ax2b=ax2.twinx()
    taillebar=0.2
    cpt=0
    for tla in ["H-zkNNJ","RankReduce"] :

        if cpt == 1 :
            cptc = 1

            cc = 2
        else :
            cptc = 0

            cc  = 1
        ax2.plot(x,mat[:,cc],"--",c=colors[cptc],marker=mark[cptc],linewidth=5,markersize=10,label=tla);
        ax2.plot(x,mat[:,cc]/mat2[:,cc],"-",c=colors[cptc],marker=mark[cptc+2],linewidth=5,markersize=10);

        print tla
        print "cpct=",cptc
        #accuracy=acc(mat,mat2,cc)
        #print acc
        #print accuracy
        # ax2b.bar(x+taillebar*(cpt-1),accuracy,taillebar, color=colors[cptc],hatch = hatches[cptc],alpha=0.3)

        cpt +=1

    ax2.plot(min(x),-4,"--",color="black", label= " recall")
    ax2.plot(min(x),-4,"-",color="black", label= " precision")
    # ax2.bar(min(x),-4,color="black", label= " accuracy",alpha=0.3)


    if (notisrand):
        tabtick=["2-osm","9-elninos","28-higgs","77-twitter","128-surf","281-blog","386-axial-axis"];
        plt.xticks(x,tabtick)
        ax2.set_xlabel("Dimension-File");
    else:
        tabtick=["2","9","28","77","128","281","386"];
        plt.xticks(x,tabtick)
        ax2.set_xlabel("Dimension");
    ax2.set_ylabel("Recall & Precision")
    bbox(ax2,2)
    grid(True)

    if (notisrand):
        ax2.set_yticks(np.arange(0.2,1.09,0.2))
        ax2.set_ylim(0,1.1)
        # ax2b.set_yticks(np.arange(0.2,1.09,0.2))
        # ax2b.set_ylim(0,1.1)
    else:
        ax2.set_yticks(np.arange(0.1,1.09,0.1))
        ax2.set_ylim(0.5,1.05)
        # ax2b.set_yticks(np.arange(0.1,1.09,0.1))
        # ax2b.set_ylim(0.5,1.05)

    # ax2b.set_ylabel("Accuracy")

    show()
    fig2.savefig('../../img-perf/dim/'+name+'acc.pdf',dpi=400)


tracer_graph_dimension("dataset",True)
tracer_graph_dimension("rand",False)
