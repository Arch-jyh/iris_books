import streamlit as st
import plotly.graph_objects as go
import sympy
import numpy as np
from scipy.stats import multivariate_normal #多元正态分布 #可用于创建模型

# 定义一个函数，将 NumPy 数组转换为 LaTeX bmatrix 格式
def bmatrix(a):
    """返回一个 LaTeX 矩阵表示"""
    if len(a.shape) > 2:  # 如果数组维度大于2，抛出异常
        raise ValueError('bmatrix 函数最多支持二维矩阵')  
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 将数组转换为字符串并去掉方括号
    rv = [r'\begin{bmatrix}']  # LaTeX 矩阵起始
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 按行格式化
    rv += [r'\end{bmatrix}']  # LaTeX 矩阵结束
    return '\n'.join(rv)  # 返回拼接后的字符串

with st.sidebar:
    st.latex(r'''
             \Sigma = \begin{bmatrix}
             \sigma_1^2 & 
             \rho \sigma_1 \sigma_2 \\
             \rho \sigma_1 \sigma_2 & 
             \end{bmatrix}
             ''')
    st.write('$\sigma_1$')
    sigma_1 = st.slider('sigma_1',1.0,2.0,step = 0.1)
    st.write('$\sigma_2$') #
    sigma_2 = st.slider('sigma_2',1.0,2.0,step = 0.1)
    st.write('$\\rho') 
    rho_12 = st.slider('rho',-0.9,0.9,step = 0.1)
    
    
st.latex(r'''
   f(x) = \frac{1}{\sqrt{2\pi} \sigma} 
          \exp\left( -\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{\!2}\,\right)
          ''')  # 1D 正态分布公式
st.latex(r'''
   f(x) = \frac{1}{\left( 2 \pi \right)^{\frac{D}{2}} 
          \begin{vmatrix}
          \Sigma 
          \end{vmatrix}^{\frac{1}{2}}} 
          \exp\left( 
         -\frac{1}{2}
          \left( x - \mu \right)^{T} \Sigma^{-1} \left( x - \mu \right)
          \right)
          ''')  # 2D 正态分布公式
          
x1 = np.linspace(-3,3,101)
x2 = np.linspace(-3,3,101)
xx1,xx2 = np.meshgrid(x1,x2)
pos = np.dstack((xx1,xx2)) #将矩阵叠起来(101,101,2)

Sigma = [[sigma_1**2,rho_12 * sigma_1*sigma_2],
         [rho_12 * sigma_1 * sigma_2,sigma_2**2]] #协方差矩阵
rv = multivariate_normal([0,0],Sigma) #创建多元正态分布对象
PDF_zz = rv.pdf(pos) #计算网格上的概率密度

Sigma = np.array(Sigma)

D,V = np.linalg.eig(Sigma)
D = np.diag(D)

st.latex(r'''\Sigma = \begin{bmatrix}%s & %s\\%s & %s\end{bmatrix}''' 
         % (sigma_1**2, 
            rho_12 * sigma_1 * sigma_2, 
            rho_12 * sigma_1 * sigma_2, 
            sigma_2**2))
st.latex(r'''\Sigma = V \lambda V^{T}''')
st.latex(bmatrix(Sigma) + '=' + 
         bmatrix(np.around(V,decimals = 3)) + '@' + 
         bmatrix(np.around(D,decimals = 3)) + '@' + 
         bmatrix(np.around(V.T,decimals = 3))
         )

fig_surface = go.Figure(go.Surface(
    x = x1,
    y = x2,
    z = PDF_zz,
    colorscale = 'RdYlBu_r',
    ))
fig_surface.update_layout(
    autosize = False,
    width = 500,
    height = 500
    )
st.plotly_chart(fig_surface)

fig_contour = go.Figure(
    go.Contour(
        z = PDF_zz,
        x = x1,
        y = x2,
        colorscale = 'RdYlBu_r'
        )
    )
fig_contour.update_layout(
    autosize = False,
    width = 500,
    height = 500
    )

st.plotly_chart(fig_contour)