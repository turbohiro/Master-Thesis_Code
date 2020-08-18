from PSO import PSO
from DE import DE
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


dim = 3
size = 200
iter_num = 200
x_max = 5
max_vel = 0.05
a = [2.0543,4.1446,6.1995,8.2433,10.332]
b = [1.6006,2.7859,4.4384,5.6575,7.8381]
c = [5.5833,6.5566,8.2199,8.9066,9.8766]

pso = PSO(dim, size, iter_num, x_max, max_vel)
fit_var_list1, best_pos1 = pso.update()
print("PSO最优位置:" + str(best_pos1))
print("PSO最优解:" + str(fit_var_list1[-1]))
#plt.plot(np.linspace(0, iter_num, iter_num), fit_var_list1, c="R", alpha=0.5, label="PSO")
print(fit_var_list1)

#de = DE(dim, size, iter_num, -x_max, x_max)
#fit_var_list2, best_pos2 = de.update()
#print("DE最优位置:" + str(best_pos2))
#print("DE最优解:" + str(fit_var_list2[-1]))
#plt.plot(np.linspace(0, iter_num, iter_num), fit_var_list2, c="G", alpha=0.5, label="DE")


sns.set_style('white')
print('画出训练结果...')
font = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}
fig,ax = plt.subplots(figsize = (12,8))
ax.plot(np.linspace(0, iter_num, iter_num), fit_var_list1, c="R", alpha=0.5, linewidth = 4, label="PSO")
plt.ylabel('Fitness of DPF soot loading',font)
plt.xlabel('Iterations',font)
plt.xticks(fontsize=14,fontweight='normal') #默认字体大小为10
plt.yticks(fontsize=14,fontweight='normal')
ax.set_ylim(0.01, 1.0)
plt.grid(linestyle = '--')     # 添加网格线
plt.title('DPF soot loading fitness in PSO',font)
plt.savefig('9test2.jpg',dpi=600, bbox_inches = 'tight')
plt.legend(loc='best',prop = font)
plt.show()