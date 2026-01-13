from sympy.abc import x
from sympy import Poly,latex#多项式工具,因为库是符号代数运算和多边形没关系
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


with st.sidebar:
    n = st.slider('Degree of a polynomial:',
                  min_value=2,
                  max_value = 20,
                  value = 10,
                  step = 1)
    
    
expr = (x+1)**n

#只进行代数展开,不管顺序
expr_expand = expr.expand()
#这一步会白絮,按次数顺序,得到的是多项式对象
expr_expand = Poly(expr_expand)
#将多项式对象(符号化的)转化为latex,latex是sympy中的
st.latex(latex(expr_expand))
#系数操作也会排序,按照次数从高到低
poly_coeffs = expr_expand.coeffs()

degrees = np.linspace(n,0,n+1)

fig,ax = plt.subplots()

plt.stem(degrees,np.array(poly_coeffs,dtype = float))
plt.xlim(0,n)
plt.xticks(np.arange(0,n+1))
y_max = max(poly_coeffs)
y_max = float(y_max)
plt.ylim(0,y_max)

ax.spines[['right','top']].set_visible(False)
ax.invert_xaxis()
plt.xlabel('Degree')
plt.ylabel('Coefficient')

st.pyplot(fig)