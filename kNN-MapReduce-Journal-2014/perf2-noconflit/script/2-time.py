#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *
import copy

NB=0
TIME=1
RATIOMEM=5
ACC=3
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
rc('font', size=25)
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
lab = [0.12,0.25,0.5,1,2,4,8,16,32,64,128,256];


def figg():
	fig = figure( figsize=(13, 10), dpi=80)
	fig.subplots_adjust(bottom=0.12,top = 0.84, left=0.15, right=0.85,wspace=0.1,hspace=0.2)
	return fig

ANGLE=0
def bbox(ax,nb=3):
	ax.set_xticks(range(-3,10))
	ax.set_xlim(-3,8)
	ax.set_xticklabels(lab,rotation=ANGLE)
	ax.tick_params(axis='x', which='major')#, labelsize=28)
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
	fig =figg()
	plt.cla(); plt.clf();
	ax = fig.add_subplot(1,1,1)
	ax.tick_params(axis='both', which='major')
	cpt=0

	maxi=0;
	div = 1#1000/60

	for mat in matrices :
		maxi = max(maxi,max(mat[:,TIME]/div))
	# print maxi
	#ax.set_ylim(maxi+1)


	for mat in matrices :
	    div = 1#1000/60

	    ax.plot(log2(mat[:,NB]),mat[:,TIME]/div,color=colors[cpt],
	            marker=mark[cpt],label=tab2[cpt])
	    cpt += 1
	ax.grid()

	if not isK :
		ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
		ax.set_xlabel('Number of records ($*10^{5}$)')
	else :
		ax.xaxis.set_major_formatter(FormatStrFormatter(' $2^{%0.0f}*10^{5}$'))
		ax.set_xlabel('K')
	ax.set_ylabel('Time(min)')
	bbox(ax)
	keepgoodylabel(ax,matrices,TIME,div)
	ax.set_ylim(1,maxi+1)
	show()
	fig.savefig('../../img-perf/'+name+'/time.pdf',dpi=400)
	plt.close();


#----------------------------------------MEMOIRE----------------------------
def memoire(name,matrices,matoutput,isK=False):
    fig =figg()
    plt.cla(); plt.clf();
    ax = fig.add_subplot(1,1,1)
    cpt=0
    #ax.set_xscale('log')

    #plt.ylim(0, 150.0)
    taillebar=0.15

    mini = 0
    #maxi_x = 0
    maxi=0
    for mat in matrices :
        mini = min(mini,min(mat[:,0]))
        #maxi_x = max(maxi_x,max(mat[:,0]))
        maxi = max(maxi,max(mat[:,RATIOMEM]))

    xx = []
    for mat in matrices :
        #print("xxx ")
        #print(mat[:,0])
        div = 1
        index = where(mat[:,0]==96)
        if len(index[0]) :
            mat=delete(mat,index[0][0],axis=0)
        if not isK :
            mat[:,0] = log2(mat[:,0])
            xx  = mat[:,0] ;
            #error in the file, we don't add 1 for hbknnnj
            print(cpt,mat[:,RATIOMEM])
            if cpt == 4 :
                ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,5]/div,taillebar,
                  color=colors[cpt],label=tab2[cpt])
            else :
                ax.bar(mat[:,0]+taillebar*(cpt-2),mat[:,5]/div,taillebar,
                 color=colors[cpt],label=tab2[cpt])
            cpt +=1
            print("-------")
            print(mat[:,0])

	ax.set_ylim(0.1, 4.2)
	ax.yaxis.set_ticks(np.arange(0,4.5,1))
    bbox(ax)

    #ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
    ax.set_xlabel('Number of records ($*10^{5}$)')
    # ax.set_ylabel('(Intermediate + Final)/Final size')
    ax.set_ylabel('Space requirement')
    ax2=ax.twinx()
    ax2.plot(log2(matoutput[:,0]),matoutput[:,1]/1024,"--",color="black")
    ax2.set_ylabel('result size (GB)')
    ax2.yaxis.set_ticks(np.arange(0,13,3))
    ax2.set_ylim(0.1, 13)

    grid(True)
    show()
    fig.savefig('../../img-perf/'+name+'/memory.pdf',dpi=400)
    plt.close()

