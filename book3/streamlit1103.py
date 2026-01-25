import streamlit as st
import numpy as np
import plotly.graph_objects as go

x = np.linspace(-2,2,100)

linear = x

quadratic = x**2

cubic = x**3

def plot_curve(x,y,title = 'Function Plot'):
    fig = go.Figure()
    #scatter是分散的意思,表示数据以散点形式给出,但是可以指定绘图方式
    fig.add_trace(go.Scatter(x = x,y = y,mode = 'lines',name = title,line = dict(width = 2)))
    
    fig.update_layout(
        title = title,
        xaxis_title = 'x',
        yaxis_title = 'f(x)',
        xaxis = dict(showgrid = True,zeroline = True),
        yaxis = dict(showgrid = True,zeroline = True),
        template = 'plotly_white',
        legend = dict(x = 0.02,y = 0.98))#
    
    st.plotly_chart(fig)
    

st.title('单项式叠加函数展示')
st.write('### 基本函数图像')#自动转为markdown格式,变为副标题

st.write('**一次函数**: $f_1(x) = x$')
plot_curve(x,linear,title = 'f1(x) = x')

st.write('**二次函数**: $f_1(x) = x^2$')
plot_curve(x,quadratic,title = 'f1(x) = x')

st.write('**三次函数**: $f_1(x) = x^3$')
plot_curve(x,cubic,title = 'f1(x) = x^3')


st.write('### 叠加函数设置')
st.write('请选择叠加洗漱 $a$,$b$,$c$,对应的权重:')

selected_terms = st.multiselect(#返回列表
    '选择要叠加的单项式',
    ['一次函数 ($f_1(x) = x$)','二次函数 ($f_2(x) = x^2$)','三次函数 ($f_3(x) = x^3$)'],
    default = ['一次函数 ($f_1(x) = x$)'])

a,b,c = 0,0,0

if '一次函数 ($f_1(x) = x$)' in selected_terms:
    a = st.slider('设置 $a$ 的值:',-10.0,10.0,1.0,step = 0.1)
    
if '二次函数 ($f_2(x) = x^2$)' in selected_terms:
    b = st.slider('设置 $b$ 的值:',-10.0,10.0,1.0,step = 0.1)
    
if '三次函数 ($f_3(x) = x^3$)' in selected_terms:
    c = st.slider('设置 $c$ 的值:',-10.0,10.0,1.0,step = 0.1)
    
    
combined_function = a * linear + b*quadratic + c*cubic

st.write('### 叠加函数公式')
latex_formula = f'f(x) = {a:.2f} \\cdot x + {b:.2f} \\cdot x^2 + {c:.2f} \\cdot x^3' 
st.latex(latex_formula)

st.write('### 叠加函数图像')
plot_curve(x,combined_function,title = '叠加函数 f(x)')