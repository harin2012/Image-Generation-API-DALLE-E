from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey

# initialize your image generation client

client = OpenAI(api_key=apikey)


def generate_image(images_description, num_images):
    img_response = client.images.generate(
        model="dall-e-3",
        prompt=images_description,
        size="1024x1024",
        quality="standard",
        n=1

    )

    image_url = img_response.data[0].url
    return image_url


st.set_page_config(page_title="Dalle-Image_Generator", page_icon=":camera", layout="wide")
# create a title

st.title("Dalle-E-3 Image Generation Tool")

# create a subhead

st.subheader("Powered by the worlds most powerful image generation API-DALLE-E")

img_description = st.text_input('Enter the description for the image you want to generate')
num_of_images = st.number_input("select the number of images you want", min_value=1, max_value=5, value=1)

# create a button

if st.button("Generate Images"):
    generate_image = generate_image(img_description, num_of_images)

    st.image(generate_image)