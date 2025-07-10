# =============================================================================
# 产生行注释模板
# =============================================================================
#%%导入库
# =============================================================================
# 导入库
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%%等差数列
# =============================================================================
# 等差数列
# =============================================================================
a0 = 1 #首项
n = 10 #项数
d = 2 #公差

#第一个参数为首项,第二个参数为终止值(不强制包括这个值),这里的a0+n*d是确保生成n项,第三个参数为步长
a_array = np.arange(a0, a0 + n*d, d)
print('打印等差数列:');print(a_array)

fig = plt.figure(figsize =(8,8))
plt.scatter(np.arange(n),a_array)
plt.title('Arithmotic Progression')
plt.xlabel('Index, $n$')
plt.ylabel('Value, $a_n$')
plt.show()
#%%二元函数
# =============================================================================
# 二元函数
# =============================================================================

x1_array = np.linspace(-3,3,301)
x2_array = np.linspace(-3,3,301)
xx1,xx2 = np.meshgrid(x1_array,x2_array)

#二元函数曲面数据
ff = xx1*np.exp(-xx1**2 - xx2**2)

#可视化
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(projection = '3d')
#绘制二元函数网格面
#stride参数控制绘制网格线密度
ax.plot_wireframe(xx1,xx2,ff,rstride = 10,cstride = 10)
plt.show()

#%%
# =============================================================================
# 鸢尾花数据
# =============================================================================

#加载数据集
iris_df = sns.load_dataset('iris')
#显示数据集前五行
print('打印鸢尾花数据前五行');print(iris_df.head())

#%%
fig,ax = plt.subplots(figsize = (8,8))
#sns可以绘制在plt的ax上 
#seborn是另一个封装在matplotlib的高级绘图库
ax = sns.scatterplot(data = iris_df,x = 'sepal_length',
                     y = 'sepal_width',hue = 'species')

ax.set_xlabel('Sepal length (cm)')
ax.set_ylabel('Sepal width (cm)')
#配置指定刻度
ax.set_xticks(np.arange(4,8+1,step = 1))
ax.set_yticks(np.arange(1,5+1,step = 1))
#强制横纵轴比例缩放
ax.axis('scaled')
ax.grid(linestyle = '--',linewidth = 0.25,color = [0.7,0.7,0.7])
ax.set_xbound(lower = 4,upper = 8)
ax.set_ybound(lower = 1,upper = 5)              