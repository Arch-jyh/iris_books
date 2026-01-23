import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

st.header('Chapter 9, Dive into Conic Sections | Book 3')

with st.sidebar:
    
    m = st.slider('Define m:',
                  1.0,2.0,value = 1.5,step = 0.1)
    st.write('m is ' + str(m))
    
    n = st.slider('Define n:',
                  1.0,2.0,value = 1.5,step = 0.1)
    st.write('n is ' + str(n))
    
    rho = st.slider('Define rho:',
                  -1.0,1.0,value = 0.0,step = 0.1)
    st.write('rho is ' + str(rho))
    
    
    
x = np.linspace(-4,4,num = 201)
y = np.linspace(-4,4,num = 201)

xx,yy = np.meshgrid(x,y)

fig,ax = plt.subplots(figsize = (8,8))

rect = patches.Rectangle((-m,-n),2*m,2*n,
                         linewidth = 0.25,edgecolor = 'k',
                         linestyle = '--',
                         facecolor = 'none')

ax.add_patch(rect)


ellipse = ((xx / m)**2 - 2*rho*(xx/m)*(yy/n) + (yy/n)**2) / (1 - rho**2)

plt.contour(xx,yy,ellipse,levels = [1],colors = ['b'])

plt.axvline(x = 0,color = 'k',ls = '-')
plt.axhline(y = 0,color = 'k',ls = '-')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)

ax.spines[['top','right','bottom','left']].set_visible(False)

st.pyplot(fig)