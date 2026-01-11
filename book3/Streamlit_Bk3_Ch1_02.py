from mpmath import mp
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

with st.sidebar:
    
    num_digits = st.slider('Number of decimal digits:',
                           min_value = 10000,
                           max_value = 100000,
                           step = 10000)
    
    
#一位用于整数
#dps本身是截断式的,不存在四舍五入,+2是出了整数位后多加了一位,用于工程安全余量
mp.dps = num_digits + 2
pi_digits = mp.pi
pi_digits = str(pi_digits)[2:]#算上了工程安全余量
pi_digits_list = [int(x) for x in pi_digits]#已经修改为了整数

pi_digits_array = np.array(pi_digits_list)#转为array

#函数中,索引 = 数值本身,值 = 出现次数,如果没有索引为0 长度为最大值+1(算上0)
#不要和10进制混淆,显示是十进制,每个数可以用多个进制表示,所以就是单纯的计数工具.bin不是二进制的意思(计算箱的意思)
counts = np.bincount(pi_digits_array)

fig,ax = plt.subplots()

ax.barh(range(10),counts,align = 'center',
        edgecolor = '0.6')#参数可以是任何可迭代对象

ax.spines[['top','right']].set_visible(False)

ax.set_xlabel('Count')
ax.set_ylabel('Digit,0~9')
plt.yticks(range(10))#参数可以是任何可迭代对象

st.pyplot(fig)#