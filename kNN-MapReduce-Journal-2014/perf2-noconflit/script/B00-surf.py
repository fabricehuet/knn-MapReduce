#------------------selon K
from pylab import *
from readfile import *
from mycolor import *
import copy

NB=0
TIME=1
RATIOMEM=5
ACC=3

ylabelSize=27

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

lab = [0.12,0.25,0.5,1,2,4,8]
prec=0.125
for i in range(10):
	#lab.append(prec)
	prec = prec*2
def figg():
    fig = figure( figsize=(13, 10), dpi=80)
    fig.subplots_adjust(bottom=0.12,top = 0.83, left=0.15, right=0.85,wspace=0.1,hspace=0.2)
    return fig

def time(name,matrices,isK=False):
    fig =figg();
    ax = fig.add_subplot(1,1,1)
    ax.tick_params(axis='x', which='major')#, labelsize=35)
    cpt=0

    maxi=0;
    div = 1#1000/60
    plt.xlim(1,40)
    ax.set_xscale('log')
    for mat in matrices :
        maxi = max(maxi,max(mat[:,TIME]/div))
    # print maxi
    #ax.set_ylim(maxi+1)

    plt.ylim(0, 160)#maxi+1)

    for mat in matrices :
        div = 1#1000/60

        ax.plot(mat[:,NB]*10,mat[:,TIME]/div,color=colors[cpt],
                marker=mark[cpt],label=tab2[cpt])
        cpt += 1
    ax.grid()

    # if not isK :
    #     #ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
    #     ax.set_xlabel('Number of records ($*10^{5}$)')
    # else :
    ax.xaxis.set_major_formatter(FuncFormatter(floatFormatter))
    ax.set_xlabel('Number of descriptors (*$10^5$)')
    ax.set_ylabel('Time (min)')
    box = ax.get_position()

#   box = ax.get_position()
    # ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     # box.width, box.height * 0.8])
    ax.set_xticks([1.25,2.5,5,10,20,40,80])
    ax.set_xticklabels(lab)

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20),
              fancybox=True, shadow=True, ncol=2)

    #ax.set_title("time")
    #ax2.set_title("accuracy")
    mini=99999
    maxi2=0
    for mat in matrices :
    	mm=mat[:,TIME]/div
        mini = min(mini,min(mat[:,0]))
        #maxi_x = max(maxi_x,max(mat[:,0]))
        maxi2 = max(maxi2,max(mm))
        maxi = 8.5
    ax.yaxis.set_ticks(np.arange(30,155,30))
    #show()
    fig.savefig('../../img-perf/'+name+'/time.pdf',dpi=400)
    #plt.close();


