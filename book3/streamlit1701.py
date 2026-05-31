from sympy import lambdify,diff,evalf,exp
from sympy.abc import x,y,z
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

with st.sidebar:
    option_i = st.selectbox('Choose from:',
                            ['First-order approximation',
                             'Second-order approximation']
                            )
    x_0 = st.slider('Expansion point:',
                    min_value = -2.5,
                    max_value = 2.5,
                    step = 0.1
                    )
    
    
f_x = exp(-x**2)
x_array = np.linspace(-3,3,100)
f_x_fcn = lambdify(x,f_x)
f_x_array = f_x_fcn(x_array)

f_x_1_diff = diff(f_x,x)
f_x_1_diff_fcn = lambdify(x,f_x_1_diff)

f_x_2_diff = diff(f_x,x,2)
f_x_2_diff_fcn = lambdify(x,f_x_2_diff)

fig,ax = plt.subplots()
ax.plot(x_array,f_x_array,linewidth = 1.5)
ax.set_xlabel('$\it{x}$')
ax.set_ylabel('$\it{f}(\it{x})$')

y_0 = f_x.evalf(subs = {x:x_0})
x_t_array = np.linspace(x_0 - 0.5,x_0+0.5,50)

b = f_x_1_diff.evalf(subs = {x:x_0})
a = f_x_2_diff.evalf(subs = {x:x_0})

if option_i == 'First-order approximation':
    approx_f = b*(x - x_0) + y_0
    approx_f_fcn = lambdify(x,approx_f)
    approx_f_array = approx_f_fcn(x_t_array)

else:
    approx_f = a/2 * (x - x_0)**2 + b*(x - x_0) + y_0
    approx_f_fcn = lambdify(x,approx_f)
    approx_f_array = approx_f_fcn(x_t_array)
    
if type(approx_f_array) == float:
    approx_f_array = approx_f_array + x_t_array * 0
    
ax.plot(x_t_array, approx_f_array, linewidth=0.25, color='r')  # 绘制近似曲线
ax.plot(x_0, y_0, marker='.', color='r', markersize=12)  # 标记展开点
ax.grid(linestyle='--', linewidth=0.25, color=[0.5, 0.5, 0.5])  # 设置网格线
ax.set_xlim(-3, 3)  # 设置x轴范围
ax.set_ylim(-0.25, 1.25)  # 设置y轴范围
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
## 使用Streamlit显示图形 ##
st.pyplot(fig)  # 在Streamlit界面显示图形