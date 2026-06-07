import numpy as np
import plotly.graph_objects as go
import streamlit as st

with st.sidebar:
    num_toss = st.slider('Number of toss',
                         min_value = 50,
                         max_value = 200,
                         step = 1)
    rnd_seed = st.slider('Random seed number',
                         min_value = 0,
                         max_value = 100,
                         step = 1)
    
np.random.seed(rnd_seed)

toss = np.random.randint(low = 0,high = 2,size = (num_toss,1))

iteration = np.arange(1,num_toss + 1)
cum_mean = np.cumsum(toss) / iteration

scatter_fig = go.Figure()

scatter_fig.add_trace(go.Scatter( #trace表示一组数据
    x = iteration[toss.flatten() == 1],
    y = toss[toss == 1].flatten(),
    mode = 'markers',
    marker = dict(color = 'red',size = 6),#默认是圆点 用symbol参数修改
    name = 'Head (1)'#name是这组点的名字
    ))

scatter_fig.add_trace(go.Scatter(
    x = iteration[toss.flatten() == 0],
    y = toss[toss == 0].flatten(),
    mode = 'markers',
    marker = dict(color = 'blue',size = 6),
    name = 'Tail (0)'
    ))

scatter_fig.update_layout(
    title = 'Coin Toss Results',
    xaxis_title = 'Iteration',
    yaxis_title = 'Result (0:Tail,1:Head)',
    yaxis = dict(tickvals = [0,1]),#yaxis表示配置y轴,tickvals配置刻度
    showlegend = True
    )

mean_fig = go.Figure()

mean_fig.add_trace(go.Scatter(
    x = iteration,
    y = cum_mean,
    mode = 'lines',
    line = dict(color = 'green'),
    name = 'Cumulative Mean'
    ))

mean_fig.add_trace(go.Scatter(
    x = [1,num_toss],
    y = [0.5,0.5],
    mode = 'lines',
    line = dict(color = 'red',dash = 'dash'),#dash表示虚线 一个一个dash组成的总的是虚线
    name = 'Mean = 0.5'
    ))

mean_fig.update_layout(
    title = 'Cumulative Mean of Coin Toss',
    xaxis_title = 'Iteration',
    yaxis_title = 'Cumulative Mean',
    yaxis = dict(tickvals = [0,0.5,1]),
    showlegend = True
    )


st.plotly_chart(scatter_fig)
st.plotly_chart(mean_fig)