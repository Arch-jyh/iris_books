import numpy as np
from sympy import lambdify, diff, exp, latex, simplify  # 导入符号计算和数学库
from sympy.abc import x, y  # 定义符号变量 x 和 y
from matplotlib import pyplot as plt  # 导入 Matplotlib 进行绘图
from matplotlib import cm  # 导入颜色映射模块
import streamlit as st


with st.sidebar:
    x_a = st.slider('a:',
                    min_value = -1.5,
                    max_value = 1.5,
                    step = 0.1)
    y_b = st.slider('b:',
                    min_value = -1.5,
                    max_value = 1.5,
                    step = 0.1)
    
num = 301  # 设置网格数量
x_array = np.linspace(-1.5, 1.5, num)  # x 的取值范围
y_array = np.linspace(-1.5, 1.5, num)  # y 的取值范围
xx, yy = np.meshgrid(x_array, y_array)  # 创建 x 和 y 的网格
num_stride = 10  # 绘制时的步长

f_xy = exp(-x**2 - y**2)  # 定义函数 f(x, y) = exp(-x^2 - y^2)
f_xy_fcn = lambdify([x, y], f_xy)  # 将符号函数转换为数值函数
f_xy_zz = f_xy_fcn(xx, yy)  # 计算 f(x, y) 在全局网格上的值
x_a_array = np.linspace(x_a - 0.5, x_a + 0.5, 101)  # x 的局部范围
y_b_array = np.linspace(y_b - 0.5, y_b + 0.5, 101)  # y 的局部范围
xx_local, yy_local = np.meshgrid(x_a_array, y_b_array)  # 创建局部网格
f_xy_zz_local = f_xy_fcn(xx_local, yy_local)  # 计算 f(x, y) 在局部网格上的值
f_ab = f_xy_fcn(x_a, y_b)  # 计算 f(x_a, y_b) 的值



f_ab = f_xy_fcn(x_a, y_b)  # 再次计算 f(x_a, y_b) 用于零阶近似
approx_zero_order = f_ab + xx_local * 0

df_dx = f_xy.diff(x)  # 计算 f(x, y) 对 x 的偏导数
df_dx_fcn = lambdify([x, y], df_dx)  # 转换为数值函数
df_dx_a_b = df_dx_fcn(x_a, y_b)  # 计算偏导数在 (x_a, y_b) 处的值
df_dy = f_xy.diff(y)  # 计算 f(x, y) 对 y 的偏导数
df_dy_fcn = lambdify([x, y], df_dy)  # 转换为数值函数
df_dy_a_b = df_dy_fcn(x_a, y_b)  # 计算偏导数在 (x_a, y_b) 处的值
approx_first_order = approx_zero_order + df_dx_a_b * (xx_local - x_a) + df_dy_a_b * (yy_local - y_b)  # 一阶近似

d2f_dxdx = f_xy.diff(x, 2)  # 计算 f(x, y) 对 x 的二阶偏导数
d2f_dxdx_fcn = lambdify([x, y], d2f_dxdx)  # 转换为数值函数
d2f_dxdx_a_b = d2f_dxdx_fcn(x_a, y_b)  # 计算二阶偏导数在 (x_a, y_b) 处的值
d2f_dxdy = f_xy.diff(x, y)  # 计算 f(x, y) 对 x 和 y 的混合二阶偏导数
d2f_dxdy_fcn = lambdify([x, y], d2f_dxdy)  # 转换为数值函数
d2f_dxdy_a_b = d2f_dxdy_fcn(x_a, y_b)  # 计算混合二阶偏导数在 (x_a, y_b) 处的值
d2f_dydy = f_xy.diff(y, 2)  # 计算 f(x, y) 对 y 的二阶偏导数
d2f_dydy_fcn = lambdify([x, y], d2f_dydy)  # 转换为数值函数
d2f_dydy_a_b = d2f_dydy_fcn(x_a, y_b)  # 计算二阶偏导数在 (x_a, y_b) 处的值
approx_second_order = approx_first_order + (d2f_dxdx_a_b * (xx_local - x_a)**2
                                            + 2 * d2f_dxdy_a_b * (xx_local - x_a) * (yy_local - y_b)
                                            + d2f_dydy_a_b * (yy_local - y_b)**2) / 2  # 二阶近似





