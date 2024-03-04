import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
def q(ts, u, st, su):#ts=y, u=x, y=ax+b, st = dy, su=dx
    tu = np.mean(ts*u)
    uu = np.mean(np.square(u))
    tt = np.mean(np.square(ts))
    a = (tu-np.mean(ts)*np.mean(u))/(uu-np.mean(u)**2)
    sa=sqrt((tt-np.mean(ts)**2)/(uu-np.mean(u)**2)-a**2)
    sa/=sqrt(len(ts))
    b = np.mean(ts) - a*np.mean(u)
    ssa = a*(np.mean(st)/np.mean(ts)+np.mean(su)/np.mean(u))
    s= sqrt(sa**2+ssa**2)
    sb = np.mean(st) + s*np.mean(u) +np.mean(su)*a
    return a, b, s, sb

def latex(arr, r=3):
    arr = np.round(np.array(arr), r)
    for line in arr:
        ll = ''
        for a in line:
            ll+='& ' +str(a)
        print(ll+' \\\ \\hline')
    print()
m = 0.001*np.array([1285.6, 236.6, 412.9, 587.6, 645.3, 1161.4, 412.9, 236.2, 934.2, 174.7, 1470.6, 996.6, 185., 351.4, 536.4, 477.4, 460.2, 361.7, 234.4, 1172., 1346.7, 1531.7, 819.9, 1104.5])
Lambda = np.array([1.54, 1.24, 1.28, 1.35, 1.35, 1.58, 1.33, 1.29, 1.43, 1.24, 1.59, 1.45, 1.24, 1.28, 1.32, 1.31, 1.3, 1.28, 1.35, 1.5, 1.54, 1.61, 1.29, 1.45])
e = np.array([17.6, 15.9, 11.2, 9.2, 30.8, 38, 18.4, 29.5])
de = np.array([0, 0.8, 0, 0.4, 0.4, 0.5, 1.7, 0])
de = np.sqrt(0.01+de**2)
u = np.array([1.9, 1.86, 1.79, 1.72, 2.17, 2.27, 1.96, 2.12])
t1 = np.array([52.5, 64.5, 72.5, 81, 91, 107, 123, 147])
u1 = 2.27
e01 = -84
e1 = -np.array([47.2, 50.4, 51.2, 52, 55.2, 58.4, 61.6, 64.8])-e01
t2 = np.array([113, 123, 141, 150, 161, 172, 135, 183])
u2 = 1.96
e02 = -73.6
e2 = -np.array([56, 57.6, 58.4, 59.2, 60.8, 60.8, 57.6, 61.6])-e02
t3 = np.array([70.5, 80.5, 92, 100, 110, 120, 131, 140, 160, 190])
u3 = 2.12
e03 = -66.4
e3 = -np.array([40.8, 43.2, 44.8, 46.4, 47.2, 48, 48.8, 53.6, 54.4, 55.2])-e03
dm = 0.1*0.001
g = 9.8
dg = 0.02
f = m*g
df = dm*g+dg*m
length = 10
dlength = 0.05
dlambda = dlength*(1+Lambda)/length
lambda_ = Lambda-1/Lambda**2
dlambda_ = dlambda*(1+2/Lambda**3)
klambda, lambda0, dklambda, dlambda0 = q(f, Lambda, df, dlambda)
klambda_, lambda_0, dklambda_, dlambda_0 = q(f, lambda_, df, dlambda_)
du = dlength*(1+2/u**3)
A = length*(klambda_*(u**2+2/u)/2 + lambda_0*u)/100
dA = A*dlength/length + dklambda_*(u**2+2/u)/2*length + (u*du+du/u**2)*klambda_*length + dlambda_0*u*length + du*length*lambda_0
dA /= 100
k = 200
Te = e/k
dTe = de/k
kTA, bTA, dkTA, dbTA = q(Te, A, dTe, dA)
lnT1 = np.log(e1/k)
lnT2 = np.log(e2/k)
lnT3 = np.log(e3/k)
dlnT1 = 0.1/e1/k
dlnT2 = 0.1/e2/k
dlnT3 = 0.1/e3/k
klnT1, blnT1, dklnT1, dblnT1 = q(lnT1, t1, dlnT1, np.repeat(0.5, len(t1)))
klnT2, blnT2, dklnT2, dblnT2 = q(lnT2, t2, dlnT2, np.repeat(0.5, len(t2)))
klnT3, blnT3, dklnT3, dblnT3 = q(lnT3, t3, dlnT3, np.repeat(0.5, len(t3)))

table1 = [m, f, df, Lambda, dlambda]
table11 = []
table12 = []
for arr in table1:
    table11.append(arr[0:10])
    table12.append(arr[10:])
latex(table11)
latex(table12)
table2 = [u, e, de, 1000*Te, 1000*dTe]
latex(table2, 1)
latex([e1/k, e2/k, e2/k])
tablelambda = [[klambda, lambda0, dklambda, dlambda0], [klambda_, lambda_0, dklambda_, dlambda_0]]
latex(tablelambda)
tableT = [[klnT1, blnT1, dklnT1, dblnT1], [klnT2, blnT2, dklnT2, dblnT2], [klnT3, blnT3, dklnT3, dblnT3]]
latex(tableT, 6)
fig, ax = plt.subplots()

def plotim(ax, k, b, xdata, ydata, dx, dy, color='blue', label=''):
    xmin = np.min(xdata)
    xmax = np.max(xdata)
    deltax = xmax-xmin
    zapas = deltax/5
    x = np.linspace(xmin-zapas, xmax+zapas, 10)
    y = k*x+b
    ax.plot(x, y, color=color, label=label)
    ax.errorbar(xdata, ydata, xerr=dx, yerr=dy, color=color, marker='o', ls='none', markersize=3)
    return ax
ax = plotim(ax, kTA, bTA, A, Te, dA, dTe, label=f'$\Delta T$ = {round(kTA, 3)}$A$ +{round(bTA, 3)}')
#ax = plotim(ax, klambda_, lambda_0, lambda_, f, dlambda_, df, color='g', label=f'$f$ = {round(klambda_, 3)}$(\lambda+1/\lambda^2)$ + {round(lambda_0, 3)}')
plt.xlabel("A, J")
plt.ylabel("$\Delta T$, mK")
plt.legend(loc=2)
plt.xticks(np.linspace(-0.5, 2, 11))
plt.yticks(np.linspace(0, 200., 11)/1000, np.linspace(0, 200, 11).astype(int))
plt.grid()
plt.show()
ts = np.array([270.9, 214, 162.2])/1000
dts = np.array([3.9, 10, 4.9])/1000
As = np.array([A[-3], A[-1], A[-2]])
latex([du],2)
dAs = np.array([dA[-3], dA[-1], dA[-2]])
kk, bb, dkk, dbb = q(As, ts, dAs, dts)
print(kTA, bTA, dkTA, dbTA)
#fig1, ax1 = plt.subplots()
'''ax.plot(x, y1, color='blue', label=f"Max q: $\Delta T_0$={round(a1, 4)}$N$+{round(b1, 4)}")
plotim()
plt.xlabel("$q$, 100л/с")
plt.ylabel("$\\alpha$, 10мВт/К")
plt.legend(loc=2)
plt.xticks(np.linspace(0, 0.2, 21), (100*np.linspace(0, 0.2, 21)).astype(int))
plt.yticks(np.linspace(0.00, 250, 26), (np.linspace(0, 25, 26)).astype(int))
plt.grid()
print(ks, dks, bs, sb)
plt.show()'''