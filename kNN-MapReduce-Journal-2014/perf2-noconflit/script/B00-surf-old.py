#------------------selon K
from pylab import *
from readfile import *
from mycolor import *


NB=0
TIME=1
RATIOMEM=5
ACC=3
#-------------------------------------------------------------------------------
rc('font', size=18)
rc('legend', columnspacing=1)
rc('lines', linewidth=3)
rc('lines',markersize=8)
#tab = ["hzknnj","lsh","hvdknnj","hbnlj","hbknnj"]
tab  = ["hzknnj","lsh","hvdknnj","hbnlj","hbknnj"]
tab2 = ["H-zkNNJ","RankReduce","PGBJ","H-BNLJ","H-BkNNJ"]
#mark = ['o','d','s','*','v']
#-------------------------------------------------------------------------------

#----------------------------------------1-------


def time(name,matrices,isK=False):
    fig =figure( figsize=(12, 8), dpi=80)
    ax = fig.add_subplot(1,1,1)
    ax.tick_params(axis='both', which='major', labelsize=20)
    cpt=0

    maxi=0;
    div = 1#1000/60

    for mat in matrices :
        maxi = max(maxi,max(mat[:,TIME]/div))
    # print maxi
    #ax.set_ylim(maxi+1)

    plt.ylim(0, maxi+1)

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
    ax.set_xlabel('Number of Images (*$10^4$)')
    ax.set_ylabel('time(min)')
    box = ax.get_position()

#   box = ax.get_position()
    # ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     # box.width, box.height * 0.8])
    ax.set_xticks([1.25,2.5,5,10])
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.13),
              fancybox=True, shadow=True, ncol=5)

    #ax.set_title("time")
    #ax2.set_title("accuracy")

    #show()
    fig.savefig('../../img-perf/'+name+'/time.pdf',dpi=400)


#----------------------------------------MEMOIRE----------------------------
def memoire(name,matrices,matoutput,isK=False):
    fig =figure( figsize=(12, 8), dpi=80)
    ax = fig.add_subplot(1,1,1)
    cpt=0
    #ax.set_xscale('log')

    #plt.ylim(0, 150.0)
    taillebar=0.20

    mini = 0
    #maxi_x = 0
    maxi=0
    for mat in matrices :
        mini = min(mini,min(mat[:,0]))
        #maxi_x = max(maxi_x,max(mat[:,0]))
        #maxi = max(maxi,max(mat[:,RATIOMEM]))
        maxi = 5

    #print("maxi ")
    #print(maxi_x)
    plt.ylim(0, maxi+0.1)
    #plt.xlim(mini+2,maxi_x)
    for mat in matrices :
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
        print(mat[:,0])
        ax.bar(mat[:,0]*10+taillebar*(cpt-2),mat[:,RATIOMEM]/div+1,taillebar,color=colors[cpt],label=tab2[cpt])
        cpt +=1

        # print("-------")
        # print(mat[:,0])

    #ax.set_xticks(mat[:,0]+taillebar)
    #ax.set_xscale('log')
    # ax.set_xticks(arange(0,10,1))
    ax.set_xticks([1.25,2.5,5,10])
    ax.set_yticks(arange(0,10,1))
    ax.xaxis.set_major_formatter(FuncFormatter(floatFormatter))
    #ax.set_xticks([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
    ax.tick_params(axis='x', which='major', labelsize=20)
    box = ax.get_position()

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.13),
        fancybox=True, shadow=True, ncol=5)

    # ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
    #ax.xaxis.set_major_formatter(FormatStrFormatter('$2^{%1.1f}$'))
    #ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
    ax.set_xlabel('Number of Images (*$10^4$)')
    ax.set_ylabel('(Intermediate + Final)/Final size')
    #ax.xaxis.set_tick_params(width=5)

    ax2=ax.twinx()
    ax2.plot(matoutput[:,0]*10,matoutput[:,1]/1024/1024/1024,"--",color="black")
    ax2.set_ylabel('result size (GB)')
    #ax2.set_yticks(arange(1,12,1))

    grid(True)
    show()
    fig.savefig('../../img-perf/'+name+'/memory.pdf',dpi=400)

def floatFormatter(x, pos):
    #print(x, " " , pow(2,x))
    if x.is_integer() :
        return "{:1.0f}".format(x)
    else :
        return "{:1.2f}".format(x)

def accuracy(name,matrices,depart,linedeb,linefin):
    fig =figure( figsize=(12, 8), dpi=80)
    ax = fig.add_subplot(1,1,1)
    cpt=0
    #ax.set_xscale('log')

    #plt.ylim(0, 150.0)
    taillebar=0.1

    #ax.set_ylim(maxi+1)

    plt.ylim(0, 0.7)

    # print(matrices)
    for index in range(0,2) :
        #print("xxx " + tab2[depart+cpt])
        mat = matrices[depart+cpt]
        # print(index, mat)
        #mat = delete(mat, range(8,size(mat[:,0])), axis=0)
        #mat = delete(mat, (0), axis=0)
        #print(mat[:,NB])
        div = 1#1000/60
        #print(mat[:,ACC])
        # xlab=mat[:,0];
        # for i in range(1,size(xlab)):
        #   xlab[i]=xlab[i]+taillebar*cpt
        # print xlab
        # print(mat[:,NB])
        ax.plot(mat[:,NB]*10,mat[:,ACC]/div,"--",
                color=colors[cpt],marker=mark[cpt],label=tab2[cpt])
        cpt +=1

    box = ax.get_position()
    # ax.set_position([box.x0, box.y0 + box.height * 0.1,
    #                  box.width, box.height * 0.8])

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.13),
              fancybox=True, shadow=True, ncol=5)
    ax.xaxis.set_major_formatter(FuncFormatter(floatFormatter))



    #ax.xaxis.set_major_formatter(FormatStrFormatter(' $2^{%0.0f}*10^{5}$'))
    #ax.set_xlabel('#data by file')
    #ax.xaxis.set_major_formatter(FuncFormatter(powerFormater))
    ax.set_xticks([1.25,2.5,5,10])
    ax.set_xlabel('Number of Images (*$10^4$)')
    ax.set_ylabel('Accuracy')

    grid(True)
    show()
    fig.savefig('../../img-perf/'+name+'/accuracy.pdf',dpi=400)
    # print('../../img-perf/'+name+'/accuracy.pdf')


def traceK(path,name,isK):
    matrices=[]
    # tab = ["hbknnj","hbnlj","hvdknnj","hzknnj","lsh"]
    # tab2 = ["hbknnj","hbnlj","pgbj","hzknnj","rankreduce"]

    for i in tab[0:size(tab)-1] :
        label,mat = file2matrix(path+"/"+i+".txt",RATIOMEM+1,';')
        # print mat;
        matrices.append(mat)

    l,matoutput = file2matrix(path+"/outputfinal.txt",2,';')
    # print matoutput


    #tracer_des_temps
    time(name,matrices,isK)
    #tracer_des_memoires
    memoire(name,matrices,matoutput)
    #tracer d'accuracy
    print(matrices[1])
    accuracy(name,matrices,0,2,2)

traceK("../surf/data", "surf/data",True)