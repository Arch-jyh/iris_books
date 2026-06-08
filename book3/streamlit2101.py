import streamlit as st
import plotly.express as px


df = px.data.iris()

features = df.columns.to_list()[:-2]#取前四列

with st.sidebar:
    st.write('2D scatter plot')
    
    x_feature = st.radio('Horizontal axis',
                         features)
    
    y_feature = st.radio('Vertical axis',
                         features) 
    
    marginal_x = st.radio('Horizontal marginal',
                          ['histogram',
                           'rug',
                           'box',
                           'violin'])
    
    marginal_y = st.radio('Vertical marginal',
                          ['histogram',
                           'rug',
                           'box',
                           'violin'])
    
    
with st.expander('Original data'):
    st.write(df)
    
with st.expander('2D scatter plot'):
    fig_2 = px.scatter(df,
                       x = x_feature,
                       y = y_feature,
                       color = 'species',
                       marginal_x = marginal_x,
                       marginal_y = marginal_y)
    
    st.plotly_chart(fig_2)