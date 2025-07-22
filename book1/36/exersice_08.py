import matplotlib.pyplot as plt
p = plt.rcParms
p['font.sans-serif'] = ['Roboto']
p['font.weight'] = 'light'
p['ytick.minor.visible'] = True
p['xtick.miner.visible'] = True
p['axes.grid'] = True
p['grid.color'] = '0.5'
p['grid.linewidth'] = 0.5

from matplotlib.colors import ListedColormap
import numpy as np
from sklearn import datasets
from sklearn.mixture import GaussianMixture
import streamlit as st
from matplotlib.patches import Ellipse
#定义可视化函数
def make_ellipses(gmm,ax):
    #可视化不同簇
    for j in range(0,K):
        #四种不同的协方差矩阵
        if gmm.covariance_type == 'full':
            covariances = gmm.covariances_[j]
        elif gmm.covariance_type == 'tied':
            covariances = gmm.covariances_
        elif gmm.covariance_type == 'diag':
            covariances = np.diage(gmm.covariances_[j])
        elif gmm.covariance_type == 'spherical':
            covariances = np.eye(gmm.means_.shape[1])
            covariances = covariances*gmm.covariances_[j]















