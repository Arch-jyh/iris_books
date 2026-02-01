import numpy as np
import matplotlib.pyplot as plt
from sympy import latex,lambdify
import streamlit as st
from sympy.abc import x


def plot_secant(x0,y0,x1,y1):
    k = (y1 - y0)/(x1 - x0)
    x = np.linspace(-1,4,100)#局部变量x不影响外部的全局变量x
    secant_y_x = k*(x - x0) + y0
    plt.plot(x,secant_y_x,color = 'r',linewidth = 0.25)
    
with st.sidebar:
    x0 = st.slider('Fixed point:',min_value = 0.5,max_value = 1.5,step = 0.1)
    delta_x = st.slider('Delta x:',min_value = 0.01,max_value = 0.5,value = 0.5,step = 0.01)
    
f_x = x**2
x_array = np.linspace(-1,4,100)
f_x_fcn = lambdify(x,f_x)
y_array = f_x_fcn(x_array)

y0 = f_x_fcn(x0)
x1 = x0 + delta_x
y1 = f_x_fcn(x1)


fig,ax = plt.subplots(figsize = (8,8))

fig.patch.set_alpha(0)
ax.set_facecolor('none')

plt.plot(x_array,y_array,color = '#00448A',linewidth = 1.25)
plt.plot(x0,y0,color = '#92D050',marker = 'x',markersize = 12)
plt.plot(x1,y1,color = '#00448A',marker = 'x',markersize = 12)

plot_secant(x0,y0,x1,y1)

plt.xlabel('X')  # 设置x轴标签
plt.ylabel('$y = f(x)$')  # 设置y轴标签
ax.set_title('$f(x) = %s$' % latex(f_x))  # 设置标题显示函数表达式
ax.set_xlim(0, 2)  # 设置x轴范围
ax.set_ylim(-1, 4)  # 设置y轴范围

st.pyplot(fig)