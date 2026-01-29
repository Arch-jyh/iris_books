import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import streamlit as st
from sympy import symbols,lambdify
import plotly.graph_objects as go

def mesh_square(x1_0,x2_0,r,num):
    rr = np.linspace(-r,r,num)
    xx1,xx2 = np.meshgrid(rr,rr)
    xx1 = xx1 + x1_0
    xx2 = xx2 + x2_0
    return xx1,xx2,rr


def plot_surf(xx1,xx2,ff,caption = 'fig'):
    norm_plt = plt.Normalize(ff.min(),ff.max())
    colors = cm.coolwarm(norm_plt(ff))

    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    surf = ax.plot_surface(xx1,xx2,ff,facecolors = colors,shade = False)
    surf.set_facecolor((0,0,0,0))

    plt.tight_layout()
    ax.set_xlabel(r'$\it{x_1}$')
    ax.set_ylabel(r'$\it{x_2}$')
    ax.set_zlabel(r'$\it{f}(\it{x_1},\it{x_2})$')#
    ax.set_title(caption)
    ax.set_proj_type('ortho')
    ax.set_xlim(xx1.min(),xx1.max())
    ax.set_ylim(xx2.min(),xx2.max())
    ax.grid(True,lw = 0.25,ls = ':')

    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = '10'
    
    return fig

    
def plot_contourf(xx1,xx2,ff,caption = 'fig'):
    fig,ax = plt.subplots()
    cntr2 = ax.contourf(xx1,xx2,ff,levels = 15,cmap = 'RdBu_r')
    fig.colorbar(cntr2,ax = ax)
    ax.set_xlabel(r'$\it{x_1}$')
    ax.set_ylabel(r'$\it{x_2}$')
    ax.set_title(caption)
    ax.grid(ls = '--',lw = 0.25,color = '0.5')
    
    return fig


with st.sidebar:
    st.latex(r'f(x_1,x_2) = ax_1^2 + bx_1x_2 + cx_2^2 + dx_1 + ex_2 + f')
    a = st.slider('a',-2.0,2.0,0.1)
    b = st.slider('b',-2.0,2.0,0.1)
    c = st.slider('c',-2.0,2.0,0.1)
    d = st.slider('d',-2.0,2.0,0.1)
    e = st.slider('e',-2.0,2.0,0.1)
    f = st.slider('f',-2.0,2.0,0.1)
    
    
x1,x2 = symbols('x1 x2')
x1_0,x2_0 = 0,0
r,num = 2,30
xx1,xx2,x1_array = mesh_square(x1_0,x2_0,r,num)
x2_array = x1_array


f_sym = a*x1**2 + b*x1*x2 + c*x2**2 + d*x1 + e*x2 + f
f_fcn = lambdify([x1,x2],f_sym)
ff = f_fcn(xx1,xx2)
fig_1 = plot_surf(xx1,xx2,ff)
fig_2 = plot_contourf(xx1,xx2,ff)

fig_surface = go.Figure(go.Surface(
    x = x1_array,y = x2_array,z = ff,showscale = False,colorscale = 'RdYlBu_r'))#
fig_surface.update_layout(autosize = True,width = 800,height = 600)

st.plotly_chart(fig_surface)

fig_contour = go.Figure(data = go.Contour(
    z = ff,x = x1_array,y = x2_array,colorscale = 'RdYlBu_r'))
fig_contour.update_layout(autosize = True,width = 600,height = 600)
st.plotly_chart(fig_contour)