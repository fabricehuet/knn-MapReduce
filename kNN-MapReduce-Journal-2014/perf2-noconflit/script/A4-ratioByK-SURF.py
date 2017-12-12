#------------------selon K
from pylab import *
from readfile import *
from mycolor import *
import copy


NB=0
TIME=1
RATIOMEM=5
ACC=3
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

#----------------------------------------1-------
lab=["2","8","32","64","128","256","512"]
ANGLE=0
def figg():
    fig = figure( figsize=(13, 10), dpi=80)
    fig.subplots_adjust(bottom=0.12,top = 0.83, left=0.15, right=0.85,wspace=0.1,hspace=0.2)
    return fig

def bbox(ax,nb=2):
    ax.set_xticks([2,8,32,64,128,256,512])
    ax.set_xticklabels(lab,rotation=ANGLE)
    ax.tick_params(axis='x', which='major')#, labelsize=35)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20),
                  fancybox=True, shadow=True, ncol=nb)



def keepgoodylabel(ax,matrices,TIME,div,mul=1):
    mini=99999
    maxi2=0
    for mat in matrices :
        mm = mat[:,TIME]/div
        mini = min(mini,min(mm))
        #maxi_x = max(maxi_x,max(mat[:,0]))
        maxi2 = max(maxi2,max(mm))
        ecart=(maxi2-mini)*mul
        step=round(ecart/4)/mul
    ax.yaxis.set_ticks(np.arange(0,maxi2+step/2,step))


def time(name,matrices,isK=False):
    fig = figg()
    ax = fig.add_subplot(1,1,1)
    ax.tick_params(axis='both', which='major')
    cpt=0

    maxi=0;
    div = 1#1000/60
    cc=0
    for mat in matrices :
        # print tab[cc]
        # print mat
        cc=cc+1
        maxi = max(maxi,max(mat[:,TIME]/div))
    # print maxi
    #ax.set_ylim(maxi+1)

    plt.ylim(0, maxi+1)

    for mat in matrices :
        div = 1#1000/60
        #print(mat[:,NB])
        ax.plot(mat[:,NB],mat[:,TIME]/div,color=colors[cpt],
                marker=mark[cpt],label=tab2[cpt])
        cpt += 1
    ax.grid()
    ax.set_xscale('log');
    ax.set_ylabel('Time (min)');
    ax.set_xlabel('k');
    bbox(ax);
    ax.set_xlim(0,513);
    ax.yaxis.set_ticks(np.arange(0,121,30));
    show();
    fig.savefig('../../img-perf/'+name+'/time.pdf',dpi=400)


#----------------------------------------Disk Usage----------------------------
def memoire(name,matrices,matoutput,isK=False):
        fig = figg()
        ax = fig.add_subplot(1,1,1)
        cpt=0
        taillebar=0.15

        mini = 0
        #maxi_x = 0
        maxi=0
        for mat in matrices :
                mini = min(mini,min(mat[:,0]))
                #maxi_x = max(maxi_x,max(mat[:,0]))
                maxi = max(maxi,max(mat[:,RATIOMEM]))

        plt.ylim(0, 20)
        #plt.xlim(mini+2,maxi_x)
        #copy the matrices because we modify them, avoid side effects
        matrices2=copy.deepcopy(matrices)
        for mat in matrices2 :
            # print("xxx ") # + tab2[cpt])
            # print(mat[:,0])
            div = 1#1000/60
           # mat=delete(mat, [2], axis=1)
            #print(mat[:,RsATIOMEM]/div)
            #xlab=log2(mat[:,0]);
            #for i in range(1,size(xlab)):
           #    xlab[i]=xlab[i]+taillebar*cpt
           # print xlab

           # we remove the value at x=96 because
           # it does not look pretty

            index = where(mat[:,0]==96)
            #print(index)
            if len(index[0]) :
                print("Found it!")
                #print(mat)
                mat=delete(mat,index[0][0],axis=0)

            if not isK :
                        mat[:,0] = log2(mat[:,0])
                #+1 because it's originally intermediate/final
            if cpt == 3 or cpt == 0 or cpt ==2 :
                # print("x=",mat[:,RATIOMEM-1])
                ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,RATIOMEM]/div,taillebar,color=colors[cpt],label=tab2[cpt])
                        #print(cpt, mat[:,RATIOMEM-1])
            else :
                # print("cpt=",cpt, "acc=",mat[:,RATIOMEM])
                ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,RATIOMEM]/div,taillebar,color=colors[cpt],label=tab2[cpt])
            cpt +=1
            # print(mat[:,0])
            # print("-------")
            # print(mat[:,0])

        #ax.set_xticks(mat[:,0]+taillebar)
        # ax.set_yscale('log')
        #ax.set_xticks([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        ax.set_yticks([2,5,10,15,20])
        bbox(ax)
        ax.set_xticks([1,3,5,6,7,8,9])
        ax.set_xticklabels(["2","8","32","64","128","256","512"])

        ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
        #ax.xaxis.set_major_formatter(FormatStrFormatter('$2^{%1.1f}$'))
        # ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
        ax.set_xlabel('k')
        ax.set_ylabel('Space requirement')
        #ax.xaxis.set_tick_params(width=5)

        ax2=ax.twinx()
        ax2.plot(log2(matoutput[:,0]),matoutput[:,1]/1024/1024/1024,"--",color="black")
        ax2.set_ylabel('result size (GB)')

        ax2.set_yticks(np.arange(0.4,1.7,0.4))
        ax2.set_ylim(0,1.7)
        #ax2.set_yticks(arange(1,12,1))

        grid(True)
        show()
        fig.savefig('../../img-perf/'+name+'/memory.pdf',dpi=400)

