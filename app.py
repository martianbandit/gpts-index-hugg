import streamlit as st

x = st.slider('choisir la valeur')
st.write(x, 'squared is', x * x)
st.sidebar.write("### hey!")


prompt = st.chat_input("dit de quoi! ")
if prompt:
    st.write(f"L'utilisateur a publier ce prompt: {prompt}")
    
    import streamlit as st

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")