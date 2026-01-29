import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from sympy.abc import x
from sympy import exp,lambdify,latex

with st.sidebar:
    st.latex(r'f(x) = a \exp(-(b(x - c))^2 + d')
    a = st.slider('a',-2.0,2.0,0.1)
    b = st.slider('b',-2.0,2.0,0.1)
    c = st.slider('c',-2.0,2.0,0.1)
    d = st.slider('d',-2.0,2.0,0.1)
    

x_array = np.arange(-4,4+0.01,step = 0.01)
#如果a = 0会自动化简为一个标量变为标量d,导致是一个数不是数组,绘图报错
f_x = a*exp(-(b*(x - c))**2) + d
st.latex('f(x) = ' + latex(f_x))

f_x_fcn = lambdify([x],f_x)
#如果已经是标量d的f_x_fcn,将不依赖x,输出直接是d,标量(为了信息最小化)
f_x_array = f_x_fcn(x_array)


fig,ax = plt.subplots()

plt.plot(x_array,f_x_array,color = '#0070C0',label = 'f(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y = 0,color = 'k',linestyle = '-')
plt.axvline(x = 0,color = 'k',linestyle = '-')
plt.xticks(np.arange(-4,5,step = 1))
plt.yticks(np.arange(-4,5,step = 1))
plt.axis('scaled')

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.spines[['top','right','bottom','left']].set_visible(False)

plt.legend()
ax.grid(ls = '--',lw = 0.25,color = '0.5')
plt.rcParams['figure.figsize'] = [7.5,3.5]
plt.rcParams['figure.autolayout'] = True

st.pyplot(fig)