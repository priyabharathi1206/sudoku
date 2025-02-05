import streamlit as st
def on_input_change():
    st.session_state['message'] = "Input detected!"

def main():
    st.title("User Input Form in Grid Layout")
    
    # Define grid layout with columns
    col1, col2, col3 = st.columns(3)
    matrix=[["*" for _ in range(3)] for _ in range(3)]
    with col1:
        matrix[0][0]=st.number_input("",min_value=1,max_value=3,key="00",on_change=on_input_change)
        matrix[1][0]=st.number_input("",min_value=1,max_value=3,key="10",on_change=on_input_change)
        matrix[2][0]=st.number_input("",min_value=1,max_value=3,key="20",on_change=on_input_change)
    
    with col2:
        matrix[0][1]=st.number_input("",min_value=1,max_value=3,key="01",on_change=on_input_change)
        matrix[1][1]=st.number_input("",min_value=1,max_value=3,key="11",on_change=on_input_change)
        matrix[2][1]=st.number_input("",min_value=1,max_value=3,key="21",on_change=on_input_change)
    
    with col3:
        matrix[0][2]=st.number_input("",min_value=1,max_value=3,key="02",on_change=on_input_change)
        matrix[1][2]=st.number_input("",min_value=1,max_value=3,key="12",on_change=on_input_change)
        matrix[2][2]=st.number_input("",min_value=1,max_value=3,key="22",on_change=on_input_change)

    
    
    # Submit button
    if st.button("Submit"):
        st.success("fdf")

    
    if "message" in st.session_state:
        st.write(st.session_state["message"])

main()