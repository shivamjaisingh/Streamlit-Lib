import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

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

fig, ax = plt.subplots()
ax.set_title("Matplotlib Scatter Plot")
ax.scatter(arr1, arr2, s = arr3, c = arr3, alpha = 0.6)
st.pyplot(fig)



fig, ax = plt.subplots()
ax.set_title("Seaborn Scatter Plot")
ax = sns.scatterplot(arr1)
st.pyplot(fig)

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