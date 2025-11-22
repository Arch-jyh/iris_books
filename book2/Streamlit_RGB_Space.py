#导入整个对象系统,用go作为建成
import plotly.graph_objects as go
import numpy as np
#创建webapp的库
import streamlit as st

with st.sidebar:
    st.title('RGB色彩空间')
    num = st.slider('颗粒度',5,15,8,1)
    
    
Red = np.linspace(0,255,num)
Green = np.linspace(0,255,num)
Blue = np.linspace(0,255,num)


RRR,GGG,BBB = np.meshgrid(Red,Green,Blue)
colors_rgb = np.column_stack((RRR.ravel(),
                              GGG.ravel(),
                              BBB.ravel()))

#*是解包操作,只解包最外层
#zip按照索引对其取出同索引的位置元素再聚齐为数组
r_values,g_values,b_values = zip(*colors_rgb)

#创建交互式图像,不是matplotlib
fig = go.Figure()

#不同于add_subplot,这里是往fig中添置数据,的意思.任何绘图,点线面,轴等都是数据
#叫trace的原因是每一次都是数据都是一个轨迹,多个轨迹可以叠加在一起
fig.add_trace(go.Scatter3d(
    x = r_values,
    y = g_values,
    z = b_values,
    mode = 'markers',#画点
    marker = dict(#定义点的样式,用点的属性字典
        color = colors_rgb,
        size = 6
        )
    ))#


fig.update_layout(#调整布局
                  #使用dict()是创建新字典的意思,和另一个创建字典的语法等同
                  #这个创建字典是函数形式
    scene = dict(#配置坐标系位置,相当于axes
        xaxis = dict(title ='Red'),#设置图的外边框
        yaxis = dict(title = 'Green'),
        zaxis = dict(title = 'Blue'),
        ),
    margin = dict(l = 0,r = 0,b = 0,t = 0)#控制留白
    )
fig.layout.scene.camera.projection.type = 'orthographic'
st.plotly_chart(fig)