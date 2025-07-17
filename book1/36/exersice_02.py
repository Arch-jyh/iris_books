import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import streamlit as st
import seaborn as sns

#配置默认视图样式
#rc的意思是run commands表示配置脚本的初始化命令集初始文件,后面的params表示配置文件中的参数
p = plt.rcParams
p['font.sans-serif'] = ['Roboto']
#设置字体粗细权重,light比默认更轻
p['font.weight'] = 'light'
#控制次级刻度是否显示
p['ytick.minor.visible'] = True
p['xtick.minor.visible'] = True
p['axes.grid'] = True
p['grid.color'] = '0.5'
p['grid.linewidth'] = 0.5

with st.sidebar:
    st.title('Bivariate Gaussian Distribution')
    #质心位置
    mu_X1 = st.slider('mu_X1',min_value = -4.0,max_value=4.0,
                      value=0.0,step = 0.1)
    mu_X2 = st.slider('mu_X2',min_value = -4.0,max_value = 4.0,
                      value = 0.0,step = 0.1)
    
    #标准差
    sigma_X1 = st.slider('sigma_X1',min_value = 0.5,max_value = 3.0,
                         value = 1.0,step = 0.1)
    sigma_X2 = st.slider('sigma_X2',min_value = 0.5,max_value = 3.0,
                         value = 1.0,step = 0.1)
    #相关性系数
    rho = st.slider('rho',min_value = -0.95,max_value = 0.95,
                    value = 0.0,step = 0.05)
    
#质心
mu = [mu_X1,mu_X2]
#协方差矩阵
Sigma = [[sigma_X1**2,sigma_X1*sigma_X2*rho],
         [sigma_X1*sigma_X2*rho,sigma_X2**2]]

width = 4
x1 = np.linspace(-width,width,321)
x2 = np.linspace(-width,width,321)
xx1,xx2 = np.meshgrid(x1,x2)
xx12 = np.dstack((xx1,xx2))
bi_norm = multivariate_normal(mu,Sigma)
#二元高斯PDF
PDF_joint = bi_norm.pdf(xx12)


#生成协方差矩阵具体值
sigma_x1=1.00;sigma_x2 = 1.3;rho_x12 = -0.5
mean = [0.6,-0.6] #就是mu
cov = [[sigma_x1**2,sigma_x1*sigma_x2*rho_x12],
         [sigma_x1*sigma_x2*rho_x12,sigma_x2**2]] #是sigma
#生成的点是两列,一列x一列y
normal_joint=np.random.multivariate_normal(mean, cov,1000)


#绘制二院高斯PDF等高线
fig,ax= plt.subplots(figsize=(5,5))

plt.contourf(xx1,xx2,PDF_joint,20,cmap = 'RdYlBu_r') #20表示登高区域数量
plt.axvline(x = mu_X1,color = 'k',linestyle = '--')
plt.axhline(y = mu_X2,color = 'k',linestyle = '--')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')

st.pyplot(fig)

#使用seaborn绘制具体值的图像
#jointplot不允许位置参数,必须关键字参数
g=sns.jointplot(x=normal_joint[:,0],y=normal_joint[:,1],
                   kind='scatter',marginal_kws={'bins':20},
                   height=5)
st.pyplot(g.fig)



g = sns.jointplot(x=normal_joint[:,0],
                  y=normal_joint[:,1],
                  kind='scatter',
                  marginal_kws={'bins':20},
                  height=5)
st.pyplot(g.fig)







