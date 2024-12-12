import streamlit as st
import openai

# App title
st.title("Chat with a Research Paper")

# File uploader
uploaded_file = st.file_uploader("Upload your research paper (text format only)", type=["txt"])

# API Key input
openai_api_key = st.text_input("Enter your OpenAI API key", type="password")
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)
# Question input
question = st.text_area("Ask a question about the paper")

# Main interaction logic
if uploaded_file and question and not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")

if uploaded_file and question and openai_api_key:
    # Read and decode the uploaded file
    article = uploaded_file.read().decode()

    # Construct the prompt
    prompt = f"Here's a research article:\n\n{article}\n\nBased on this article, please answer the following question:\n\n{question}"

    

    try:
        # Configure OpenAI API
        openai.api_key = openai_api_key

        # Generate response
        stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
        # Display response
        st.success("Response:")
        st.write(respuesta = stream.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")

# Add instructions
st.markdown(
    """
    ### Instructions
    1. Upload a plain text version of your research paper.
    2. Enter your OpenAI API key (kept private).
    3. Ask a question related to the uploaded paper.
    """
)
