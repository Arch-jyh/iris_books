import plotly.express as px
import streamlit as st

df = px.data.gapminder()
df.rename(columns = {'country':'country or territory'},inplace = True)

with st.sidebar:
    st.title('气泡图')
    

fig = px.scatter(df,x = 'gdpPercap',y = 'lifeExp',
                 #按年份生成一张一张图,有动画效果
                 animation_frame='year',
                 #同一个国家在不同年份是同一个对象(一个气泡),可以让动画追踪
                 animation_group='country or territory',
                 size = 'pop',
                 color = 'continent',
                 hover_name = 'country or territory',
                 log_x = True,
                 size_max = 55,#缩放比例没变,但是大于55会限制
                 #坐标轴范围
                 range_x = [100,100000],
                 range_y = [25,90]
                 )

st.plotly_chart(fig)