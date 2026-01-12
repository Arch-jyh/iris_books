import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def bmatrix(a):
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    #array转化为字符串时候,数据的逗号分割改成了空格
    #replace将[]都换成了空字符串 splitlines表示按照按换行符分隔字符串
    lines = str(a).replace('[','').replace(']','').splitlines()
    rv = [r'\begin{bmatrix}']
    #split是将字符串按照空白分隔
    #'&'.join表示用&加入join传入的多个字符串之间组成新的一个字符串
    rv += ['   ' + '&'.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']
    return '\n'.join(rv)#\n是为了python字符串的观察,latex已经有\\换行了,不用\n仍然正确.\n是Python的latex会在解析时候不当成指令,当成无意义空白

with st.sidebar:
    st.latex(r'C_{m\times n} = A_{m\times p} B_{p\times n}')
    rows_A = st.slider('Number of rows in A:',
                       min_value = 1,
                       max_value = 9,
                       value = 5,
                       step = 1)#value是默认值
    
    cols_A = st.slider('Number of cols in A:',
                       min_value = 1,
                       max_value = 9,
                       value = 5,
                       step = 1)
    
    rows_B = st.slider('Number of rows in B:',
                       min_value = 1,
                       max_value = 9,
                       value = 5,
                       step = 1)
    
    cols_B = st.slider('Number of cols in B:',
                       min_value = 1,
                       max_value = 9,
                       value = 5,
                       step = 1)
    

#10是上边界,开区间不包含,默认最小值为0(包含)
#size不是必须的,不写返回单个整数,size为单个值输出1维数组,这里输出二维数组
A = np.random.randint(10,size = (rows_A,cols_A))
B = np.random.randint(10,size = (rows_B,cols_B))

st.latex(r'A_{m\times p} = ' + bmatrix(A))
st.latex(r'B_{p\times n} = ' + bmatrix(B))

try:
    
    C = A@B
    st.latex('C = AB = ' + bmatrix(C))
        
    fig,axs = plt.subplots(1,5,figsize = (12,3))

    plt.sca(axs[0])
    ax = sns.heatmap(A,cmap = 'RdYlBu_r',
                    cbar_kws = {'orientation':'horizontal'},
                    yticklabels = np.arange(1,rows_A+1),xticklabels = np.arange(1,cols_A+1))
    ax.set_aspect('equal')
    plt.title('$A$')
    plt.yticks(rotation = 10)
    
    
    plt.sca(axs[1])
    plt.title('$@$')
    plt.axis('off')
    
    plt.sca(axs[2])
    ax = sns.heatmap(B,cmap = 'RdYlBu_r',
                    cbar_kws = {'orientation':'horizontal'},
                    yticklabels = np.arange(1,rows_B+1),xticklabels = np.arange(1,cols_B+1))
    ax.set_aspect('equal')
    plt.title('$B$')
    plt.yticks(rotation = 10)
    
    
    plt.sca(axs[3])
    plt.title('$=$')
    plt.axis('off')
    
    plt.sca(axs[4])
    ax = sns.heatmap(C,cmap = 'RdYlBu_r',
                    cbar_kws = {'orientation':'horizontal'},
                    yticklabels = np.arange(1,rows_A+1),xticklabels = np.arange(1,cols_B+1))
    ax.set_aspect('equal')
    plt.title('$C$')
    plt.yticks(rotation = 10)
    
    st.pyplot(fig)
    
except:
    st.write('The number of columns of the first matrix,must equal the number of rows of the second matrix.')