import streamlit as st

button_return = st.button('click me')
st.write(button_return)
st.write(type(button_return))

checkbox_return = st.checkbox('check me')
st.write(checkbox_return)
st.write(type(checkbox_return))

radio_return = st.radio('choose one:',
                        ['A','B','C'])
st.write(radio_return)
st.write(type(radio_return))

selectbox_return = st.selectbox('choose me:',
                                ['1','2','3'])
st.write(selectbox_return)
st.write(type(selectbox_return))

#返回一个list列表,索引顺序对应选择顺序
multiselect_return=st.multiselect('Choose me:',
               ['1','2','3','4'])
st.write(multiselect_return)
st.write(type(multiselect_return))

#返回浮点值
slider_return = st.slider('Select a value:',
                          #必须都为浮点数
                          0.0,10.0,5.0)
st.write(slider_return)
st.write(type(slider_return))

#返回整数
select_slider_return = st.select_slider('Select a value:',
                                        options=[1,2,3,4,5])
st.write(select_slider_return)
st.write(type(select_slider_return))

text_input_return = st.text_input('Enter your name')
st.write(text_input_return)
st.write(type(text_input_return))

#返回浮点数
number_input_return = st.number_input('Enter a number')
st.write(number_input_return)
st.write(type(number_input_return))

text_area_return = st.text_area('Enter your massage')
st.write(text_area_return)
st.write(type(text_area_return))

#返回datetime.date类型,是日期对象
date_input_return = st.date_input('Select a date')
st.write(date_input_return)
st.write(type(date_input_return))
#datetime.time时间对象
time_input_return = st.time_input('Select a time')
st.write(time_input_return)
st.write(type(time_input_return))

#返回内存临时对象,因为没有web框架,是临时应用
file_uploader_return = st.file_uploader('upload a file')
st.write(file_uploader_return)
st.write(type(file_uploader_return))

#返回值不带颜色的#前缀 #是网页后加的表示颜色  直接返回6位16进制结果
color_picker_return = st.color_picker('Pick your color')
st.write(color_picker_return)
st.write(type(color_picker_return))


