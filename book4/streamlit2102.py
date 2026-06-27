import numpy as np
from sympy import lambdify,diff,exp,latex,simplify,symbols
import plotly.figure_factory as ff #px快速画图 go精细控图 ff生成特殊图
import plotly.graph_objects as go
import streamlit as st


x1,x2 = symbols('x1 x2')
num = 301
x1_array = np.linspace(-3,3,num)
x2_array = np.linspace(-3,3,num)
xx1,xx2 = np.meshgrid(x1_array,x2_array)

f_x = 3*(1 - x1)**2*exp(-(x1**2) - (x2 + 1)**2) \
    -10 * (x1 / 5 - x1**3 - x2**5) * exp(-x1**2 - x2**2) \
        -1 / 3*exp(-(x1 + 1) ** 2 - x2**2)
        
f_x_fcn = lambdify([x1,x2],f_x)
f_zz = f_x_fcn(xx1,xx2)

st.latex('f(x_1,x_2) = ' + latex(f_x))

grad_f = [diff(f_x,var) for var in (x1,x2)]
grad_fcn = lambdify([x1,x2],grad_f)

x1__ = np.linspace(-3,3,40)
x2__ = np.linspace(-3,3,40)
xx1_,xx2_ = np.meshgrid(x1__,x2__)
V = grad_fcn(xx1_,xx2_)

fig_surface = go.Figure(go.Surface(
    x = x1_array,
    y = x2_array,
    z = f_zz,
    showscale = False,
    colorscale = 'RdYlBu_r'
    ))
fig_surface.update_layout(
    autosize = False,
    width = 800,
    height = 600)
st.plotly_chart(fig_surface)

#arrow_scale控制箭头头部缩放 scale控制剪头整体缩放
f = ff.create_quiver(xx1_,xx2_,V[0],V[1],arrow_scale = .1,scale = 0.03)
#不会穿过所有的点,根据数据作图
f_stream = ff.create_streamline(x1__,x2__,V[0],V[1],arrow_scale = .1)
#f本身已经是是个图,这里需要吧trace提出来 data和layout平级
#data里面有Scatter和bar...所以取[0]就是需要的图
trace1 = f.data[0] 
trace3 = f_stream.data[0]
trace2 = go.Contour(
    x = x1_array,
    y = x2_array,
    z = f_zz,
    showscale= False,
    colorscale = 'RdYlBu_r'
    )

data = [trace1,trace2]
fig = go.Figure(data=data)
fig.update_layout(
    autosize = False,
    width = 800,
    height = 800)
fig.add_hline(y = 0,line_color = 'black')
fig.add_vline(x = 0,line_color = 'black')
fig.update_xaxes(range = [-2,2])
fig.update_yaxes(range = [-2,2]) #
fig.update_coloraxes(showscale = False)
st.plotly_chart(fig)

data2 = [trace3,trace2]
fig2 = go.Figure(data=data2)
fig2.update_layout(
    autosize = False,
    width = 800,
    height = 800)
fig2.add_hline(y = 0,line_color = 'black')
fig2.add_vline(x = 0,line_color = 'black')
fig2.update_xaxes(range = [-2,2])
fig2.update_yaxes(range = [-2,2]) #
fig2.update_coloraxes(showscale = False)
st.plotly_chart(fig2)