import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st


p = plt.rcParams
p["font.sans-serif"] = ["Roboto"]
p["font.weight"] = "light"
p["ytick.minor.visible"] = False
p["xtick.minor.visible"] = False
p["axes.grid"] = True
p["grid.color"] = "0.5"
p["grid.linewidth"] = 0.5

def bmatrix(a):
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
        
    #replace是转换第一个参数成第二个参数.这里相当于删除 最后一个方法表示按照行切分,将每一行切成一个一个的字符串
    lines = str(a).replace('[','').replace(']','').splitlines()
    #rv表示返回值的命名
    #r表示python不再读取字符串中的\,但是这里LaTeX引擎还是会读取\
        #python中只有字符串内才解析'\',使用r将所有python关于\的转义解析,其他功能调用的\正常
            #转移解析属于字符串下
        #latex来自streamlit,因为需要渲染
    rv = [r'\begin{bmatrix}']
    rv += ['   ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']#
    return '\n'.join(rv)


with st.sidebar:
    st.title('三维等值面')
    #这里返回的字符串是包括\的,python没有执行
    #这个字符串bmatrix不是前端调用python,而是用python生成字符串,作用是前端的函数语法
    st.latex(r'''Q = \begin{bmatrix}
             a & b & c\\
                 b & d & e\\
                     c & e & f
                     \end{bmatrix}''')#仅仅是字符串的显示,是字母表示的矩阵形状,没有数字
                     
    a = st.slider('a', -5,5,1,1)
    b = st.slider('b', -5,5,0,1)
    c = st.slider('c', -5,5,0,1)
    d = st.slider('d', -5,5,2,1)
    e = st.slider('e', -5,5,0,1)
    f = st.slider('f', -5,5,3,1)
    
    
x = np.linspace(-2,2,21)
y = np.linspace(-2,2,21)
z = np.linspace(-2,2,21)

X,Y,Z = np.meshgrid(x,y,z)

Points = np.column_stack([X.ravel(),Y.ravel(),Z.ravel()])

Q = np.array([[a,b,c],
              [b,d,e],
              [c,e,f]])

st.latex('Q = ' + bmatrix(Q))#这里显示了实际的矩阵,有数字
fff = np.diag(Points @ Q @Points.T)#对角化,只取对角线

fig = go.Figure(data = go.Isosurface(
    x = X.flatten(),
    y = Y.flatten(),
    z = Z.flatten(),
    value = fff.flatten(),
    surface_count = 8,
    colorscale = 'RdYlBu',
    caps = dict(x_show = False,y_show = False)
))

fig.update_layout(autosize = False,
                  width = 800,height = 800,
                  margin = dict(l = 65,r = 50,b = 65,t = 90))


st.plotly_chart(fig)