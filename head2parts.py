import csv
import pprint
import math
import sys
from matplotlib import pyplot
def partszahyou(n):
    
    if l_i[3*n+1] != '' and l_i[3*n+2] != '':
        return [float(l_i[3*n+1]),float(l_i[3*n+2])]
    else:
        return [-1,-1]

args = sys.argv
soutai = []
num = args[1]
vs = []
#va = [vx,vy,v]
va = []
with open('csv/'+num+'.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    l = l[1:]

    for i in range(int(l[-1][0])):
        l_i = l[i]
        # head = partszahyou(0)
        # if head[0] == -1 or head[1] == -1: break
        chest = partszahyou(1)
        if chest[0] == -1 or chest[1] == -1: continue
        RSho = partszahyou(2)
        if RSho[0] == -1 or RSho[1] == -1: continue
        LSho = partszahyou(5)
        if LSho[0] == -1 or LSho[1] == -1: continue
        kokan = partszahyou(8)
        if kokan[0] == -1 or kokan[1] == -1: continue
        Rkn = partszahyou(10)
        if Rkn[0] == -1 or Rkn[1] == -1: continue
        Lkn = partszahyou(13)
        if Lkn[0] == -1 or Lkn[1] == -1: continue
        
        tmp1 = [round(x - y,3) for (x, y) in zip(chest,kokan)]
        tmp2 = [round(x - y,3) for (x, y) in zip(chest,RSho)]
        tmp3 = [round(x - y,3) for (x, y) in zip(chest,LSho)]
        tmp4 = [round(x - y,3) for (x, y) in zip(chest,Rkn)]
        tmp5 = [round(x - y,3) for (x, y) in zip(chest,Lkn)]
        
        leng = math.sqrt(tmp1[0]**2 + tmp1[1]**2)
        
        
        # [(chest-kokan),(chest-Rs),(chest-Ls),(kokan-Rk),(kokan-Lk)]
        soutai_i = [int(l[i][0]),[int(n*100/leng) for n in tmp1],[int(n*100/leng) for n in tmp2],[int(n*100/leng) for n in tmp3],[int(n*100/leng) for n in tmp4],[int(n*100/leng) for n in tmp5]]
        soutai.append(soutai_i)
for i in range(1,len(soutai)):
    soutai_i = soutai[i]
    soutai_i_1 = soutai[i-1]
    v_i = []
    for j in range(1,6):
        xdiff = soutai_i[j][0] - soutai_i_1[j][0]
        ydiff = soutai_i[j][1] - soutai_i_1[j][1]
        time = soutai_i[0]-soutai_i_1[0]
        v_i.append([xdiff/time,ydiff/time])
    
    vs.append(v_i)

vx = []
vy = []
vxy = []
for i in range(len(vs)):
    vx_i = 0
    vy_i = 0
    vxy_i = 0
    v_i = vs[i]
    for i in range(5):
        if v_i[i][0]**2 > 600:
            vx_i = 600
        else: vx_i = v_i[i][0]**2
        if v_i[i][1]**2 > 600:
            vy_i = 600
        else: vy_i = v_i[i][1]**2
        if vx_i + vy_i > 1000:
            vxy_i = 1000
        else: vxy_i = vx_i + vy_i
    
    vx.append(vx_i)
    vy.append(vy_i)
    vxy.append(vxy_i)
        
    va.append([vx_i,vy_i,vxy_i])



pyplot.plot(vx,marker = "o")
pyplot.savefig("plot/" + num + "/vx.png", format="png", dpi=300)
pyplot.clf()
pyplot.plot(vy,marker = "o")
pyplot.savefig("plot/" + num + "/vy.png", format="png", dpi=300)
pyplot.clf()
pyplot.plot(vxy,marker = "o")
pyplot.savefig("plot/" + num + "/vxy.png", format="png", dpi=300)
pyplot.clf()
pyplot.plot(vx,marker = "o")
pyplot.plot(vy,marker = "o")
pyplot.plot(vxy,marker = "o")
pyplot.savefig("plot/" + num + "/mix.png", format="png", dpi=300)