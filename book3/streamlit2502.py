import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def draw_vector(vector,RGB,ax):
    ax.quiver(0,0,vector[0],vector[1],
              angles = 'xy',
              scale_units = 'xy',
              scale = 1,
              color = RGB)
    
T = np.matrix([[0.7,0.2],
               [0.3,0.8]])

def bmatrix(a):
    if len(a.shape)>2:
        raise ValueError('bmatrix can at most display two dimensions')
    
    #先执行str(a)时候[[a,b],[c,d]] >>> '[[a b] \n [c d]]' 注意,变成了空格
    #splitlines将\n断开字符串变成了列表 并由\n变成的','隔开
    lines = str(a).replace('[','').replace(']','').splitlines()
    rv = [r'\begin{bmatrix}']
    #列表里面用for自动append添加
    rv += ['  ' + '&'.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']
    
    return '\n'.join(rv)

with st.sidebar:
    p = st.slider('Ratio of chickens:',
                  min_value = 0.0,
                  max_value = 1.0,
                  step = 0.05)
    
    num_steps = st.slider('Number of nights:',
                          min_value = 10,
                          max_value = 30,
                          step = 1)
    
    pi_0 = np.array([[p],
                     [1 - p]])
    
    st.latex('T = ' + bmatrix(T))
    st.latex('\pi (0) = ' + bmatrix(pi_0))
    st.latex('\pi(k + 1) = T \pi(k)')

x1 = np.linspace(-1.1,1.1,num = 201)
x2 = x1
xx1,xx2 = np.meshgrid(x1,x2)
zz = ((np.abs((xx1))**2) + (np.abs((xx2))**2))**(1./2)#

pi = pi_0

colors = plt.cm.rainbow(np.linspace(0,1,num_steps + 1))

fig,ax = plt.subplots(figsize = (10,10))

fig.patch.set_alpha(0)
ax.set_facecolor('none')

plt.plot(x1,1 - x1,color = 'k',linestyle = '--')

plt.contour(xx1,xx2,zz,levels = [1],colors = '0.5',linestyles = '--')#

for i in np.arange(0,num_steps + 1):
    draw_vector(pi / np.linalg.norm(pi),colors[i],ax)
    draw_vector(pi,colors[i],ax)
    pi = T@pi
    
ax.tick_params(left=False, bottom=False)  # 隐藏坐标轴刻度线
ax.set_xlim(-1.1, 1.1)  # 设置x轴范围
ax.set_ylim(-1.1, 1.1)  # 设置y轴范围
ax.axvline(x=0, color='0.5')  # 绘制y轴
ax.axhline(y=0, color='0.5')  # 绘制x轴
ax.spines['top'].set_visible(False)  # 隐藏上边框
ax.spines['right'].set_visible(False)  # 隐藏右边框
ax.spines['bottom'].set_visible(False)  # 隐藏下边框
ax.spines['left'].set_visible(False)  # 隐藏左边框
ax.grid(color=[0.8, 0.8, 0.8])  # 设置网格颜色
plt.xticks(np.linspace(-1, 1, 21))  # 设置x轴刻度
plt.yticks(np.linspace(-1, 1, 21))  # 设置y轴刻度

## 显示图形
st.pyplot(fig=fig)  # 使用Streamlit显示图形