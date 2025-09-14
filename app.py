import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import base64
from PIL import Image
import io

load_dotenv()

def get_response(image_data, prompt):
    model = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=1024)
    
    image_b64 = base64.b64encode(image_data).decode("utf-8")
    
    message = {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"},
            },
        ],
    }
    
    response = model.invoke([message])
    return response.content

st.set_page_config(page_title="Calorie Tracker", layout="wide")

st.title("Calorie Tracker")

uploaded_file = st.file_uploader("Upload an image of your food...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
    image_data = uploaded_file.getvalue()
    
    prompt_template = """
    You are an expert in nutritionist where you need to see the food items from the image
    and calculate the total calories, also provide the details of every food items with calories intake
    is below format

    1. Item 1 - no of calories
    2. Item 2 - no of calories
    ----
    ----
    """
    
    if st.button("Calculate Calories"):
        with st.spinner("Calculating..."):
            response = get_response(image_data, prompt_template)
            st.subheader("Calorie Details")
            st.write(response)
