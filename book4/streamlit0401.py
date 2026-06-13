import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots #plotly创建子图
import streamlit as st

def bmatrix(a):
    """返回一个LaTeX bmatrix格式的字符串
    :param a: 输入的NumPy数组
    :return: 返回LaTeX矩阵的字符串表示
    """
    if len(a.shape) > 2:  # 检查数组是否为二维
        raise ValueError('bmatrix最多只能展示二维数组')  # 如果不是二维数组，抛出异常
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 去掉数组表示中的方括号并分行
    rv = [r'\begin{bmatrix}']  # 添加LaTeX矩阵的起始标签
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 将每行元素用&连接并加上换行符
    rv += [r'\end{bmatrix}']  # 添加LaTeX矩阵的结束标签
    return '\n'.join(rv)  # 返回拼接后的字符串

n = m = 20
#horizontal_spacingu是水平间距
fig = make_subplots(rows = 1,cols = 2,horizontal_spacing = 0.035) 

xv = []
yv = []
for k in range(-n,n+1):
    xv.extend([k,k,np.nan]) #extend表示逐个添加元素到列表中
    yv.extend([-m,m,np.nan])
    
lw = 1
fig.add_trace(go.Scatter(x = xv,y = yv,mode = 'lines',
                         line_width = lw,line_color = 'red'),
              1,1)

xh = []
yh = []
for k in range(-m,m+1):
    xh.extend([-m,m,np.nan])
    yh.extend([k,k,np.nan])
fig.add_trace(go.Scatter(x = xh,y = yh,mode = 'lines',
                         line_width = lw,line_color = 'blue'),
              1,1)

with st.sidebar:
    #bmatrix告诉latex这是方括号矩阵形式
    #&表示换列,\\表示换行
    st.latex(r'''
             A = \begin{bmatrix}
             a & b\\
            c & d
            \end{bmatrix}
             ''')
    a = st.slider('a',-2.0,2.0,step = 0.1,value = 0.1)
    b = st.slider('b',-2.0,2.0,step = 0.1,value = 0.)
    c = st.slider('c',-2.0,2.0,step = 0.1,value = 0.)
    d = st.slider('d',-2.0,2.0,step = 0.1,value = 0.1)

theta = np.pi / 6

A = np.array([[a,b],
              [c,d]],dtype = float)
X = np.array(xv)
Y = np.array(yv)
Txvyv = A@np.stack((X,Y))#stack默认是按照第0维度堆叠

X = np.array(xh)
Y = np.array(yh)
Txhyh = A@np.stack((X,Y))

st.latex(r'A = ' + bmatrix(A))
a1 = A[:,0].reshape((-1,1))
a2 = A[:,1].reshape((-1,1))

#latex语法里\n换行会被当成空格 \\才是现实上的换行
st.latex(r'''
         a_1 = Ae_1 = ''' + bmatrix(A) + 'e_1 = ' + bmatrix(a1)) 
st.latex(r'''
         a_2 = Ae_2 = ''' + bmatrix(A) + 'e_2 = ' + bmatrix(a2))
st.latex(r'\begin{vmatrix} A \end{vmatrix} = ' + str(np.linalg.det(A)))

square_x = np.array([0,1,1,0])
square_y = np.array([0,0,1,1])
square_array = np.stack((square_x,square_y))

fig.add_trace(go.Scatter(x = square_x,y = square_y,fill = 'toself',line_color = 'orange'),1,1)
A_times_square_array = A @ square_array

fig.add_trace(go.Scatter(x = A_times_square_array[0,:],y = A_times_square_array[1,:],
                         fill = 'toself',line_color = 'orange'),1,2)
fig.add_trace(go.Scatter(x = Txvyv[0],y = Txvyv[1],mode = 'lines',line_width = lw,line_color = 'red'),1,2)
fig.add_trace(go.Scatter(x = Txhyh[0],y = Txhyh[1],mode = 'lines',line_width = lw,line_color = 'blue'),1,2)

fig.update_xaxes(range = [-4,4])
fig.update_yaxes(range = [-4,4])
fig.update_layout(width = 800,height = 500,showlegend = False,template = 'none', #不显示图例,不使用模板
                  #背景颜色设为白色,不显示x嗯y的网格线
                  plot_bgcolor = 'white',yaxis2_showgrid = False,xaxis2_showgrid = False)

st.plotly_chart(fig)





