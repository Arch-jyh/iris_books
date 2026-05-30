import numpy as np
from sympy import lambdify,diff,exp,latex
from sympy.abc import x,y
import streamlit as st
import plotly.graph_objects as go

options = ['First-order partial derivative with respect to x1',
           'First-order partial derivative with respect to x2',
           'Second-order partial derivative with respect to x1',
           'Second-order partial derivative with respect to x2']
label = 'Choose from'

with st.sidebar:
    option_i = st.selectbox(label,options)
    
num = 301
x_array = np.linspace(-3,3,num)
y_array = np.linspace(-3,3,num)
xx,yy = np.meshgrid(x_array,y_array)

f_xy = 3 * (1 - x)**2 * exp(-(x**2) - (y + 1)**2) \
       - 10 * (x / 5 - x**3 - y**5) * exp(-x**2 - y**2) \
       - 1 / 3 * exp(-(x + 1)**2 - y**2)  # 复杂函数表达式
f_xy_fcn = lambdify([x, y], f_xy)  # 将符号函数转换为数值函数
f_xy_zz = f_xy_fcn(xx, yy)  # 计算目标函数在网格点的值

df_dx = f_xy.diff(x)  # 对 x 计算一阶偏导数
df_dx_fcn = lambdify([x, y], df_dx)  # 转换为数值函数
df_dx_zz = df_dx_fcn(xx, yy)  # 计算一阶偏导数在网格点的值

df_dy = f_xy.diff(y)  # 对 y 计算一阶偏导数
df_dy_fcn = lambdify([x, y], df_dy)  # 转换为数值函数
df_dy_zz = df_dy_fcn(xx, yy)  # 计算一阶偏导数在网格点的值

d2f_dxdx = f_xy.diff(x, 2)  # 对 x 计算二阶偏导数
d2f_dxdx_fcn = lambdify([x, y], d2f_dxdx)  # 转换为数值函数
d2f_dxdx_zz = d2f_dxdx_fcn(xx, yy)  # 计算二阶偏导数在网格点的值

d2f_dydy = f_xy.diff(y, 2)  # 对 y 计算二阶偏导数
d2f_dydy_fcn = lambdify([x, y], d2f_dydy)  # 转换为数值函数
d2f_dydy_zz = d2f_dydy_fcn(xx, yy)  # 计算二阶偏导数在网格点的值

if option_i == 'First-order partial derivative with respect to x1':
    st.latex(r'\frac{\partial{f}}{\partial{x_1}}')#显示公式
    ff = df_dx_zz
    
elif option_i == 'First-order partial derivative with respect to x2':
    st.latex(r'\frac{\partial{f}}{\partial{x_2}}')#显示公式
    ff = df_dy_zz
    
if option_i == 'Second-order partial derivative with respect to x1':
    st.latex(r'\frac{\partial^2{f}}{\partial{x_1^2}}')#显示公式
    ff = d2f_dxdx_zz
    
if option_i == 'Second-order partial derivative with respect to x2':
    st.latex(r'\frac{\partial^2{f}}{\partial{x_2^2}}')#显示公式
    ff = d2f_dydy_zz
    
    
fig_surface = go.Figure(go.Surface(#三个数值默认立体的
    x = x_array,
    y = y_array,
    z = ff,
    showscale = False,
    colorscale = 'RdYlBu_r'
    ))

fig_surface.update_layout(
    width = 800,
    height = 600
    )

st.plotly_chart(fig_surface)

fig_contour = go.Figure(data = go.Contour(#默认二维图
    z=ff,
    x = x_array,
    y = y_array,
    colorscale = 'RdYlBu_r'
    ))
fig_contour.update_layout(
    width = 600,
    height = 600
    )

st.plotly_chart(fig_contour)