def powerFormater(x, pos):
	#print(x, " " , pow(2,x))
	y = pow(2,x)
	print("y=", pow(2,x))
	if y>1 :
		return "{:1.0f}".format(y)
	else :
		return "{:1.1f}".format(y)
def acc(mat):
		k=20
		ratioresult=(mat[:5,ACC+1])
		recall=(mat[:5,ACC])
		datasetS=mat[:5,0]*100000
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

def accuracyGEO(name,matrices,depart,linedeb,linefin):
	fig =figg()
	plt.cla(); plt.clf();

	ax = fig.add_subplot(1,1,1)
	cpt=0
	#ax.set_xscale('log')

	#plt.ylim(0, 150.0)
	taillebar=0.1

	#ax.set_ylim(maxi+1)

	taillebar=0.15
	# ax2=ax.twinx()
	for index in range(0,2) :

		mat = matrices[depart+cpt]
		accuracy=acc(mat)
		print mat
		mat2 = matrices[depart+cpt]
		print mat2
		div = 1
		xlab=log2(mat[:,0]);
		for i in range(1,size(xlab)):
			xlab[i]=xlab[i]+taillebar*cpt
		ax.plot(log2(mat[:5,0]),mat[:5,ACC],"--", color=colors[cpt],marker=mark[cpt],label=tab2[cpt])
		ax.plot(log2(mat2[:5,0]),mat2[:5,ACC]/(mat[:5,ACC+1]),"-", color=colors[cpt],marker=mark[cpt])

		# ax2.bar(log2(mat[:5,0])+(cpt-1)*taillebar,accuracy,taillebar, color=colors[cpt],label=tab2[cpt]+" accuracy",hatch = hatches[cpt],alpha=0.3)
		cpt +=1

	ax.plot(min(log2(mat2[:5,0])),-4,"--",color="black", label= " recall")
	ax.plot(min(log2(mat2[:5,0])),-4,"-",color="black", label= " precision")
	# ax.bar(min(log2(mat2[:5,0])),-4,color="black", label= " accuracy",alpha=0.3)

	box = ax.get_position()
	# ax.set_position([box.x0, box.y0 + box.height * 0.1,
	#                  box.width, box.height * 0.8])
	bbox(ax,2)


	#ax.xaxis.set_major_formatter(FormatStrFormatter(' $2^{%0.0f}*10^{5}$'))
	#ax.set_xlabel('#data by file')
	#ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
	ax.set_xlabel('Number of records ($*10^{5}$)')
	ax.set_ylabel('Recall & Precision')
	# ax2.set_ylabel('Accuracy')

	mini=99999
	maxi2=0
	for mat in matrices :
		mm = mat[:5,ACC]/div
		mm2= mat2[:,ACC+1]/div
		mini = min(min(mini,min(mm)),min(mm2))
		#maxi_x = max(maxi_x,max(mat[:,0]))
        maxi2 = max(max(maxi2,max(mm)),max(mm2))
	ecart=maxi2-mini
	step=round((ecart/4)*100)/100.0
	print maxi2
	ax.yaxis.set_ticks(np.arange(0.6,1.01,0.05))
	ax.set_ylim(0.8, 1.01)
	# ax2.yaxis.set_ticks(np.arange(0.6,1.01,0.05))
	# ax2.set_ylim(0.8, 1.01)
	#ax2.set_ylim(0.89, 1.01)
	ax.set_xlim(-3.2,1.2)

	grid(True)
	show()
	fig.savefig('../../img-perf/'+name+'/accuracy.pdf',dpi=400)
	#plt.close();