def shuffle(name,matrices,matoutput,isK=False):
        fig =figg()
        fig.subplots_adjust(left=0.2, right=0.85)
        ax = fig.add_subplot(1,1,1) #fig.add_subplot(2,1,1)
        # ax2 = fig.add_subplot(2,1,2)
        cpt=0
        taillebar=0.15

        mini = 0
        #maxi_x = 0
        maxi=0
        for mat in matrices :
                mini = min(mini,min(mat[:,0]))
                #maxi_x = max(maxi_x,max(mat[:,0]))
                maxi = max(maxi,max(mat[:,RATIOMEM]))

        #plt.xlim(mini+2,maxi_x)
        #copy the matrices because we modify them, avoid side effects
        matrices2=copy.deepcopy(matrices)
        maxo = 0
        div=1e9
        div2=63e6*2
        xx=[]
        for mat in matrices2 :
            print tab2[cpt]
            print mat[:,6]
            index = where(mat[:,0]==96)
            #print(index)
            if len(index[0]) :
                print("Found it!")
                #print(mat)
                mat=delete(mat,index[0][0],axis=0)

            if not isK :
                        mat[:,0] = log2(mat[:,0])
                        xx=mat[:,0]
                #+1 because it's originally intermediate/final
            if(cpt<5):
                # print(mat[:,6])
                #ax.plot(mat[:,0],mat[:,6]/div,marker=mark[cpt],color=colors[cpt],label=tab2[cpt])

                # ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,6]/div,taillebar,color=colors[cpt],label=tab2[cpt])
                ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,6]/div2,taillebar,color=colors[cpt],label=tab2[cpt])
                        #print(cpt, mat[:,RATIOMEM-1])
                #ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,6]/div,taillebar,color=colors[cpt],label=tab2[cpt])
                #ax2.bar(mat[:,0]+taillebar*(cpt-2),mat[:,6]/div2,taillebar,color=colors[cpt],label=tab2[cpt])
                        #print(cpt, mat[:,RATIOMEM-1])
                maxo = max(maxo,max(mat[:,6]))
                cpt +=1
                # print(mat[:,0])
            # print("-------")
            # print(mat[:,0])

        #ax.set_xticks(mat[:,0]+taillebar)
        #ax.set_xscale('log')
        #ax.set_xticks([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

        #ax4=ax.twinx()
        #ax4.plot(xx,ones(len(xx))*(63*2/1e3),"--",color="black")
        #ax4.set_ylabel('|R|+|S| (GB)')
        #ax4.set_yticks(np.arange(0.02,0.15,0.02))
        #ax4.set_ylim(0,0.15)
        ax.tick_params(axis='x', which='major')#, labelsize=35)
        ax.set_xticks([1,3,5,6,7,8,9])
        ax.set_xlim(0,10);
        ax.set_ylim(0,0)
        # ax.set_ylim(0,1)
        # ax.set_yticks(np.arange(0,1.2,0.3))
        ax.set_yticks(np.arange(0.0,10,3.0))
        #ax.set_yticklabels(["0.0","8","32","64","128","256","512"])
        # ax2.set_yticks(np.arange(0.0,10,3.0))
        ax.set_xticklabels(["2","8","32","64","128","256","512"],rotation=ANGLE)


        ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
        #ax.xaxis.set_major_formatter(FormatStrFormatter('$2^{%1.1f}$'))
        # ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
        # ax.set_xlabel('k')
        # ax.set_ylabel('CO (GB)')


        # ax2.tick_params(axis='x', which='major', labelsize=35)
        # ax2.set_xticks([1,3,5,6,7,8,9])
        # ax2.set_xlim(0,9);
        # ax2.set_ylim(0,0)
        # ax2.set_yticks(np.arange(0.0,10,3.0))
        # ax2.set_yticks(np.arange(0.0,10,3.0))
        # ax2.set_yticklabels(["0.0","8","32","64","128","256","512"])
        # ax2.xaxis.set_major_formatter(FuncFormatter(powerFormater))
        #ax.xaxis.set_major_formatter(FormatStrFormatter('$2^{%1.1f}$'))
        # ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
        ax.set_xlabel('k')
        #ax2.set_ylabel('Comunication overhead \n(GB)')
        ax.set_ylabel('Communication overhead ratio')
        #ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25),
              #fancybox=True, shadow=True, ncol=2)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20),fancybox=True, shadow=True, ncol=2)
        ax.grid(True)
        #ax2.grid(True)
        show()
        fig.savefig('../../img-perf/'+name+'/shuffle.pdf',dpi=400)



