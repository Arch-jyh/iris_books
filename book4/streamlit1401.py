import numpy as np
import streamlit as st
import time

A = np.matrix([[0.7,0.2],
               [0.3,0.8]])

with st.sidebar:
    pi_0_chicken = st.slider('Ratio of chicken:',
                             0.0,1.0,step = 0.1)
    pi_0_rabbit = 1 - pi_0_chicken
    st.write('Ratio of rabbit:' + str(round(pi_0_rabbit,1)))
    
    num_iterations = st.slider('Number of nights:',
                               20,100,step = 5)
    

progress_bar = st.sidebar.progress(0) #初始化进度条为0%
status_text = st.sidebar.empty()

last_rows = np.array([[pi_0_chicken,pi_0_rabbit]])

chart = st.line_chart(last_rows) #将初始状态绘制到图上

for i in range(1,num_iterations):
    last_status = last_rows[-1,:]
    new_rows = last_status @ A.T
    percent = (i + 1) * 100 / num_iterations
    
    status_text.text('%i%% Complete' % percent) #旧的表达形式 类似%d 两个%%表示输出数转为真的百分比
    chart.add_rows(new_rows)#根据列绘制折线图,所以数据需要的是2D的,这里是往已有数据里面添加行
    progress_bar.progress(int(percent)) #int接收0-100 float接收0.0-1.0
    last_rows = new_rows
    time.sleep(0.1) #这里暂停执行0.1秒
    
progress_bar.progress(0)
