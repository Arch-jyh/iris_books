import streamlit  as st
import plotly.express as px

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris


## 定义函数 bmatrix，用于生成 LaTeX 矩阵
def bmatrix(a):
    """返回一个 LaTeX 矩阵"""
    if len(a.shape) > 2:  # 检查输入是否为二维数组
        raise ValueError('bmatrix 函数最多显示二维矩阵')  # 如果不是二维，抛出异常
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 将数组转为字符串并去除括号
    rv = [r'\begin{bmatrix}']  # 开始 LaTeX 矩阵的格式
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 为每一行添加 LaTeX 格式
    rv += [r'\end{bmatrix}']  # 结束 LaTeX 矩阵的格式
    return '\n'.join(rv)  # 将所有行连接为字符串并返回

iris = load_iris()
X = iris.data
y = iris.target

feature_names = ['Sepal length,x1','Sepal width,x2',
                'Petal length,x3','Petal width,x4']

X_df = pd.DataFrame(X,columns = feature_names)

X = X_df.to_numpy()

G = X.T @ X
D,V = np.linalg.eig(G)
np.set_printoptions(suppress = True) #配置打印选项,抑制科学计数法
D = np.diag(D)

st.latex(r'G = X^T X = ' + bmatrix(G))
st.latex(r'G = V \Lambda V^T')
st.latex(r'G =' +  
         bmatrix(np.round(V,2)) + '@' + 
         bmatrix(np.round(D,2)) + '@' + 
         bmatrix(np.round(V.T,2)) #round保留二位四舍五入
         )
st.write('Mapped data:')
st.latex('Z = XV')

Z = X@V

df = pd.DataFrame(Z,columns = ['PC1','PC2','PC3','PC4'])
mapping_rule = {0:'setosa',1:'versicolor',2:'virginica'}
df.insert(4,'species',y)
df['species'] = df['species'].map(mapping_rule)

#提取特征列
features = df.columns.tolist()[:-1] #不包含类别映射

with st.expander('Mapped data'):
    st.write(df)
    
with st.expander('Heatmap'):
    fig_1 = px.imshow(df.iloc[:,0:4],
                      color_continuous_scale = 'RdYlBu_r')
    st.plotly_chart(fig_1)
    
with st.sidebar:
    st.write('2D scater plot')
    x_feature = st.radio('Horizontal axis',features)#选择特征
    y_featrue = st.radio('Vertical axis',features)
    
with st.expander('2D scatter plot'):
    fig_2 = px.scatter(df,x = x_feature,y = y_featrue,color = 'species')
    st.plotly_chart(fig_2)
    
with st.expander('3D scatter plot'):
    fig_3 = px.scatter_3d(df,
                          x = 'PC1',
                          y = 'PC2',
                          z = 'PC3',
                          color = 'species')
    st.plotly_chart(fig_3)
    
with st.expander('Pairwise scatter plot'):
    fig_4 = px.scatter_matrix(df,
                              dimensions = ['PC1','PC2','PC3','PC4'],
                              color = 'species')
    st.plotly_chart(fig_4)