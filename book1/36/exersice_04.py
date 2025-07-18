import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import streamlit as st

p = plt.rcParams
p['font.sans-serif'] = ['Roboto']
p['font.weight'] = 'light'
p['ytick.minor.visble'] = True
p['xtick.minor.visble'] = True
p['axes.grid'] = True
p['grid.color'] = '0.5'
p['grid.linewidth'] = 0.5


#生成随机数据
np.random.seed(0)
num = 30
#氛围内等概率抽取数字
X = np.random.uniform(0,4,num)
#最后加上的是正态分布形式的抽取数字 均值为0标准差为1
#代码对X进行操作就是最整个数组操作,加上的也是相同大小的数组,是数组维度所以不需要add
y = np.sin(0.4*np.pi * X) +0.4 * np.random.randn(num)
#仅仅接收一个参数tup
data = np.column_stack([X,y])

#-1表示自动计算行的数量,1表示一列 变成了101行1列的二维数据
x_array = np.linspace(0,4,101).reshape(-1,1)
degree_array = [1,2,3,4,7,8]

with st.sidebar:
    st.title('Polynomial Regression')
    degree = st.slider('Degree',
                       min_value = 1,
                       max_value = 9,
                       value = 2,stap = 1)
    

fig,ax = plt.subplots(figsize = (5,5))

#创建对象
poly = PolynomialFeatures(degree = degree)
#将X形状变为列向量,再生成新的特征矩阵,第一个值为1表示x的0次方
X_poly = poly.fit_transform(X.reshape(-1,1))

#训练线性回归模型
poly_reg = LinearRegression()
poly_reg.fit(X_poly,y)
y_poly_pred = poly_reg.predict(X_poly)
data_ = np.column_stack([X,y_poly_pred])

y_array_pred = poly_reg.predict(poly.fit_transform(x_array))









