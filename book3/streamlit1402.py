import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

with st.sidebar:
    st.latex('a_k = aq^{k}')
    
    a = st.slider('a',min_value = 1,max_value = 5,step = 1)
    n = st.slider('n',min_value=20,max_value=50,step = 5)
    #默认值形参名是value
    #位置参数顺序为名称,最小值,最大值,默认值,步长
    q = st.slider('q',-2.0,2.0,0.0,0.1)
    
GP_sequence = [a*q**i for i in range(n)]
index = np.arange(1,n+1,1)

fig,ax = plt.subplots()

fig.patch.set_alpha(0)#patch是整张画布背景,设置背景可见度(透明度)
ax.set_facecolor('none')#刻度轴坐标围城的范围的背景色

plt.xlabel('Index $x$')
plt.ylabel('Term $a_k$')
plt.plot(index,GP_sequence,marker = '.',markersize = 6,linestyle = 'None')
plt.plot(index,GP_sequence,lw = 0.25,color = '0.5')

st.pyplot(fig)