import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import streamlit as st

with st.sidebar:
    num_intervals = st.slider('Number of intervals:',
                              min_value = 5,
                              max_value = 50,
                              step = 1)
    
x = Symbol('x')
f_x = x**2
f_x_fcn = lambdify(x,f_x)

integral_f_x = integrate(f_x,x)