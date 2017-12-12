#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

#path     = "../data/params-lsh/surf/";

rc('font', size=40)
rc('legend', fontsize=30)
rc('legend', columnspacing=1)
rc('lines', linewidth=5)
rc('lines',markersize=20)

data = np.genfromtxt('../data/params-lsh/lsh-surf-params.csv', delimiter=';',skip_header=2,skip_footer=0,
                     names=['l', 'm', 'w','hdfs','time','accuracy','ratiorecall',
                            'ratiores',	'bucket'])
print data
data['time'][:] = data['time'][:]/1000/60;
rc('lines',markersize=15)

def partie_function(num,name,mat,taillebar,msg,ok=True, label_left=True, label_right=True,ia=0,ib=6,lab='w'):

    ax = fig.add_subplot(1,3,num);
    b = ax.plot(min(data[lab][ia:ib]),-1,'--',color=colors[0],marker=mark[0],label="recall")
    ax.plot(min(data[lab][ia:ib]),-1,'--',  color="purple" ,marker=mark[2],alpha=1 ,label="precision")
    #pour la legende c'est vide sinon
    #a = ax.bar(data[lab][ia:ib]-taillebar/2.0,data['time'][ia:ib],taillebar,label="time",alpha=0.4)
    a = ax.plot(data[lab][ia:ib],data['time'][ia:ib],'-', c=colors[1],marker=mark[1],label="time",alpha=0.9)
	#grid(True)
    ax2 = ax.twinx()
    ax2.plot(data[lab][ia:ib],data['accuracy'][ia:ib],'--', c=colors[0],marker=mark[0])
    ax2.plot(data[lab][ia:ib],data['accuracy'][ia:ib]/data['ratiores'][ia:ib],'--',  color="purple" ,marker=mark[2],alpha=1 )
    ax.set_ylim([0,max(data['time'])])
    ax2.set_ylim([0,1])
    ax.set_xlabel(name)


    if label_left :
        ax.set_ylabel('Time (min)')
        #, color=colors[1])

    if label_right :
        ax2.set_ylabel('Accuracy')

    if(num > 1) :
        for tl in ax.get_yticklabels():
            tl.set_visible(False)
    if(num < 3) :
        for tl in ax2.get_yticklabels():
            tl.set_visible(False)
        #		tl.set_color(colors[1])

    if(ok):
            #ax.legend(loc='upper left',fancybox=True, shadow=True)
            #ax2.legend(loc='upper right',fancybox=True, shadow=True)

        bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="pink", ec="k", lw=2)
        leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.2),ncol=3,  fancybox=True, shadow=True)
        #[a, b], ['time','accuracy'],


    mini = min(data[lab][ia:ib])
    maxi = max(data[lab][ia:ib])
    inter=(maxi+mini)/4
    t = ax.annotate(msg, xy=(mini+inter,180), xycoords="data",
                        va="center", ha="center",
                        bbox=dict(boxstyle="round", fc="w"))
    grid(True)
    return;



#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['red','blue','green','silver','aqua','magenta','gold','black']
#-----------------------------------------------


rc('font', size=21)
rc('legend', columnspacing=1)

fig =figure(figsize=(16, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.07, top = 0.85, right=0.91,wspace=0.3)


#label,
matW = data #file2matrix(path+"W.txt",4,';')
label,matM = [data['m'][0:6],data['hdfs'][0:6]]#file2matrix(path+"M.txt",4,';')
label,matL = [data['l'][0:6],data['hdfs'][0:6]]#file2matrix(path+"L.txt",4,';')
#matW[:,0] = matW[:,0]/10
partie_function(1,"W ($*10^{7}$)",matW,1,"L=1, M=6",False, True, False,ia=0,ib=6,lab='w');
partie_function(2,"L",matL,0.8,"M=7, W=$7*10^{7}$",True, False, False,ia=12,ib=18,lab='l');
partie_function(3,"M",matM,2,"L=1, W=$7*10^{7}$",False, False, True,ia=6,ib=12,lab='m');


#plt.tight_layout(pad=4.0, w_pad=2.5, h_pad=1.0)

#-----------------------------------------------

show()
fig.savefig('../../img-perf/perso/lsh/params_surf.pdf',dpi=400)
