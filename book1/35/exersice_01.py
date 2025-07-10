import streamlit as st
import seaborn as sns
#导入另一种绘图模块
import plotly.express as px

#显示标题 函数输入为str
st.title('Welcome to the world of :red[streamlit]')
#显示章节标题
st.header('Pandas DataFrame')
#显示markdown文本
st.markdown('Load :blue[Iris Data set]')
#导入数据帧
df = sns.load_dataset('iris')
##显示数据帧
st.write(df)
#章节标题
st.header('Visualize Using Heatmap')
#取所有的行,提取的列从索引为0直到数第二列(索引为-2,-1不算,开区间)
fig = px.imshow(df.iloc[:,:-1])
st.write(fig)

#练习
st.subheader('subheader')
st.caption('caption')
st.code('code like this')
st.text('i can stop the loneliness')
st.latex('abcd111')