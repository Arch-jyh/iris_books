import numpy as np
from sympy import lambdify,diff,exp,latex,simplify,symbols
import plotly.figure_factory as ff #快速生成特定图形
import plotly.graph_objects as go #细节控制和通用性
import streamlit as st


x1,x2 = symbols('x1 x2')
num = 301
x1_array = np.linspace(-3,3,num)
x2_array = np.linspace(-3,3,num)
xx1,xx2 = np.meshgrid(x1_array,x2_array)

f_x =  3*(1-x1)**2*exp(-(x1**2) - (x2+1)**2)\
    - 10*(x1/5 - x1**3 - x2**5)*exp(-x1**2-x2**2)\
    - 1/3*exp(-(x1+1)**2 - x2**2) 
    
f_x_fcn = lambdify([x1,x2],f_x)
f_zz = f_x_fcn(xx1,xx2)


#sympy的latex函数返回的是字符串,写下了latex语法
#st.latex仅仅做转播交给latex渲染器
    #渲染器处理自动处理字符串,有语法的直接用,没有的会转换为latex显示
st.latex('f(x_1,x_2) = ' + latex(f_x))


fig_surface = go.Figure(go.Surface(
    x = x1_array,
    y = x2_array,
    z = f_zz,
    showscale = False,#关闭颜色条
    colorscale = 'RdYlBu_r'))
fig_surface.update_layout(
    autosize = True,
    width = 800,
    height = 600)

st.plotly_chart(fig_surface)


#%%  这个表示代码元cell,用于编辑器识别,不是python语法,方便代码分块

fig_contour = go.Figure(data = 
                        go.Contour(
                            z = f_zz,
                            x = x1_array,
                            y = x2_array,
                            colorscale = 'RdYlBu_r'))
fig_surface.update_layout(
    autosize = True,
    width = 800,
    height = 600)

st.plotly_chart(fig_contour)