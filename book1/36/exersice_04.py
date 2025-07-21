import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression,Ridge
import streamlit as st

p = plt.rcParams
p['font.sans-serif'] = ['Roboto']
p['font.weight'] = 'light'
p['ytick.minor.visible'] = True
p['xtick.minor.visible'] = True
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
                       value = 2,step = 1)
    alpha = st.number_input('alpha',min_value = 0.0,max_value=10.0,
                            value = 1.0,step = 0.01,format = '%.4f')
    

#创建多项式特征生成器
poly = PolynomialFeatures(degree = degree)
#将X形状变为列向量,再生成新的特征矩阵,第一个值为1表示x的0次方
X_poly = poly.fit_transform(X.reshape(-1,1))

#训练线性回归模型
poly_reg = LinearRegression()
poly_reg.fit(X_poly,y)
#用已经训练好的模型做预测,得到对应的y值
y_poly_pred = poly_reg.predict(X_poly)
#组合X和y值生成对应点数组
data_ = np.column_stack([X,y_poly_pred])
#先将二维矩阵x_array转换成多项式特征矩阵 x_array已经是二维单列矩阵了
y_array_pred = poly_reg.predict(poly.fit_transform(x_array))

#创建岭回归模型
ridge = Ridge(alpha = alpha)
ridge.fit(X_poly,y)
y_ridge_pred = ridge.predict(poly.fit_transform(x_array))


#绘制散点图
fig,ax = plt.subplots(figsize = (5,5))
ax.scatter(X,y,s = 20)
ax.scatter(X,y_poly_pred,marker = 'x',color = 'k')

ax.plot(([i for (i,j) in data_],[i for (i,j) in data]),
        ([j for (i,j) in data_],[j for (i,j) in data]),
        c = [0.6,0.6,0.6],alpha = 0.5)

ax.plot(x_array,y_array_pred,color = 'r')
ax.plot(x_array,y_ridge_pred,color = 'b')

#提取参数
coef = poly_reg.coef_
intercept = poly_reg.intercept_
#回归解析式
equation = '$y = {:.1f}'.format(intercept)#
for j in range(1,len(coef)):
    equation += ' + {:.1f}x^{}'.format(coef[j],j)
equation += '$'
equation = equation.replace('+ -','-')
ax.text(0.05,-1.8,equation)
st.write(equation)
ax.set_aspect('equal',adjustable = 'box')
ax.set_xlim(0,4)
ax.grid(False)
ax.set_ylim(-2,2)

st.pyplot(fig)