def shuffle(name,matrices,matoutput,isK=False):
    fig = figure( figsize=(13, 10), dpi=80)
    fig.subplots_adjust(bottom=0.12,top = 0.84, left=0.15, right=0.85,wspace=0.1,hspace=0.2)

    plt.cla(); plt.clf();
   # ax =  plt.subplot2grid((2,2),(0,0))
   # ax2 = plt.subplot2grid((2,2),(0,1))
    ax3 =  fig.add_subplot(1,1,1) #plt.subplot2grid((2,2),(1,0),colspan=3 )

    ax4 = ax3.twinx()
    cpt=0
    #ax.set_xscale('log')

    #plt.ylim(0, 150.0)
    taillebar=0.15
    matrices2=copy.deepcopy(matrices)
    mini = 0
    #maxi_x = 0
    maxi=0
    for mat in matrices :
        mini = min(mini,min(mat[:,0]))
        #maxi_x = max(maxi_x,max(mat[:,0]))
        maxi = max(maxi,max(mat[:,RATIOMEM]))

    cpt=0
    matsize=np.array([1.8,3.6,7.1,15,29,57,114,229,459,916,1800,3600]).transpose()
    matsize=matsize*1e6*2;
    matsizex=np.array([0.12,0.25,0.5,1,2,4,8,16,32,64,128,256]).transpose()

    xx = []
    taillebar=0.15
    for mat in matrices2 :
        #print("xxx ")
        #print(mat[:,0])
        #div =1e9
        print tab2[cpt]
        print mat[:,6] ,"/" , matsize[:len(mat[:,6])]
        index = where(mat[:,0]==96)
        if len(index[0]) :
            mat=delete(mat,index[0][0],axis=0)
        if not isK and cpt <4 : #ignore H-BkNNJ for this figure
            mat[:,0] = log2(mat[:,0])
            xx  = mat[:,0] ;
            #print(cpt,mat[:,RATIOMEM])
            ax3.bar(mat[:,0]+taillebar*(cpt-2),mat[:,6]/matsize[:len(mat[:,6])],taillebar,
                  color=colors[cpt],label=tab2[cpt])

            cpt +=1
            #print("-------")
            #print(mat[:,0])

    ax4.plot(log2(matsizex),matsize/1e9,"--",color="black")
    ax4.yaxis.set_ticks(np.arange(2,9,2))
    ax4.set_ylabel('|R|+|S| (GB)')

	#ax.set_ylim(0, maxi+1.2)

    #ax.set_xticks(mat[:,0]+3)
    #ax.set_xscale('log')
    #ax.set_xticks(range(-3,3))
    #ax.set_xticklabels(lab,rotation=ANGLE)



    #ax2.set_xticks(range(3,9))
    #ax2.set_xticklabels([8,16,32,64,128,256,512],rotation=ANGLE)

    # ax2.tick_params(axis='x', which='major', labelsize=24)
    # ax3.tick_params(axis='x', which='major', labelsize=24)
    # ax.tick_params(axis='x', which='major', labelsize=24)

    #ax3.legend(loc='upper center', bbox_to_anchor=(1, 1.5),
	#           fancybox=True, shadow=True, ncol=3)
    #bbox(ax3,2)

    ax3.tick_params(axis='x', which='major')#, labelsize=24)

	#ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
    ax3.set_xlabel('Number of records ($*10^{5}$)')
    # ax.set_ylabel('(Intermediate + Final)/Final size')
    #ax.set_ylabel('Communication overhead \n(GB)')

    ax3.yaxis.set_ticks(np.arange(2,8,2))

    ax3.set_ylabel('Communication overhead ratio')





    # These are in unitless percentages of the figure size. (0,0 is bottom left)

    bbox(ax3,2)
    grid(True)
    show()
    fig.savefig('../../img-perf/'+name+'/shuffle.pdf',dpi=400)
    plt.close()

#------------------selon les data
def tracedata(path,name):
	matrices=[]
	# tab = ["hbknnj","hbnlj","hvdknnj","hzknnj","lsh"]
	# tab2 = ["hbknnj","hbnlj","pgbj","hzknnj","rankreduce"]
	for i in tab :
	    label,mat = file2matrix(path+"/"+i+".txt",RATIOMEM+2,';')
	    # print mat;
	    matrices.append(mat)

	l,matoutput = file2matrix(path+"/outputfinal.txt",2,';')
	# print matoutput


	#tracer_des_temps
	#time(name,copy.deepcopy(matrices))
	#tracer_des_memoires
	shuffle(name,copy.deepcopy(matrices),matoutput)

	#memoire(name,copy.deepcopy(matrices),matoutput)

	#tracer d'accuracy
	#accuracy(name,matrices,0,2,2)
	#accuracyGEO(name,copy.deepcopy(matrices),0,2,2)


tracedata("../geo/data","geo/data")
# DO NOT USE, SEE A4-ratioByK.py
#traceK("../geo/k","geo/k",True)