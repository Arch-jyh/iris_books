import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon,Circle
import numpy as np

with st.sidebar:
    num_vertices = st.slider('Number of side of polygon:',
                             min_value = 4,
                             max_value = 20,
                             step = 1)


#fig_1    
fig_1,ax = plt.subplots()
ax.set_aspect('equal')

hexagon_inner = RegularPolygon((0,0),numVertices = num_vertices,
                               radius = 1,alpha = 0.2,edgecolor = 'k')#多边形半径指的是到顶点的半径(外接圆半径)
ax.add_patch(hexagon_inner)

hexagon_outer = RegularPolygon((0,0), numVertices = num_vertices,
                               radius = 1/np.cos(np.pi/num_vertices),
                               alpha = 0.2,edgecolor = 'k')
ax.add_patch(hexagon_outer)

circle = Circle((0,0),radius = 1,facecolor = 'none',edgecolor = 'k')
ax.add_patch(circle)

plt.axis('off')
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
st.pyplot(fig_1)



#fig_2
n_array = np.linspace(3,num_vertices)

pi_lower_b = np.sin(np.pi/n_array) * n_array
pi_upper_b = np.tan(np.pi/n_array) * n_array

fig_2,ax = plt.subplots()

plt.axhline(y = np.pi,color = 'r',ls = '--')
plt.plot(n_array,pi_lower_b,color = 'b')
plt.plot(n_array,pi_upper_b,color = 'g')
plt.fill_between(n_array,pi_lower_b,pi_upper_b,color = '#DEEAF6')
plt.tight_layout()
plt.xlabel('Number of sides,n')
plt.ylabel(r'Estimate of $\pi$')
plt.xlim(n_array.min(),n_array.max())
st.pyplot(fig_2)