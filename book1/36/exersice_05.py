import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p = plt.rcParams
p['font.sans-serif'] = ['Roboto']
p['font.weight'] = 'light'
p['ytick.minor.visible'] = True
p['xtick.minor.visible'] = True
p['axes.grid'] = True
p['grid.color'] = '0.5'
p['grid.linewidth'] = 0.5

import pandas_datareader as pdr
import seaborn as sns
import statsmodels.multivariate.pca as pca
import streamlit as st
p = plt.rcParams
p['font.sans-serif'] = ['Roboto']
p['font.weight'] = 'light'
p['ytick.minor.visible'] = True
p['xtick.minor.visible'] = True
p['axes.grid'] = True
p['grid.color'] = '0.5'
p['grid.linewidth'] = 0.5

df = pdr.data.DataReader(['DGS6MO','DGS1',
                          'DGS2','DGS5',
                          'DGS7','DGS10',
                          'DGS20','DGS30'],
                         data_source = 'fred',
                         start = '01-01-2022',
                         end = '12-31-2022')
df = df.dropna()

df = df.rename(columns={'DGS6MO':'0.5 yr',
                        'DGS1': '1 yr',
                        'DGS2': '2 yr',
                        'DGS5': '5 yr',
                        'DGS7': '7 yr',
                        'DGS10': '10 yr',
                        'DGS20': '20 yr',
                        'DGS30': '30 yr'})
#进行百分比转化,不断计算今天比昨天涨了多少
#当前行相较于前一行
X_df = df.pct_change()
#第一行没有上一行的数据,所以为NaN,这里删除
X_df = X_df.dropna()

with st.sidebar:
    st.title('Principal Component Analysis')
    num_of_PCs = st.slider('Numbor of PCs',
                           min_value = 1,
                           max_value = 8,
                           value = 2 , step = 1)

#构建pca模型 第一个参数为输入矩阵,每行一个样本,每列一个特征
#第二个参数对每列特征做处理
pca_model = pca.PCA(X_df,standardize = True)
variance_V = pca_model.eigenvals
explained_var_ratio = pca_model.eigenvals / pca_model.eigenvals.sum()

X_df_ = pca_model.project(num_of_PCs)

fig,axes = plt.subplots(2,4,figsize = (8,4))
axes = axes.flatten()

for col_idx,ax_idx in zip(list(X_df_.columns),axes):
    sns.lineplot(X_df_[col_idx],ax = ax_idx)
    sns.lineplot(X_df[col_idx],ax = ax_idx)
    sns.lineplot(X_df[col_idx] - X_df_[col_idx], c = 'k',ax = ax_idx)
    ax_idx.set_xticks([])
    ax_idx.set_yticks([])
    ax_idx.axhline(y = 0,c = 'k')
    
plt.tight_layout()
st.pyplot(fig)


fig2,axes = plt.subplots(2,4,figsize = (8,4))
axes = axes.flatten()

for col_idx,ax_idx in zip(list(X_df_.columns),axes):
    sns.scatterplot(X_df_[col_idx],ax = ax_idx,c = 'b')
    sns.scatterplot(X_df[col_idx],ax = ax_idx , c = 'r')
    sns.lineplot(X_df[col_idx] - X_df[col_idx], c = 'k',ax = ax_idx)
    ax_idx.set_xticks([])
    ax_idx.set_yticks([])
    ax_idx.axhline(y = 0,c = 'k')
    
plt.tight_layout()
st.pyplot(fig2)

fig3,axes = plt.subplots(2,4,figsize = (8,4))
axes = axes.flatten()

for col_idx,ax_idx in zip(list(X_df_.columns),axes):
    sns.heatmap(X_df_,ax = ax_idx)
    sns.heatmap(X_df,ax = ax_idx)
    ax_idx.set_xticks([])
    ax_idx.set_yticks([])
    ax_idx.axhline(y = 0,c = 'k')
    
plt.tight_layout()
st.pyplot(fig3)















