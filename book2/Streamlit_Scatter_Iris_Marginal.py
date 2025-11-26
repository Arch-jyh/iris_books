import plotly.express as px
import streamlit as st

df = px.data.iris()
#.columns表示取出来列名,是1d列名序列,然后用切片取出来
#任然得到pdindex对象,很像list
features = df.columns[:4]


#建立一个作用域,在这个作用域下写的st空间都会放在sidebar区域
#相当于给with中的代码提供了运行条件
#with后面是一个上下文对象,创建了with中的代码运行的mini环境
#仅仅在with中才有这个环境,执行完将会将环境关闭
#不隔离变量,只是给with中的语句提供临时环境
with st.sidebar:
    st.title('鸢尾花数据')
    x_col = st.radio('横轴',features)
    y_col = st.radio('纵轴',features)
    marginal_x = st.radio('横轴边缘',['histogram','rug','box','violin'])
    marginal_y = st.radio('纵轴边缘',['histogram','rug','box','violin'])
    
    
fig = px.scatter(df,x = x_col,y = y_col,color = 'species',
                 marginal_x = marginal_x,
                 marginal_y = marginal_y,
                 width = 650,height = 600)


#用户每次点击边栏进行交互,代码完全都会重新执行
#点击的选项是自动保存的,自动重跑时候会加载上次点击的对象
st.plotly_chart(fig)
