# Calorie Tracker

This is a simple web application built with Streamlit that allows you to calculate the calorie content of a meal by uploading an image of it. The application uses the OpenAI GPT-4 Vision model to analyze the image, identify the food items, and estimate their calorie counts.

## How It Works

The application leverages the power of OpenAI's vision capabilities. When you upload an image of your food:

1.  The image is sent to the GPT-4 Vision API.
2.  A prompt is provided to the model asking it to act as an expert nutritionist.
3.  The model analyzes the image to identify each food item present.
4.  It then calculates the estimated calories for each item and provides a total calorie count for the meal.
5.  The results are displayed in a clear and easy-to-read format.

## Setup Instructions

To run this application locally, you'll need to follow these steps:

### Prerequisites

*   Python 3.7+
*   An OpenAI API key with access to the GPT-4 Vision model.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Chatbot-Tracker
```

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

*   **For macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

*   **For Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 3. Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

The application requires your OpenAI API key to function. Create a file named `.env` in the root of the project directory and add your API key to it.

```
OPENAI_API_KEY="your-openai-api-key-here"
```

**Note:** Your API key is sensitive information. Do not commit the `.env` file to version control. The included `.gitignore` file should already be configured to ignore it.

### 5. Run the Application

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run app.py
```

This will start a local web server, and you can access the application in your browser at the URL provided in the terminal (usually `http://localhost:8501`).

## Usage

1.  Open the application in your web browser.
2.  Click the "Upload an image of your food..." button to select an image file (JPG, JPEG, or PNG).
3.  Once the image is uploaded and displayed, click the "Calculate Calories" button.
4.  The application will process the image and display the calorie details for each food item and the total.

## Dependencies

This project relies on the following Python libraries:

*   `streamlit`: For creating the web application interface.
*   `langchain-openai`: For interacting with the OpenAI API.
*   `python-dotenv`: For managing environment variables.
*   `Pillow`: For image manipulation.
*   `langchain`: Core LangChain library for building language model applications.
