import streamlit as st
import plotly.express as px

df = px.data.iris()

features = df.columns.to_list()[:-2] #将df的列标签变成python的list

with st.sidebar:
    st.write('2D scatter plot')
    x_feature = st.radio('Horizontal axis',
                         features)
    y_feature = st.radio('Verticla axis',
                         features)
    
with st.expander('Original data'):
    st.write(df)
    
with st.expander('Heatmap'):
    fig_1 = px.imshow(df.iloc[:,0:4],
                      color_continuous_scale='RdYlBu_r')
    st.plotly_chart(fig_1)
    
with st.expander('2D scatter plot'):
    fig_2 = px.scatter(df, x = x_feature,y = y_feature,color = 'species')
    st.plotly_chart(fig_2)
    
with st.expander('3D scatter plot'):
    fig_3 = px.scatter_3d(df,
                          x = 'sepal_length',
                          y = 'sepal_width',
                          z = 'petal_length',
                          color = 'species')
    st.plotly_chart(fig_3)
    
with st.expander('Paerwise scatter plot'):
    fig_4 = px.scatter_matrix(df,
                              dimensions=['sepal_width',
                                          'sepal_length',
                                          'petal_width',
                                          'petal_length'],
                              color = 'species')
    
    st.plotly_chart(fig_4)