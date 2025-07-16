import streamlit as st
#导入SciPy中的beta分类函数,生成高绿分布
from scipy.stats import beta,norm
import matplotlib.pyplot as plt
import numpy as np

#运行时的配置字典,修改默认绘图样式
p = plt.rcParams
#这里的key期望的值是一个列表,是一个字体名称列表,按照顺序作为优先级依次寻找可用字体
#value为列表是防止没有可现实字体
#将新的列表赋值给value 这个列表中只有这一个可用字体
p['font.sans-serif'] = ['Roboto']
#全局字体
p['font.weight'] = 'light'
#开启坐标轴小刻度线
p['ytick.minor.visible'] = True
p['xtick.minor.visible'] = True
#打开主刻度网格
p['axes.grid'] = True
#网格颜色中等灰色
p['grid.color'] = '0.5'
#网格宽度
p['grid.linewidth'] = 0.5

def uni_normal_pdf(x,mu,sigma):
    
    coeff = 1/np.sqrt(2*np.pi)/sigma
    z = (x - mu)/sigma
    f_x = coeff*np.exp(-1/2*z**2)
    
    return f_x

x_array = np.linspace(-5,5,200)

#这里仅是将组件放置在侧边栏内.每一次调整滑块都会重跑上下全部代码
with st.sidebar:
    st.title('Univariate Gaussian distribution PDF')
    #r前缀告诉python将\后面的都当做普通字符,无转移字符. '''...'''允许允许跨多行写字符串
    st.latex(r'''{\displaystyle f(x)={\frac {1}{\sigma {\sqrt {2\pi }}}}
             e^{-{\frac {1}{2}}\left({
                 \frac{x-\mu }{\sigma}}\right){2}}}''')
    mu_input = st.slider('mu',min_value = -5.0,max_value = 5.0 , value = 0.0,step=0.2)
    sigma_input = st.slider('sigma',min_value = 0.0,max_value = 4.0,value = 1.0,step=0.1)
    
    
pdf_array = uni_normal_pdf(x_array,mu_input,sigma_input)


#图二正态分布随机数生成
random_array = np.random.normal(2,0.5,1000)
#图二叠加的伦敦pdf曲线数据生成
x_line = np.linspace(0,4,201)
y_pdf = norm.pdf(x_line,2,0.5)

#图三cdf数据生成
y_cdf = norm.cdf(x_line,2,0.5)


#绘图
fig,axs = plt.subplots(2,1,figsize = (8,10))

ax1 = axs[0]
ax1.plot(x_array,pdf_array,'b',lw = 1)

ax1.axvline(x = mu_input,c = 'r',ls = '--')
ax1.axvline(x = mu_input + sigma_input, c ='r',ls = '--')
ax1.axvline(x = mu_input - sigma_input, c = 'r',ls = '--')

#标准正态
ax1.plot(x_array,uni_normal_pdf(x_array,0,1),
        c = [0.8,0.8,0.8],lw = 1)

ax1.axvline(x = 0,c = [0.8,0.8,0.8],ls = '--')
ax1.axvline(x = 0+1,c = [0.8,0.8,0.8],ls = '--')
ax1.axvline(x = 0-1,c = [0.8,0.8,0.8],ls = '--')

ax1.set_xlim(-5,5)
ax1.set_ylim(0,1)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$f_X(x)$')
#
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
ax1.tick_params(axis = 'x',direction = 'in')
ax1.tick_params(axis = 'y',direction = 'in')


#直方图+直方图内pdf
ax2 = axs[1]

ax2.hist(random_array,bins = 20,density = True,alpha = 0.6)
ax2.plot(x_line,y_pdf,'b',lw = 1)

ax2.set_xlim(0,4)
ax2.set_ylim(0,1)

#cdf绘图
ax2.plot(x_line,y_cdf,'g--')

st.pyplot(fig)










