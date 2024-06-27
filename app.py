import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## Llama 2 response function
def getLlamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model=r'D:\github\Llama 2\model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.01})
    
    template = """
Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)
    
    response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

# Page configuration
st.set_page_config(page_title="Generate Blogs", page_icon='🤖', layout='wide')

# Custom CSS for modern UI
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 2rem;
            background-color: white;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .footer {
            text-align: center;
            margin-top: 2rem;
            padding: 1rem 0;
            background-color: #4CAF50;
            color: white;
            font-size: 0.8rem;
            border-radius: 4px;
        }
        .footer a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .instructions {
            margin-bottom: 1rem;
        }
        .input-section {
            margin-bottom: 2rem;
            background-color: #f9f9f9;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .generate-btn button {
            background-color: #4CAF50;
            color: white;
            padding: 0.75rem 2rem;
            font-size: 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .generate-btn button:hover {
            background-color: #45a049;
        }
        .response {
            margin-top: 2rem;
            padding: 1.5rem;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            color: #333;  /* Ensure text color is visible */
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>Generate Blogs 🤖</h1>", unsafe_allow_html=True)

# Instructions
with st.expander("Instructions", expanded=True):
    st.markdown("""
        Welcome to the Blog Generator app! 
        - Enter your blog topic.
        - Specify the number of words.
        - Choose the target audience.
        - Click "Generate" to create your customized blog.
    """, unsafe_allow_html=True)

# Input fields
with st.container():
    input_text = st.text_input("Enter the Blog Topic")

    col1, col2 = st.columns([1, 1])

    with col1:
        no_words = st.text_input("Number of Words", placeholder="e.g., 500")
    with col2:
        blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common people'))

    # Generate button
    generate_clicked = st.button("Generate Blog", key="generate_button")

# Display response upon clicking Generate button
if generate_clicked:
    if not input_text:
        st.warning("Please enter a blog topic.")
    elif not no_words or not no_words.isdigit():
        st.warning("Please enter a valid number of words.")
    else:
        with st.spinner('Generating blog...'):
            response = getLlamaresponse(input_text, int(no_words), blog_style)
            st.success("Blog generated successfully!")
            st.markdown(f"<div class='response'>{response}</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        &copy; 2024 Blog Generator | Built with Streamlit |
        <a href="https://www.streamlit.io/" target="_blank">Streamlit</a>
    </div>
""", unsafe_allow_html=True)
