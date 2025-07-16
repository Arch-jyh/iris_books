import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import streamlit as st

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





















