import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd


def bmatrix(a):
    """返回一个 LaTeX 矩阵表示"""
    if len(a.shape) > 2:  # 检查输入的数组是否为二维
        raise ValueError('bmatrix 函数最多显示二维矩阵')  # 如果不是二维数组，抛出异常
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 去掉数组的方括号并按行拆分
    rv = [r'\begin{bmatrix}']  # 开始 LaTeX 矩阵的表示
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 将每一行的元素用 LaTeX 格式化
    rv += [r'\end{bmatrix}']  # 结束 LaTeX 矩阵的表示
    return '\n'.join(rv)  # 返回拼接后的 LaTeX 字符串

with st.sidebar:
    # 在侧边栏中展示一个 LaTeX 格式的矩阵模板
    st.latex(r'''
             A = \begin{bmatrix}
    a & b\\
    c & d
    \end{bmatrix}''')

    # 为矩阵 A 的元素 a, b, c, d 创建滑块，用户可调整这些值
    a = st.slider('a', -2.0, 2.0, step=0.1, value=1.0)  # 滑块用于设置 a 的值，默认值为 1.0
    b = st.slider('b', -2.0, 2.0, step=0.1, value=0.0)  # 滑块用于设置 b 的值，默认值为 0.0
    c = st.slider('c', -2.0, 2.0, step=0.1, value=0.0)  # 滑块用于设置 c 的值，默认值为 0.0
    d = st.slider('d', -2.0, 2.0, step=0.1, value=1.0)  # 滑块用于设置 d 的值，默认值为 1.0
    
x1_ = np.linspace(-1,1,11)
x2_ = np.linspace(-1,1,11)

xx1,xx2 = np.meshgrid(x1_,x2_)
X = np.column_stack((xx1.flatten(),xx2.flatten()))

A = np.array([[a,b],
             [c,d]])

X = X @ A

color_array = np.linspace(0,1,len(X))
X = np.column_stack((X,color_array))
df = pd.DataFrame(X,columns = ['z1','z2','color'])

st.latex('A = ' + bmatrix(A))

fig = px.scatter(df,
                 x = 'z1',
                 y = 'z2',
                 color = 'color',
                 color_continuous_scale= 'rainbow')

fig.update_layout(
    autosize = False,
    width = 500,
    height = 500
    )

fig.add_hline(y = 0,line_color = 'black')
fig.add_vline(x = 0,line_color = 'black')

fig.update_xaxes(range = [-3,3])
fig.update_yaxes(range = [-3,3])

fig.update_coloraxes(showscale = False)

st.plotly_chart(fig)