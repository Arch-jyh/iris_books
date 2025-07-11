import streamlit as st
#导入SciPy中的beta分类函数,生成高绿分布
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

#运行时的配置字典,修改默认绘图样式
p = plt.reParams
#这里的key期望的值是一个列表,是一个字体名称列表,按照顺序作为优先级依次寻找可用字体
#value为列表是防止没有可现实字体
#将新的列表赋值给value 这个列表中只有这一个可用字体
p['font.sans-serif'] = ['Roboto']
#全局字体
p['font.weight'] = 'light'
#开启坐标轴小刻度线
p['ytick.minor.visible'] = True
p['xtick.minor.visible'] = True
#打开主刻度网格
p['axes.grid'] = True
#网格颜色中等灰色
p['grid.color'] = '0.5'
#网格宽度
p['grid.linewidth'] = 0.5








































