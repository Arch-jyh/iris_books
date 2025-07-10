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
