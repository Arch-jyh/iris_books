import numpy as np
from sympy import lambdify,sqrt
from sympy.abc import x,y
from matplotlib import pyplot as plt
import streamlit as st

def plot_fcn(A,B,dist_AX_zz,dist_BX_zz,distance):
    fig,ax = plt.subplots()

    plt.plot(A[0],A[1],color = 'k',marker = 'x',markersize = 12)
    plt.plot(B[0],B[1],color = 'k',marker = 'x',markersize = 12)
    colorbar = ax.contour(xx,yy,dist_AX_zz,levels = np.arange(0,15+1),cmap = 'RdYlBu_r')
    ax.contour(xx,yy,dist_BX_zz,levels = np.arange(0,15+1),cmap = 'RdYlBu_r')

    ax.contour(xx,yy,distance,levels = 0,colors = 'k')
    fig.colorbar(colorbar,ax = ax)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(y = 0,color = 'k',ls = '-')
    plt.axvline(x = 0,color = 'k',ls = '-')
    plt.xticks(np.arange(-10,10+1,step = 2))
    plt.yticks(np.arange(-10,10+1,step = 2))
    
    plt.axis('scaled')
    
    ax.set_xlim(xx.min(),xx.max())
    ax.set_ylim(yy.min(),yy.max())
    
    ax.spines[['top','right','bottom','left']].set_visible(False)
    
    ax.grid(ls = '--',lw = 0.25,color = '0.8')
    
    return fig

options = ('AP - BP = 0',
           'AP - BP - 3 = 0',
           'AP - BP + 3 = 0',
           'AP - 2*BP = 0',
           'AP + BP - 8 = 0')

with st.sidebar:
    option_i = st.selectbox('Choose as relation:',
                            options)
    
    A_x = st.slider('x coordinate of A:',
                    min_value = 2.0,
                    max_value = 4.0,
                    step = 0.1)
    A_y = st.slider('y coordinate of A:',
                    min_value = 2.0,
                    max_value = 4.0,
                    step = 0.1)
    
    B_x = st.slider('x coordinate of B:',
                    min_value = 2.0,
                    max_value = 4.0,
                    step = 0.1)
    B_y = st.slider('y coordinate of B:',
                    min_value = 2.0,
                    max_value = 4.0,
                    step = 0.1)
    
    

A = [A_x,A_y]
B = [B_x,B_y]

#转化为latex并渲染
#每一次执行都会新建一行,新建一行的显示不一定非要是latex,其他组件也可以,每个组件占一行
st.latex('A = ' + str(A))
st.latex('B = ' + str(B))

num = 301
x_array = np.linspace(-8,8,num)
y_array = np.linspace(-8,8,num)

xx,yy = np.meshgrid(x_array,y_array)

dist_AX = sqrt((x - A[0])**2 + (y - A[1])**2)
dist_BX = sqrt((x - B[0])**2 + (y - B[1])**2)

dist_AX_fcn = lambdify([x,y],dist_AX)
dist_BX_fcn = lambdify([x,y],dist_BX)

dist_AX_zz = dist_AX_fcn(xx,yy)
dist_BX_zz = dist_BX_fcn(xx,yy)


if option_i == 'AP - BP = 0':
    st.latex('AP - BP = 0')
    distance = dist_AX_zz - dist_BX_zz
    fig = plot_fcn(A,B,dist_AX_zz,dist_BX_zz,distance)
    
    st.pyplot(fig)
    
elif option_i == 'AP - BP - 3 = 0':
    st.latex('AP - BP - 3 = 0')
    distance = dist_AX_zz - dist_BX_zz - 3
    fig = plot_fcn(A,B,dist_AX_zz,dist_BX_zz,distance)
    
    st.pyplot(fig)
    
elif option_i == 'AP - BP + 3 = 0':
    st.latex('AP - BP + 3 = 0')
    distance = dist_AX_zz - dist_BX_zz + 3
    fig = plot_fcn(A,B,dist_AX_zz,dist_BX_zz,distance)
    
    st.pyplot(fig)
    
elif option_i == 'AP - 2*BP = 0':
    st.latex('AP - 2*BP = 0')#
    distance = dist_AX_zz - 2*dist_BX_zz
    fig = plot_fcn(A,B,dist_AX_zz,dist_BX_zz,distance)
    
    st.pyplot(fig)
    
elif option_i == 'AP + BP - 8 = 0':
    st.latex('AP + BP - 8 = 0')#
    distance = dist_AX_zz + dist_BX_zz - 8
    fig = plot_fcn(A,B,dist_AX_zz,dist_BX_zz,distance)
    
    st.pyplot(fig)