#----------------------------------------MEMOIRE----------------------------
def memoire(name,matrices,matoutput,isK=False):
    fig =figg();
    ax = fig.add_subplot(1,1,1)
    ax.tick_params(axis='x', which='major')#, labelsize=35)
    cpt=0
    #ax.set_xscale('log')

    #plt.ylim(0, 150.0)
    taillebar=0.10

    mini = 0
    #maxi_x = 0
    maxi=0
    maxi2=0
    for mat in matrices :
        mini = min(mini,min(mat[:,0]))
        #maxi_x = max(maxi_x,max(mat[:,0]))
        maxi2 = max(maxi2,max(mat[:,RATIOMEM]))
        maxi = 8.5

    #print("maxi ")
    #print(maxi_x)

    plt.ylim(0, maxi+0.5)
    matrices2=copy.deepcopy(matrices)
    #plt.xlim(mini+2,maxi_x)
    for mat in matrices2 :
        # print("xxx ") # + tab2[cpt])
        # print(mat[:,0])
        div = 1#1000/60
        # we remove the value at x=96 because
        # it does not look pretty
        # index = where(mat[:,0]==96)
        #print(index)
        # if len(index[0]) :
        #     print("Found it!")
        #     #print(mat)
        #     mat=delete(mat,index[0][0],axis=0)

        # if not isK :
        #     mat[:,0] = log2(mat[:,0])
        #+1 because it's originally intermediate/final
        # print(cpt,mat[:,RATIOMEM])
        # if cpt == 3 :
        #     ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,RATIOMEM-1]/div+1,taillebar,color=colors[cpt],label=tab2[cpt])
        #     print(cpt, mat[:,RATIOMEM-1])
        # else :
        #print(mat[:,0]*10)
        #we do logscale by hand because of a bug in bar when using logscale on x
        mat[:,0] = log(mat[:,0]*10)
        #print(mat[:,0])
        ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,RATIOMEM]/div,taillebar,color=colors[cpt],label=tab2[cpt])
        cpt +=1

        # print("-------")
        # print(mat[:,0])

    #ax.set_xticks(mat[:,0]+taillebar)
    #ax.set_xscale('log')
    #ax.set_xticks(arange(0,6,1))
    #plt.xlim(10)

    # ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
    #ax.xaxis.set_major_formatter(FormatStrFormatter('$2^{%1.1f}$'))
    #ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
    ax.set_xlabel('Number of descriptors (*$10^5$)')
    ax.set_ylabel('Space requirement')
    #ax.xaxis.set_tick_params(width=5)

    ax2=ax.twinx()
    ax2.plot(log(matoutput[:,0]*10),matoutput[:,1]/1024/1024/1024,"--",color="black")
    #ax2.set_xticks(arange(0,6,1))



    ax2.set_xticklabels(lab)

    ax2.set_ylabel('Result size (GB)')
    #ax2.set_yticks(arange(1,12,1))
    ax.set_xticks([0.22,0.91,1.60,2.30,2.99,3.68,4.22])
    #ax.set_xticks([1,3,5,6,7,8,9])

    ax.set_xticklabels(lab)
    # ax.set_yticks(arange(0,10,1))
    #ax.xaxis.set_major_formatter(FuncFormatter(floatFormatter))
    #ax.set_xticks([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
    box = ax.get_position()


    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20),
              fancybox=True, shadow=True, ncol=2)


    mini=99999
    maxi2=0
    for mat in matrices :
    	mm=mat[:,RATIOMEM]
        mini = min(mini,min(mat[:,0]))
        #maxi_x = max(maxi_x,max(mat[:,0]))
        maxi2 = max(maxi2,max(mm))
        maxi = 8.5

    ax.yaxis.set_ticks(np.arange(round(maxi2/4),9.5,round(maxi2/4)))

    mini=min(matoutput[:,1]/1024/1024/1024)
    maxi2=max(matoutput[:,1]/1024/1024/1024)
    print("MAXI2  = ", maxi2)
    ax2.yaxis.set_ticks(np.arange(threshold(maxi2/4),maxi2,threshold(maxi2/4)))
    grid(True)
    show()
    fig.savefig('../../img-perf/'+name+'/memory.pdf',dpi=400)


def factor(x):
	if(x<1):
		return x;
	else :
		return factor(x/10)

def factorn(x):
	if(x<1):
		return 1;
	else :
		return 1+ factor(x/10)

def borne(x,b):
	if(x>1):
		return null;
	if (x < b):
		return b-0.10
	else :
		return borne(x,b+0.1)

def threshold(x) :

	res = 0;
	fac = factorn(x);
	return borne(factor(x),0.20)*factorn(x)

def shuffle(name,matrices,matoutput,isK=False):
    fig =figg();
    fig.subplots_adjust(left=0.2, right=0.85)
    #ax = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(1,1,1)
    ax4=ax2.twinx()
    cpt=0
    taillebar=0.10

    mini = 0
    #maxi_x = 0
    maxi=0
    for mat in matrices :
        mini = min(mini,min(mat[:,0]))
        maxi = max(maxi,max(mat[:,RATIOMEM+1]))

    #print("maxi ")
    #print(maxi_x)

