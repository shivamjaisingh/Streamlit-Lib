import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title("Exploring Streamlit")
st.header("Heading 1")
st.subheader("Subheading 1")
st.text("General Text")
st.markdown("```bash pip install streamlit```")
st.write("Latex Support")
st.latex(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2")
st.caption("Caption of the image")
st.metric(label="Velocity in kilometres per hour", value=75.4, delta=-2)

sample_data = {"Mammals": ["Cat", "Dog", "Pig"]}
df = pd.DataFrame(sample_data)
st.dataframe(df)
st.table(df)
st.json(sample_data)

df = np.random.randn(5,5)

st.markdown("## Line Chart")
st.line_chart(df)

st.markdown("## Area Chart")
st.area_chart(df)

st.markdown("## Bar Chart")
st.bar_chart(df)

arr1, arr2 = np.random.randn(100), np.random.rand(100)
arr3 = np.random.randint(1,1001,100)



st.image("https://bit.ly/edus3ha")
st.video("https://bit.ly/canibs3")
st.audio("https://bit.ly/rainaws3")



st.title("Super Basic Photo Editor")

def display_figures(img1, img2):
    fig1_left, fig2_right = st.columns(2)
    with fig1_left:
        st.markdown("### Original image")
        st.image(img1)
    with fig2_right:
        st.markdown("##s# Processed image")
        st.image(img2)

image_file = st.sidebar.file_uploader("Upload an image file", type=["jpg","png","tif"])

if image_file is not None:
    input_image = Image.open(image_file)

    effect = st.sidebar.selectbox("Select the type of image manipulation.",
         ["Rotate Image", "Flip Image", "Resize"])
        
    if effect == "Rotate Image":
        angle = st.sidebar.select_slider("Select the angle of rotation", [0, 90, 180, 270, 360])
        output_image = input_image.rotate(angle)

    if effect == "Flip Image":
        mirror_choice = st.sidebar.radio("Choose  how to flip the image",
                             ["Horizontally", "Vertically"])
        if mirror_choice == "Horizontally":
            output_image = input_image.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            output_image = input_image.transpose(Image.FLIP_TOP_BOTTOM)

    if effect == "Resize":
        scale_factor = st.sidebar.slider("Select the percentage size", 5, 10, 6)
        output_image = input_image.resize((input_image.width//scale_factor, input_image.height//scale_factor))

    if st.button("Process image"):
	    display_figures(input_image, output_image)


st.markdown("## Display code without execution")
code = '''st.audio("https://bit.ly/rainaws3")'''
st.code(code, language='python')

st.markdown("## Display code with execution")
with st.echo():
	st.audio("https://bit.ly/rainaws3")




with st.spinner("Counting on going..."):
    progress_bar = st.progress(0)
    for done in range(100):
        time.sleep(0.1)
        progress_bar.progress(done + 1)    
st.success("Counting complete.")
st.balloons()


st.markdown("### st.error()")
st.error("Syntax error")

st.markdown("### st.exception()")
st.exception(ZeroDivisionError("Divide by zero error"))

st.markdown("### st.warning()")
st.warning("This will be deprecated soon")

st.markdown("### st.info()")
st.info("App running optimally")

sample_data = {"Mammals": ["Cat", "Dog", "Bat", "Fox", "Pig"],
               "Birds": ["Parrot", "Eagle", "Duck", "Pegeon", "Vulture"]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.button("Click to show only mammals"):
    st.dataframe(df["Mammals"])