import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data

st.set_page_config(page_title="Multiple Charts",page_icon=":bar_chart:")
st.title("CSV File To Multiple Charts")

with st.sidebar:
    uploaded_files = st.file_uploader("Choose CSV file(s)", accept_multiple_files=True)
    selected_file = None

    if uploaded_files:
        file_names = [file.name for file in uploaded_files]
        selected_file = st.selectbox("Select a file to visualize:", file_names)
        
        for file in uploaded_files:
            if file.name == selected_file:
                df = pd.read_csv(file)
                break
    else:
        st.warning("Please upload at least one CSV file.")

    chart_type = st.radio("Choose chart type:",["Line Chart", "Bar Chart", "Area Chart"],horizontal=False)

if 'df' in locals():
    data_columns = tuple(df.columns)
    st.write("Dataset Preview:")
    st.dataframe(df)

    x_column = None
    y_column = None
    x_label = None
    y_label = None
    color = "#83c9ff"
    if st.toggle("Features"):
        col1, col2 = st.columns(2)
        col1_1, col2_1 = st.columns(2)
        col3,emty,emty, = st.columns(3)

        with col1:
            st.subheader("Select X-axis")
            x_column = st.selectbox("", options=data_columns)

        with col2:
            st.subheader("Enter X-axis label")
            x_label = st.text_input("", value=x_column)

        with col1_1:
            st.subheader("Select Y-axis")
            y_column = st.selectbox("-", options=data_columns)

        with col2_1:
            st.subheader("Enter Y-axis label")
            y_label = st.text_input("-", value=y_column)
        
        with col3:
            st.subheader("Color")
            color = st.color_picker("","#83c9ff",label_visibility="collapsed")

        if chart_type == "Line Chart":
            st.header("Line Chart")
            st.line_chart(df,x=x_column,y=y_column,x_label=x_label,y_label=y_label,color=color,use_container_width=True)
        elif chart_type == "Bar Chart":
            st.header("Bar Chart")
            st.bar_chart(df,x=x_column,y=y_column,x_label=x_label,y_label=y_label,color=color,use_container_width=True)
        elif chart_type == "Area Chart":
            st.header("Area Chart")
            st.area_chart(df,x=x_column,y=y_column,x_label=x_label,y_label=y_label,color=color,use_container_width=True)
    else:
        if chart_type == "Line Chart":
            st.header("Line Chart")
            st.line_chart(df,use_container_width=True)
        elif chart_type == "Bar Chart":
            st.header("Bar Chart")
            st.bar_chart(df,use_container_width=True)
        elif chart_type == "Area Chart":
            st.header("Area Chart")
            st.area_chart(df,use_container_width=True)

else:
    st.info("Waiting for CSV file upload...")
    st.subheader("Line Chart")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)
    st.subheader("Bar Chart")
    source = data.barley()
    st.bar_chart(source, x="year", y="yield", color="site", stack=False)
    st.subheader("Area Chart")
    source = data.unemployment_across_industries()
    st.area_chart(source, x="date", y="count", color="series", stack="center")
    st.subheader("Map")
    df = pd.DataFrame({
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),})

    st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")
    st.subheader("Scatter Chart")
    chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)
    chart_data["col4"] = np.random.choice(["A", "B", "C"], 20)

    st.scatter_chart(
        chart_data,
        x="col1",
        y="col2",
        color="col4",
        size="col3",
    )