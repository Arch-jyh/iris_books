import streamlit as st
import numpy as np
#导入的模块前者创建符号变量,后者将符号转换为python可计算函数
from sympy import symbols,lambdify
import matplotlib.pyplot as plt

#侧边框
#使用with每一次都刷新环境,上一次的残留不会影响环境
with st.sidebar:
    st.header('Choose coefficients')
    #打印latex公式,用于在侧边栏展示
    st.latex(r'f(x) = ax^2 + bx + c')
    #如果用户已经交互,前端交互过的值当成一个参数,优先级会比默认值高,再进行赋值一次
    #如果没有交互过默认执行
    a = st.slider('a',min_value = -5.0,
                  max_value = 5.0,
                  step = 0.01,value = 1.0)
    b = st.slider('b',min_value = -5.0,
                  max_value = 5.0,
                  step = 0.01,value = -2.0)
    c = st.slider('c',min_value= -5.0,
                  max_value= 5.0,
                  step= 0.01,value=-3.0)
    
#抛物线
#创建符号数学表达式
#这一步仅仅创建符号变量,仅供编程使用
#意义是职责分离,后面就知道这个x是自变量
x = symbols('x')
#用x表示的公式
#不转化abc是因为需要赋值,不是符号变量参与符号推导
#abc不是变量,如果也变为symbols将要后面传入多个数值
f_x = a*x**2 + b*x + c
x_array = np.linspace(-5,5,101)
#转化为python的表达式
#第一个参数表示自变量,第二个参数表示变量计算表达式
f_x_fcn = lambdify(x,f_x)
#计算抛物线
#abc为滑块输入值,得到了一个numpy数值组
y_array = f_x_fcn(x_array)

#主界面
st.title('Qudratic fubction')
st.latex(r'f(x) = ')
st.latex(f_x)

#可视化
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_array,y_array)

ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_aspect('equal',adjustable = 'box')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
st.write(fig)










