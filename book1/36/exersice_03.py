#精细化构建交互式可视化
import plotly.graph_objects as go
import numpy as np
import streamlit as st
#多元正态分布对象
from scipy.stats import multivariate_normal
import plotly.express as px

st.latex(r'''{\displaystyle f_{\mathbf {X} }(x_{1},\ldots,x_{k})=
         {\frac {\exp \left(-{\frac {1}{2}}
        ({\mathbf {x} }-{\boldsymbol {\mu }})
        ^{\mathrm {T} }{\boldsymbol {\Sigma }}^{-1}
        ({\mathbf {x} }-{\boldsymbol {\mu }})\right)}
          {\sqrt {(2\pi )^{k}|{\boldsymbol {\Sigma}}|}}}}''')

def bmatrix(a):
    """返回latex形式的bmatrix
    a是numpy array
    返回值为bmatrix字符串
    """
    #验证维度,bmatrix只能打印2d矩阵
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    #字符串化后,将字符串中的[]删除,仅剩下纯数字和空白
    lines = str(a).replace('[','').replace(']','').splitlines()
    #latex矩阵环境的起始命令
    rv = [r'\begin{bmatrix}']
    #split表示按照空白符号(空格,制表符等)拆成若干元素
    #用&字符分开的元素联结起来
    #'  '表示在每个首行添加两个空格,r'\\'表示换行命令
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    #矩阵环境结束命令
    rv += [r'\end{bmatrix}']
    #用换行符将目标连接成多行文本 在他们之间插入\n换行符
    return '\n'.join(rv)


xxx1,xxx2,xxx3 = np.mgrid[-3:3:0.2,-3:3:0.2,-3:3:0.2]

with st.sidebar:
    st.title('Triariate Gaussian Distribution')
    sigma_1 = st.slider('sigma_1',min_value = 0.5,max_value = 3.0,value = 1.0,step = 0.1)
    sigma_2 = st.slider('sigma_2',min_value = 0.5,max_value = 3.0,value = 1.0,step = 0.1)
    sigma_3 = st.slider('sigma_3',min_value = 0.5,max_value = 3.0,value = 1.0,step = 0.1)
    
    rho_1_2 = st.slider('rho_1_2',min_value = -0.95,max_value = 0.95,value = 0.0,step = 0.05)
    rho_1_3 = st.slider('rho_1_3',min_value = -0.95,max_value = 0.95,value = 0.0,step = 0.05)
    rho_2_3 = st.slider('rho_2_3',min_value = -0.95,max_value = 0.95,value = 0.0,step = 0.05)
    
SIGMA = np.array([[sigma_1**2,rho_1_2*sigma_1*sigma_2,rho_1_3*sigma_1*sigma_3],
                  [rho_1_2*sigma_1*sigma_2,sigma_2**2,rho_2_3*sigma_2*sigma_3],
                  [rho_1_3*sigma_1*sigma_3,rho_2_3*sigma_2*sigma_3,sigma_3**2]])

st.latex(r'\Sigma = ' + bmatrix(SIGMA))

MU = np.array([0,0,0])

st.write(xxx1.shape)
#三个三维数组展开为一维数组,然后按照深度合并
#深度表示数据是输入几组,每有一组表示一维
pos = np.dstack((xxx1.ravel(),xxx2.ravel(),xxx3.ravel()))

st.write(pos.shape)
rv = multivariate_normal(MU,SIGMA)
PDF = rv.pdf(pos)
fig = go.Figure(data = go.Volume(
    #所有的zyz点都从3维数据中摊开,区别于ravel,前者复制内存,这个靠背内存不影响原数据
    x = xxx1.flatten(),
    y = xxx2.flatten(),
    z = xxx3.flatten(),
    #对每个点求概率,value输入值需要一维数组,对应每个点的xyz,将其展平
    value = PDF.flatten(),
    #绘制等值面最小阈值
    isomin=0,
    #等值面的最大阈值
    isomax = PDF.max(),
    colorscale = 'RdYlBu_r',
    #不透明度
    opacity = 0.1,
    #绘制的等值面数量
    surface_count = 11,))

fig.update_layout(scene = dict(
                                xaxis_title = r'x_1',
                                yaxis_title = r'x_2',
                                zaxis_title = r'x_3'),
                    width = 1000,
                    margin = dict(r = 20,b = 10,l = 10,t = 10))

st.plotly_chart(fig,theme = None,use_container_width = True)


#生成并绘制服从数据的数据和图
samples = np.random.multivariate_normal(MU,SIGMA,size = 1000)

fig2 = px.scatter_3d(
    x = samples[:,0],
    y = samples[:,1],
    z = samples[:,2],
    title="Samples from Trivariate Gaussian",
    labels={"x":"x₁","y":"x₂","z":"x₃"},
    opacity=0.3)
fig2.update_layout(width = 1000,
                    margin = dict(r = 20,b = 10,l = 10,t = 10))

st.plotly_chart(fig2,theme = None,use_container_width = True)
         








