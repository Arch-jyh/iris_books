import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
import streamlit as st

def bmatrix(a):
    """返回LaTeX bmatrix

    :a: numpy数组
    :returns: 作为字符串的LaTeX bmatrix
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix最多支持显示二维矩阵')  # 确保输入矩阵是二维的
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 格式化矩阵为字符串
    rv = [r'\begin{bmatrix}']  # LaTeX矩阵的开始部分
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 添加每一行数据
    rv += [r'\end{bmatrix}']  # LaTeX矩阵的结束部分
    return '\n'.join(rv)


n = m = 20
fig = make_subplots(rows = 1,cols = 2,horizontal_spacing= 0.035)

xv = []
yv = []

for k in range(-n,n+1):
    #多次append添加到末尾
    xv.extend([k,k,np.nan])
    yv.extend([-m,m,np.nan])

lw = 1
for k in range(-n,n+1):
    fig.add_trace(go.Scatter(x = xv,y = yv,mode = 'lines',line_width = lw,
                             line_color = 'red'),1,1)

xh = []
yh = []

for k in range(-n,n+1):
    #多次append添加到末尾
    xv.extend([-m,m,np.nan])
    yv.extend([k,k,np.nan])

lw = 1
for k in range(-n,n+1):
    fig.add_trace(go.Scatter(x = xh,y = yh,mode = 'lines',line_width = lw,
                             line_color = 'red'),1,1)
    

with st.sidebar:
    st.latex(r'''
             R = \begin{bmatrix}
             \cos(\theta) & -\sin(theta) \\
            \sin(\theta) & \cos(\theta)
            \end{bmatrix}
             ''')
    theta = st.slider('Theta degree',-180,180,step = 5,value = 0)
    theta = theta / 180 * np.pi
    
R = np.array([[np.cos(theta), - np.sin(theta)],
              [np.sin(theta),np.cos(theta)]],dtype = float)

X = np.array(xv)
Y = np.array(yv)
Txvyv = R @ np.stack((X,Y)) #默认是vstack

X = np.array(xv)
Y = np.array(yv)
Txhyh = R @ np.stack((X,Y))

st.latex(r'R = ' + bmatrix(R))

r1 = R[:,0].reshape((-1,1))
r2 = R[:,1].reshape((-1,1))

st.latex(r'''
         r_1 = R e_1 = '''
         + bmatrix(R) + 
         'e_1 = '
         + bmatrix(r1)
         )
st.latex(r'''
         r2 = R e_2 = '''
         + bmatrix(R) + 
         'e_2 = '
         + bmatrix(r2)
         )

st.latex(r'\begin{vmatrix} R \end{vmatrix} = ' + str(np.linalg.det(R))) #行列式

fig.add_trace(go.Scatter(x = Txvyv[0],y = Txvyv[1],
                         mode = 'lines',line_width = lw,
                         line_color = 'red'),1,2)
fig.add_trace(go.Scatter(x = Txhyh[0],y = Txhyh[1],
                         mode = 'lines',line_width = lw,
                         line_color = 'blue'),1,2)

fig.update_xaxes(range = [-4,4])
fig.update_yaxes(range = [-4,4])

fig.update_layout(width = 800,height = 500,showlegend = False,template = 'none',
                  plot_bgcolor = 'white',yaxis2_showgrid = False,xaxis2_showgrid = False)

st.plotly_chart(fig)