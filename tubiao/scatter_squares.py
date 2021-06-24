import matplotlib.pyplot as plt


x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#plt.scatter(x_values,y_values,c = (0,0.2,0.8),edgecolor = 'none',s = 40)
#颜色映射
plt.scatter(x_values,y_values,c = y_values,cmap = plt.cm.Blues,edgecolor = 'none',s = 40)
#设置图表标题，并给坐标轴加上标签
plt.title("Square numbers",fontsize = 24)
plt.xlabel("value",fontsize = 24)
plt.ylabel("Square of value",fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis = "both",which = "major",labelsize = 14)
plt.axis([0,1100,0,1100000])







plt.show()
plt.savefig('squares_plot.png',bbox_inches = 'tight')