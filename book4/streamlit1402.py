import plotly.graph_objects as go
import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
import sympy


# 定义函数 bmatrix，将 NumPy 数组转换为 LaTeX 格式的矩阵表示
def bmatrix(a):
    """返回一个 LaTeX 矩阵表示"""
    if len(a.shape) > 2:  # 检查输入是否为二维数组
        raise ValueError('bmatrix 函数最多显示二维矩阵')  # 如果不是二维，抛出异常
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 将数组转换为字符串并去掉方括号
    rv = [r'\begin{bmatrix}']  # 开始 LaTeX 矩阵的格式
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 逐行添加 LaTeX 矩阵行
    rv += [r'\end{bmatrix}']  # 结束 LaTeX 矩阵的格式
    return '\n'.join(rv)  # 返回拼接后的 LaTeX 字符串

with st.sidebar:
    st.latex(r'''
             A = \begin{bmatrix}
             a & b\\
             b & c
             \end{bmatrix}
             ''')
             
    a = st.slider('a',-2.0,2.0,step = 0.05,value = 1.0)
    b = st.slider('b',-2.0,2.0,step = 0.05,value = 0.0)
    c = st.slider('c',-2.0,2.0,step = 0.05,value = 1.0)
    
theta_array = np.linspace(0,2*np.pi,36)
X = np.column_stack((np.cos(theta_array),
                     np.sin(theta_array)))

A = np.array([[a,b],
              [b,c]])

st.latex(r'''z^Tz = 1''')
st.latex(r'''x = Az''')

st.latex('A = ' + bmatrix(A))

X_ = X @ A

x1,x2 = sympy.symbols('x1 x2')
y1,y2 = sympy.symbols('y1 y2')
x = np.array([[x1,x2]]).T #numpy支持symbol,是array装了符号 所以这里不是symbol表达式
y = np.array([[y1,y2]]).T

Q = np.linalg.inv(A @ A.T)
D,V = np.linalg.eig(Q)
D = np.diag(D)

st.latex(r'Q = \left( AA^T\right) ^ {-1} = ' + bmatrix(np.round(Q,3)))
st.latex(r'''Q = V \Lambda V^{T}''')
#around类似round基本一样,around更像numpy里面的
#python有round numpy有 np.round np.around,前者是适配了python的round的别名
st.latex(bmatrix(np.around(Q,decimals = 3)) + '=' +  
         bmatrix(np.around(V,decimals = 3)) + '@' +
         bmatrix(np.around(D,decimals = 3)) + '@' +
         bmatrix(np.around(V.T,decimals = 3))
         )

f_x = x.T @ np.round(Q,3) @ x #方程 哪怕最后只有一个元素,也按照矩阵乘法的形状保存最后的形状
f_y = y.T @ np.round(D,3) @ y

from sympy import *

st.write('The formula of the ellipose:') #标题:显示椭圆公式
st.latex(latex(simplify(f_x[0][0])) + ' = 1') #
st.write('The formula of the transformed ellipse:')
st.latex(latex(simplify(f_y[0][0])) + ' = 1')

color_array = np.linspace(0,1,len(X))
X_c = np.column_stack((X_,color_array))
df = pd.DataFrame(X_c,columns = ['x1','x2','color'])

fig = px.scatter(df,
                 x = 'x1',
                 y = 'x2',
                 color = 'color',
                 color_continuous_scale=px.colors.sequential.Rainbow)

# 设置图形布局
fig.update_layout(
    autosize=False,  # 禁用自动调整尺寸
    width=500,  # 图表宽度为 500 像素
    height=500)  # 图表高度为 500 像素

# 添加横轴和纵轴的参考线
fig.add_hline(y=0, line_color='black')  # 添加黑色的水平参考线
fig.add_vline(x=0, line_color='black')  # 添加黑色的垂直参考线
fig.update_layout(coloraxis_showscale=False)  # 隐藏颜色条
fig.update_xaxes(range=[-3, 3])  # 设置 x 轴范围
fig.update_yaxes(range=[-3, 3])  # 设置 y 轴范围

st.plotly_chart(fig)
