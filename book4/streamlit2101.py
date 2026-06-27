import streamlit as st
import plotly.graph_objects as go
import sympy
import numpy as np

def bmatrix(a):  # 定义一个函数，将 NumPy 数组转换为 LaTeX bmatrix 格式的字符串
    """返回一个 LaTeX 矩阵表示"""
    if len(a.shape) > 2:  # 如果输入数组维度大于 2，抛出异常
        raise ValueError('bmatrix 函数只支持二维矩阵')  
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 将数组转换为字符串并移除方括号
    rv = [r'\begin{bmatrix}']  # LaTeX 矩阵开始符号
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 按行格式化
    rv += [r'\end{bmatrix}']  # LaTeX 矩阵结束符号
    return '\n'.join(rv)  # 返回拼接后的 LaTeX 字符串

with st.sidebar:
    st.latex(r'''A = \begin{bmatrix} a & b \\ b & c \end{bmatrix}''')
    st.latex(r'''f(x_1,x_2) = ax_1^2 + bx_1x_2 + cx_2^2''')
    a = st.slider('a',-2.0,2.0,step = 0.1)
    b = st.slider('b',-2.0,2.0,step = 0.1)
    c = st.slider('c',-2.0,2.0,step = 0.1)
    
x1_ = np.linspace(-2,2,101)
x2_ = np.linspace(-2,2,101)
xx1,xx2 = np.meshgrid(x1_,x2_)

x1,x2 = sympy.symbols('x1 x2')
A = np.array([[a,b],
              [b,c]])

D,V = np.linalg.eig(A)#计算特征值和特征向量
D = np.diag(D)

#%s是字符串格式显示,%d是整数格式显示
st.latex(r'''A = \begin{bmatrix}%s & %s\\%s & %s\end{bmatrix}''' % (a,b,b,c))
st.latex(r'''A = V \Lambda V^{T}''')
st.latex(bmatrix(A) + '=' + bmatrix(np.around(V,decimals = 3)) + '@' \
+ bmatrix(np.around(D,decimals =3))+'@'+bmatrix(np.around(V.T,decimals = 3)))
    
x = np.array([[x1,x2]]).T
f_x = a * x1**2 + 2*b*x1*x2 + c*x2**2
st.latex(r'''f(x_1,x_2) = ''')
st.write(f_x)

f_x_fcn = sympy.lambdify([x1,x2],f_x)
ff_x = f_x_fcn(xx1,xx2)

fig_surface = go.Figure(go.Surface(
    x = x1_,
    y = x2_,
    z = ff_x,
    colorscale = 'RdYlBu_r'
    ))
fig_surface.update_layout(
    autosize = False,
    width = 500,
    height = 500
    )
st.plotly_chart(fig_surface)

fig_contour = go.Figure(
    go.Contour(
        z = ff_x,
        x = x1_,
        y = x2_,
        colorscale = 'RdYlBu_r'
        ))
fig_contour.update_layout(
    autosize=False,  # 禁用自动调整尺寸
    width=500,  # 设置图表宽度为 500 像素
    height=500)  # 设置图表高度为 500 像素
st.plotly_chart(fig_contour)  # 在 Streamlit 页面上显示 2D 等高线图