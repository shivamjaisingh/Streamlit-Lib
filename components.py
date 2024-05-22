import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

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




# with st.spinner("Counting on going..."):
#     progress_bar = st.progress(0)
#     for done in range(100):
#         time.sleep(0.1)
#         progress_bar.progress(done + 1)    
# st.success("Counting complete.")
# st.balloons()


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


st.checkbox("Click to add a check mark")

sample_data = {"Mammals": ["Cat", "Dog", "Bat", "Fox", "Pig"],
               "Number": [5, 3, 7, 1, 6]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.checkbox("Click to show a graph of the data"):
    fig, ax = plt.subplots()
    ax = sns.barplot(x="Mammals", y="Number", data=df)
    st.pyplot(fig)


st.radio("Which of these is not a mammal?",
["Dog", "Cat", "Eagle", "Pig"])

st.selectbox("Which of these is a mammal?",
["Pigeon", "Dove", "Fox", "Vulture"])

st.select_slider("Which of these is not a bird?",
["Ostrich", "Flamingo", "Turkey", "Bat", "Pigeon"])

st.multiselect("Which of these are birds?",
["Fox", "Eagle",
"Bat", "Dove"])

slider_int = st.slider("Select an integer",
                       min_value=0,
                       max_value=100,
                       value=25)
st.write(slider_int, type(slider_int))

slider_float = st.slider("Select a float",
                         min_value=0.0,
                         max_value=100.0,
                         value=25.0)
st.write(slider_float, type(slider_float))

st.markdown("## Single-Line Input")
text_input = st.text_input("Give an example of a mammal")
st.write(text_input)

st.markdown("## Multi-Line Input")
text_area = st.text_area("Give a list of 3 birds")
st.write(text_area)


file = st.file_uploader("Select a file to upload", type=["png", "jpg"])

if file is not None:
    st.image(file)

df = pd.DataFrame({"Mammal": ["Cat", "Bat", "Fox"],
                   "Number": [3, 1, 5]})

st.dataframe(df)

st.download_button("Download data",
                   df.to_csv(index=False),
                   file_name="data.csv")

with st.form("Order Form"):
    st.write("Order Details")
    fruit = st.select_slider("Select a fruit",
                             ["Banana", "Pawpaw", "Guava", "Mango"])

    quantity = st.number_input("Select the number of fruits", min_value=0)

    city = st.text_input("Type in your city")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("You have ordered {} {}(s) to be picked up at the {} branch"
                 .format(quantity, fruit, city))

st.write("These values, {}, {}, and {}, that were set inside the form are\
         accessible outside the form".format(quantity, fruit, city))


sample_data = [3.12, -4.31, 6.76, -9.88, 1.09]
col1, col2, col3 = st.columns([2.6,5,3.8])

col1.subheader("Line Chart")
col1.line_chart(sample_data)

col2.subheader("Area Chart")
col2.area_chart(sample_data)

with col3:
    st.subheader("Bar Chart")
    st.bar_chart(sample_data)




df = pd.DataFrame({"Mammal": ["Sea Lion", "Seal", "Walrus"], "Count": [3, 5, 2]})

st.dataframe(df)
with st.expander("Click to see a bar graph of the above data"):
    fig, ax = plt.subplots()
    ax.set_title("Mammal Count")
    ax = sns.barplot(x="Mammal", y="Count", data=df)
    st.pyplot(fig)