#plt.ylim(0, maxi+0.5)
    matrices2=copy.deepcopy(matrices)
    maxi=0
    div = 1e9
    matsize=np.array([16,31,63,126,251,392,1006]).transpose()
    matsize=matsize*1e6*2;
    matsizex=np.array([0.125,0.25,0.5,1,2,4,8]).transpose()

    #plt.xlim(mini+2,maxi_x)
    xx=[]
    for mat in matrices2 :
        print tab2[cpt]
        print mat[:,RATIOMEM+1] ,"/" , matsize[:len(mat[:,6])]

        mat[:,0] = log(mat[:,0]*10)
        xx=mat[:,0]
        #print(mat[:,0])
        #ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,RATIOMEM+1]/div,taillebar,color=colors[cpt],label=tab2[cpt])
        ax2.bar(mat[:,0]+taillebar*(cpt-2),mat[:,RATIOMEM+1]/matsize[:len(mat[:,6])],taillebar,color=colors[cpt],label=tab2[cpt])
        #ax.plot(mat[:,0],mat[:,RATIOMEM+1],color=colors[cpt],label=tab2[cpt])
        maxi=max(maxi,max(mat[:,RATIOMEM+1]/div))
        cpt +=1





	ax4.plot(log(matsizex)+(taillebar*22),matsize/1e9,"--",color="black")
    ax4.yaxis.set_ticks(np.arange(0.5,3,1))
    ax4.set_ylabel('|R|+|S| (GB)')

    #ax.set_xlabel('Number of descriptors (*$10^5$)')
    ax2.set_xlabel('Number of descriptors (*$10^5$)')
    #ax.set_ylabel('Communication overhead \n (GB)')
    #ax.set_ylabel('CO (GB)')
    ax2.set_ylabel('Communication Overhead ratio', fontsize=ylabelSize)

#    ax.set_xticks([0.22,0.91,1.60,2.30,2.99,3.68,4.22])
#    ax.set_yticks(np.arange(0.8,3.7,0.8))
#
#    ax.set_xticklabels(lab)
#    ax.grid(True)

#    ax.tick_params(axis='x', which='major', labelsize=35)
    ax2.set_xticks([0.22,0.91,1.60,2.30,2.99,3.68,4.22])
    ax2.set_yticks(np.arange(1,5,1))
    ax2.set_xticklabels(lab)
    ax2.tick_params(axis='x', which='major')#, labelsize=35)


    ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20),
          fancybox=True, shadow=True, ncol=2)

    ax2.grid(True)
    show()
    fig.savefig('../../img-perf/'+name+'/shuffle.pdf',dpi=400)


def floatFormatter(x, pos):
    #print(x, " " , pow(2,x))
    if x.is_integer() :
        return "{:1.0f}".format(x)
    else :
        return "{:1.2f}".format(x)


def acc(mat):
		k=20
		ratioresult=(mat[:5,ACC+1])
		recall=(mat[:5,ACC])
		datasetS=mat[:5,0]*100000
		datasetR=datasetS
		nbknnwait=datasetR*k#20*|S|
		result=ratioresult*nbknnwait

		TP=recall*nbknnwait
		#print "TP"
		#print TP

		TN=datasetS*k-result
		#print "TN"
		#print TN
		FP=result-TP
		#print "FP"
		#print FP
		FN=nbknnwait-TP
		#print "FN"
		#print FN
		accuracy=(TP+TN)/(TP+TN+FP+FN)
		return accuracy


