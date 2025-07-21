import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors,datasets
import streamlit as st

p = plt.rcParams
p["font.sans-serif"] = ["Roboto"]
p["font.weight"] = "light"
p["ytick.minor.visible"] = True
p["xtick.minor.visible"] = True
p["axes.grid"] = True
p["grid.color"] = "0.5"
p["grid.linewidth"] = 0.5

with st.sidebar:
    st.title('k-Nearest Neighbors Classification')
    #定义knn临近数量k
    k_neighbors = st.slider('k_neighbors',
                            min_value = 2,
                            max_value = 20,
                            value = 5,step =1)
    #配置权重
    w_x = st.slider('x_weight',min_value = 0.1,max_value = 2.0,value = 1.0,step = 0.1)
    w_y = st.slider('y_weight',min_value = 0.1,max_value = 2.0,value = 1.0,step = 0.1)
    
#导入整理数据
iris = datasets.load_iris()
X = iris.data[:,:2]
y = iris.target

x1_array = np.linspace(4,8,101)
x2_array = np.linspace(1,5,101)
xx1,xx2 = np.meshgrid(x1_array,x2_array)

rgb = [[255,238,255],
       [219,238,244],
       [228,228,228]]
rgb = np.array(rgb)/255.
cmap_light = ListedColormap(rgb)
cmap_bold = [[255,51,0],
             [0,153,255],
             [138,138,138]]
cmap_bold = np.array(cmap_bold)/255.

#创建kNN分类对象,并在模型层面加权
kNN = neighbors.KNeighborsClassifier(n_neighbors=k_neighbors,
                                     #使用minkowski
                                     metric='minkowski',
                                     metric_params={'w':np.array([w_x,w_y])},
                                     #欧式距离
                                     p=2)
kNN.fit(X,y)
q = np.c_[xx1.ravel(),xx2.ravel()]
#预测
y_predict = kNN.predict(q)
y_predict = y_predict.reshape(xx1.shape)
#可视化
fig,ax= plt.subplots()
plt.contourf(xx1,xx2,y_predict,cmap = cmap_light)
plt.contour(xx1,xx2,y_predict,levels = [0,1,2],
            colors = np.array([0,68,138])/255.)
sns.scatterplot(x = X[:,0],y = X[:,1],
                hue = iris.target_names[y],
                ax = ax,
                palette = dict(setosa = cmap_bold[0,:],
                               versicolor = cmap_bold[1,:],
                               virginica = cmap_bold[2,:]),
                alpha = 1.0,
                linewidth = 1,edgecolor = [1,1,1])
plt.xlim(4,8);plt.ylim(1,5)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
ax.grid(linestyle = '--',linewidth = 0.25,color = [0.5,0.5,0.5])
ax.set_aspect('equal',adjustable = 'box')
st.pyplot(fig)




