fig = plt.figure()
ax = fig.add_subplot(1,3,1,projection = '3d')
ax.plot_wireframe(xx, yy, f_xy_zz,
                  color=[0.5, 0.5, 0.5],
                  rstride=num_stride, cstride=num_stride,
                  linewidth=0.25)  # 绘制全局网格上的 f(x, y)

approx_zero_order = f_ab + xx_local * 0  # 常数近似

ax.plot_wireframe(xx_local, yy_local, approx_zero_order,
                  color=[1, 0, 0],
                  rstride=num_stride, cstride=num_stride,
                  linewidth=0.25)  # 绘制局部网格上的零阶近似平面

ax.plot(x_a, y_b, f_ab, marker='x', color='r',
        markersize=12)  # 标记展开点

ax.set_proj_type('ortho')  # 设置正交投影

ax.set_xlabel('$x_1$')  # 设置 x 轴标签
ax.set_ylabel('$x_2$')  # 设置 y 轴标签
ax.set_zlabel('$f(x_1,x_2)$')  # 设置 z 轴标签

ax.set_xlim(xx.min(), xx.max())  # 设置 x 轴范围
ax.set_ylim(yy.min(), yy.max())  # 设置 y 轴范围
ax.set_zlim(f_xy_zz.min(), 1.5)  # 设置 z 轴范围

ax.view_init(azim=-145, elev=30)  # 设置视角
plt.tight_layout()
ax.grid(False)


ax = fig.add_subplot(1,3,2,projection = '3d')
ax.plot_wireframe(xx, yy, f_xy_zz,
                  color=[0.5, 0.5, 0.5],
                  rstride=num_stride, cstride=num_stride,
                  linewidth=0.25)  # 绘制全局网格上的 f(x, y)

ax.plot_wireframe(xx_local, yy_local, approx_first_order,
                  color=[1, 0, 0],
                  rstride=num_stride, cstride=num_stride,
                  linewidth=0.25)  # 绘制局部网格上的一阶近似平面

ax.plot(x_a, y_b, f_ab, marker='x', color='r',
        markersize=12)  # 标记展开点

ax.set_proj_type('ortho')  # 设置正交投影

ax.set_xlabel('$x_1$')  # 设置 x 轴标签
ax.set_ylabel('$x_2$')  # 设置 y 轴标签
ax.set_zlabel('$f(x_1,x_2)$')  # 设置 z 轴标签

ax.set_xlim(xx.min(), xx.max())  # 设置 x 轴范围
ax.set_ylim(yy.min(), yy.max())  # 设置 y 轴范围
ax.set_zlim(f_xy_zz.min(), 1.5)  # 设置 z 轴范围

ax.view_init(azim=-145, elev=30)  # 设置视角
plt.tight_layout()
ax.grid(False)


ax = fig.add_subplot(1,3,3,projection = '3d')
ax.plot_wireframe(xx, yy, f_xy_zz,
                  color=[0.5, 0.5, 0.5],
                  rstride=num_stride, cstride=num_stride,
                  linewidth=0.25)  # 绘制全局网格上的 f(x, y)

ax.plot_wireframe(xx_local, yy_local, approx_second_order,
                  color=[1, 0, 0],
                  rstride=num_stride, cstride=num_stride,
                  linewidth=0.25)  # 绘制局部网格上的一阶近似平面

ax.plot(x_a, y_b, f_ab, marker='x', color='r',
        markersize=12)  # 标记展开点

ax.set_proj_type('ortho')  # 设置正交投影

ax.set_xlabel('$x_1$')  # 设置 x 轴标签
ax.set_ylabel('$x_2$')  # 设置 y 轴标签
ax.set_zlabel('$f(x_1,x_2)$')  # 设置 z 轴标签

ax.set_xlim(xx.min(), xx.max())  # 设置 x 轴范围
ax.set_ylim(yy.min(), yy.max())  # 设置 y 轴范围
ax.set_zlim(f_xy_zz.min(), 1.5)  # 设置 z 轴范围

ax.view_init(azim=-145, elev=30)  # 设置视角
plt.tight_layout()
ax.grid(False)

st.pyplot(fig)