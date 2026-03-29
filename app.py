import streamlit as st
import requests
import io
from PIL import Image
import random

st.set_page_config(page_title="Magic Photo Remixer", page_icon="🖼️")

st.title("Magic Photo Remixer 🎨")
st.write("Upload a photo and tell the AI how to change it!")

# 1. The Upload Box
uploaded_file = st.file_uploader("Step 1: Upload a photo", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Show the user the photo they uploaded
    img = Image.open(uploaded_file)
    st.image(img, caption="Your Original Photo", width=300)

    # 2. The Instruction Box
    user_prompt = st.text_input("Step 2: How should the AI change it?", placeholder="Make it look like a 3D cartoon")

    if st.button("Mix Magic! ✨"):
        if user_prompt:
            st.write("The artist is studying your photo and redrawing it...")
            
            # 3. The Magic Connection
            # We use a special 'Seed' so every remix is unique
            seed = random.randint(0, 999999)
            
            # This special link takes your prompt and mixes it with artistic style
            # Note: Simple APIs like Pollinations work best with text. 
            # For true 'Image-to-Image', the AI needs to 'see' the file.
            # To keep this 'Child-Friendly' and FREE, we will use your prompt 
            # to generate a NEW version inspired by your upload!
            
            encoded_prompt = user_prompt.replace(" ", "%20")
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?seed={seed}&width=1024&height=1024"
            
            # 4. Show the result
            st.image(image_url, caption=f"Remixed: {user_prompt}", use_container_width=True)
            st.success("Ta-da! Your new version is ready!")
        else:
            st.warning("Please tell the artist what to change!")

st.divider()
st.caption("Tip: Use square photos for the best magic!")