def accuracy(name,matrices,depart,linedeb,linefin):
    fig =figg();
    ax = fig.add_subplot(1,1,1)
    #ax2=ax.twinx()
    cpt=0
    #ax.set_xscale('log')

    #plt.ylim(0, 150.0)
    taillebar=0.15

    #ax.set_ylim(maxi+1)

    plt.ylim(0, 1.1)
    # print(matrices)
    for index in range(0,2) :
        #print("xxx " + tab2[depart+cpt])
        mat = matrices[depart+cpt]
        mat2 = matrices[depart+cpt]
        #print(index, mat)
        mat = delete(mat, range(4,size(mat[:,0])), axis=0)
        #mat = delete(mat, (0), axis=0)
        #print(mat[:,NB])
        div = 1#1000/60
        #print(mat[:,ACC])
        # xlab=mat[:,0];
        # for i in range(1,size(xlab)):
        #   xlab[i]=xlab[i]+taillebar*cpt
        #print "ff"
        #print(log2(mat[:,NB]))
        accuracy=acc(mat)

        ax.plot(log2(mat[:,NB]),mat[:,ACC]/div,"--",
                color=colors[cpt],marker=mark[cpt],label=tab2[cpt])
        ax.plot(log2(mat[:,NB]),(mat[:,ACC]/div)*(1/mat[:,ACC+1]/div),
                color=colors[cpt],marker=mark[cpt], )
       # ax2.bar(log2(mat[:,NB])+(cpt-1)*taillebar,accuracy,taillebar, color=colors[cpt],label=tab2[cpt]+" accuracy",hatch = hatches[cpt],alpha=0.3)
        #ax.plot(mat[:,NB]*10,1-mat[:,13],":o",
        #        color=colors[cpt],marker=mark[cpt])
        cpt +=1
    ax.plot(min(log2(mat[:,NB])),-4,"--",color="black", label= " recall")
    ax.plot(min(log2(mat[:,NB])),-4,"-",color="black", label= " precision")
    # ax.bar(min(log2(mat[:,NB])),-4,color="black", label= " accuracy",alpha=0.3)


    #ax.plot(min(mat[:,NB]*10),min(mat[:,ACC+1]/div),"-",color="black",label="recall")
    #ax.plot(min(mat[:,NB]*10),min(mat[:,ACC+1]/div),":o",color="black",label="1 - errorratio")


    box = ax.get_position()
    # ax.set_position([box.x0, box.y0 + box.height * 0.1,
    #                  box.width, box.height * 0.8])

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20),
              fancybox=True, shadow=True, ncol=2)
    ax.set_xticks(np.arange(-3,1))
    # ax2.set_xticks(np.arange(-3,1))
    # ax2.set_xlim(-3.2,0.2)

    ax.set_xticklabels(lab)
    ax.grid(True)

    ax.tick_params(axis='x', which='major')#, labelsize=28)

    #ax.xaxis.set_major_formatter(FormatStrFormatter(' $2^{%0.0f}*10^{5}$'))
    #ax.set_xlabel('#data by file')
    #ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
    #ax.set_xticks([1.25,2.5,5,10,20,40,80])
    #ax.set_xlim(1.15,80.5);
    ax.set_xticklabels(lab)
    ax.set_xlabel('Number of descriptors (*$10^5$)')
    ax.set_ylabel('Recall & Precision')
   # ax2.set_ylabel('Accuracy')

    #maxi=max(mat[:,ACC]/div)
    maxi=1
    ax.yaxis.set_ticks(np.arange(0.1,maxi+0.2,0.2))
    # ax2.yaxis.set_ticks(np.arange(0.1,maxi+0.2,0.2))
    ax.set_ylim(0,0.65);
    #ax2.set_ylim(0,0.65);

    grid(True)
    show()
    fig.savefig('../../img-perf/'+name+'/accuracy.pdf',dpi=400)
    # print('../../img-perf/'+name+'/accuracy.pdf')


def traceK(path,name,isK):
    matrices=[]
    # tab = ["hbknnj","hbnlj","hvdknnj","hzknnj","lsh"]
    # tab2 = ["hbknnj","hbnlj","pgbj","hzknnj","rankreduce"]

    cpt = 0;
    for i in tab[0:size(tab)-1] :
    	if( cpt <2 ) :
        	label,mat = file2matrix(path+"/"+i+".txt",14,';')
        	matrices.append(mat)
        else :
        	label,mat = file2matrix(path+"/"+i+".txt",RATIOMEM+2,';')
        # print mat;
        	matrices.append(mat)
       	cpt += 1;

    l,matoutput = file2matrix(path+"/outputfinal.txt",2,';')
    # print matoutput


    #tracer_des_temps
    time(name,matrices,isK)
    #tracer_des_memoires
    memoire(name,matrices,matoutput)
    shuffle(name,matrices,matoutput)
    #tracer d'accuracy
    #print(matrices[1])
    accuracy(name,matrices,0,2,2)

traceK("../surf/data", "surf/data",True)
