import streamlit as st
import seaborn as sns
import plotly.express as px

#显示标题
st.title('Iris Datasets')

#从seaborn导入鸢尾花数据
df = sns.load_dataset('iris')
#第一个展开区域
with st.expander('Open and view DataFrame'):
    #显示数据帧
    st.write(df)
#第二个展开区域
with st.expander('Open and view Heatmap'):
    fig = px.imshow(df.iloc[:,:-1])
    st.write(fig)









