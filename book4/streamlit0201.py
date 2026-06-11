import streamlit as st
import numpy as np
from plotly.subplots import make_subplots #子图模块
import plotly.graph_objects as go #对象模块
import plotly.express as px #快速绘图模块


def bmatrix(a):
    """返回一个LaTeX格式的bmatrix矩阵表示形式

    :a: numpy数组
    :returns: 返回字符串形式的LaTeX bmatrix矩阵
    """
    if len(a.shape) > 2:  # 如果数组维度大于2，抛出异常
        raise ValueError('bmatrix最多只能展示二维数据')
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 移除括号并分行
    rv = [r'\begin{bmatrix}']  # LaTeX矩阵开始标记
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 拼接矩阵中的元素
    rv += [r'\end{bmatrix}']  # LaTeX矩阵结束标记
    return '\n'.join(rv)  # 返回完整的LaTeX矩阵字符串

with st.sidebar:
    num_a = st.slider('Number of rows,a:',3,6,step = 1)
    num_b = st.slider('Number of rows,b:',3,6,step = 1)
    
a = np.random.uniform(0,1,num_a).reshape((-1,1))#均匀生成随机数
a = np.round(a,1)#保留一位小数

b = np.random.uniform(0,1,num_b).reshape((-1,1))
b = np.round(b,1)

show_number = False #显示初始化

with st.sidebar:
    show_number = st.checkbox('Display values')
    

tensor_a_b = a @ b.T

st.latex('a = ' + bmatrix(a))
st.latex('b = ' + bmatrix(b))
st.latex('a \\otimes b = ab^{T}')
st.latex(bmatrix(a) + '@' + bmatrix(b.T) + '=' + bmatrix(tensor_a_b))

col1,col2,col3 = st.columns(3) #生成三个容器

with col1:
    fig_a = px.imshow(a,text_auto = show_number, #显示数字选项
                      color_continuous_scale = 'viridis',
                      aspect = 'equal')
    fig_a.update_layout(height = 400,width = 300)
    fig_a.layout.coloraxis.showscale = False
    st.plotly_chart(fig_a)
    
with col2:
    fig_b = px.imshow(b,text_auto = show_number, 
                      color_continuous_scale = 'viridis',
                      aspect = 'equal')
    fig_b.update_layout(height = 400,width = 300)
    fig_b.layout.coloraxis.showscale = False
    st.plotly_chart(fig_b)
    
with col3:
    fig_ab = px.imshow(tensor_a_b,text_auto = show_number, 
                      color_continuous_scale = 'viridis',
                      aspect = 'equal')
    fig_ab.update_layout(height = 400,width = 300)
    fig_ab.layout.coloraxis.showscale = False
    st.plotly_chart(fig_ab)