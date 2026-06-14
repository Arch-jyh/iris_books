import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots #多子图功能
import streamlit as st

# 定义一个函数，用于返回LaTeX格式的bmatrix
def bmatrix(a):
    """返回LaTeX bmatrix
    :a: numpy数组
    :returns: 作为字符串的LaTeX bmatrix
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix最多只能显示二维数组')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']
    return '\n'.join(rv)

n = m = 20

fig = make_subplots(rows = 1,cols = 2,horizontal_spacing=0.035)

xv = []
yv = []

for k in range(-n,n+1):
    xv.extend([k,k,np.nan])
    yv.extend([-m,m,np.nan])
    
lw = 1
fig.add_trace(go.Scatter(x = xv,y = yv,mode = 'lines',line_width = lw,
                         line_color = 'red'),1,1)

xh = []
yh = []
for k in range(-m,m+1):
    #nan用于划线时候断开线段,所以用nan的地方不会将跨度很大的地方连起来
    xh.extend([-m,m,np.nan]) #相当于多次append,依次添加到末尾
    yh.extend([k,k,np.nan])
fig.add_trace(go.Scatter(x = xh,y = yh,mode = 'lines',line_width = lw,
                         line_color = 'blue'),1,1)

with st.sidebar:
    st.latex(r'''
             A = \begin{bmatrix}
             a & b \\
            c & d
            \end{bmatrix}
             ''')
             
    a = st.slider('a',-2.0,2.0,step = 0.1,value = 1.0)
    b = st.slider('b',-2.0,2.0,step = 0.1,value = 0.0)
    c = st.slider('c',-2.0,2.0,step = 0.1,value = 0.0)
    d = st.slider('d',-2.0,2.0,step = 0.1,value = 1.0)
    
theta = np.pi / 6
A = np.array([[a,b],
              [c,d]],dtype = float)

X = np.array(xv)
Y = np.array(yv)

Txvyv = A @ np.stack((X,Y))

X = np.array(xh)
Y = np.array(yh)

Txhyh = A @ np.stack((X,Y))
st.latex(bmatrix(A))

a1 = A[:,0].reshape((-1,1))
a2 = A[:,1].reshape((-1,1))

st.latex(r'''
         a_1 = Ae_1 = ''' + bmatrix(A) +
         'e_1 = ' + bmatrix(a1)
         )

st.latex(r'''
         a_2 = Ae_2 = ''' + bmatrix(A) +
         'e_2 = ' + bmatrix(a2)
         )

fig.add_trace(go.Scatter(x = Txvyv[0],y = Txvyv[1],
                         mode = 'lines',line_width = lw,
                         line_color = 'red'),1,2)

fig.add_trace(go.Scatter(x = Txhyh[0],y = Txhyh[1],
                         mode = 'lines',line_width = lw,
                         line_color = 'blue'),1,2)

fig.update_xaxes(range = [-4,4])
fig.update_xaxes(range = [-4,4])

fig.update_layout(width = 800,height = 500,showlegend = False,template = 'none',
                  #有多个子图,这里的axis2语法表示第二个子图的网格关闭
                  plot_bgcolor = 'white',yaxis2_showgrid = False,xaxis2_showgrid = False)

st.plotly_chart(fig)