def powerFormater(x, pos):
    #print(x, " " , pow(2,x))
    y = pow(2,x)
    # print("y=", pow(2,x))
    if y>1 :
        return "{:1.0f}".format(y)
    else :
        return "{:1.1f}".format(y)

def acc(mat):
        k=mat[:,0]
        ratioresult=(mat[:,ACC+1])
        recall=(mat[:,ACC])
        datasetS=50000
        datasetR=datasetS
        nbknnwait=datasetR*k#20*|S|
        result=ratioresult*nbknnwait

        TP=recall*nbknnwait
        # print "TP"
        # print TP

        TN=datasetS*k-result
        # print "TN"
        # print twin
        FP=result-TP
        # print "FP"
        # print FP
        FN=nbknnwait-TP
        # print "FN"
        # print FN
        accuracy=(TP+TN)/(TP+TN+FP+FN)
        return accuracy

def accuracy(name,matrices,depart,linedeb,linefin):
    fig =figg()
    ax = fig.add_subplot(1,1,1)
    # ax2 = ax.twinx()
    cpt=0
    #ax.set_xscale('log')
    #plt.xlim(0, 512)
    #plt.ylim(0, 150.0)
    taillebar=0.25

    #ax.set_ylim(maxi+1)

    #plt.ylim(0, 1.15)

    for index in range(0,2) :
        #print("xxx " + tab2[depart+cpt])
        mat = matrices[depart+cpt]
        mat = delete(mat, range(8,size(mat[:,0])), axis=0)
        #mat = delete(mat, (0), axis=0)
        #print(mat[:,NB])
        div = 1#1000/60
        #print(mat[:,ACC])
        # xlab=mat[:,0];
        # for i in range(1,size(xlab)):
        #   xlab[i]=xlab[i]+taillebar*cpt
        # print xlab
        accuracy=acc(mat)
        mat[:,0]=log2(mat[:,0])
        ax.plot(mat[:,0],mat[:,ACC]/div,"--",
                color=colors[cpt],marker=mark[cpt],label=tab2[cpt])
        ax.plot(mat[:,0],mat[:,ACC]/div*1/(mat[:,ACC+1]/div),"-",
                color=colors[cpt],marker=mark[cpt])
        # ax2.bar(mat[:,0]+(cpt-1)*taillebar,accuracy,taillebar, color=colors[cpt],label=tab2[cpt]+" accuracy",hatch = hatches[cpt],alpha=0.3)
        cpt +=1
        print(mat[:,NB])

    ax.plot(-3,-4,"--",color="black", label= " recall")
    ax.plot(-3,-4,"-",color="black", label= " precision")
    # ax.bar(-3,-4,color="black", label= " accuracy",alpha=0.3)

    bbox(ax,2)
    ax.set_xticks([1,3,5,6,7,8,9])
    ax.set_yticks(np.arange(0.2,1.1,0.2));
    # ax2.set_yticks(np.arange(0.2,1.1,0.2));
    ax.set_xticklabels(["2","8","32","64","128","256","512"])
    ax.set_xlim(0.5,9.5);
    ax.set_ylim(0,1.1);
    # ax2.set_ylim(0,1.1);
    #ax.set_xlabel('#data by file')
    # ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
    ax.set_xlabel('k')
    ax.set_ylabel('Recall & Precision')
    # ax2.set_ylabel('Accuracy')

    grid(True)
    show()
    fig.savefig('../../img-perf/'+name+'/accuracy.pdf',dpi=400)
    print('../../img-perf/'+name+'/accuracy.pdf')


def traceK(path,name,isK):
    matrices=[]
    # tab = ["hbknnj","hbnlj","hvdknnj","hzknnj","lsh"]
    # tab2 = ["hbknnj","hbnlj","pgbj","hzknnj","rankreduce"]


    for i in tab[0:size(tab)-1] :
        label,mat = file2matrix(path+"/"+i+".txt",RATIOMEM+2,';')
        # print mat;
        matrices.append(mat)

    l,matoutput = file2matrix(path+"/outputfinal.txt",2,';')
    print matoutput


    #tracer_des_temps
    time(name,matrices,isK)
    #tracer_des_memoires
    memoire(name,matrices,matoutput)
    shuffle(name,matrices,matoutput)
    #tracer d'accuracy
    accuracy(name,matrices,0,2,2)


traceK("../surf/k","surf/k",True)
#traceK("../surf/data", "surf/data",True)