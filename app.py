# Import necessary libraries
import streamlit as st
from llama_index.llms import Gemini, HuggingFaceInferenceAPI,OpenAI
from llama_index import VectorStoreIndex, download_loader
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index import ServiceContext
from IPython.display import Markdown, display
import openai
import os

# Create Streamlit web app
def main():
    st.title("Web Page Q&A Chatbot")

    # Sidebar for customizations
    with st.sidebar:
        st.subheader("Customize Settings")

        # User input: Choose loader
        loader_option = st.selectbox("Choose a loader:", ["BeautifulSoupWebReader", "SimpleWebPageReader"])

        if loader_option == "BeautifulSoupWebReader":
            loader = download_loader("BeautifulSoupWebReader")()
        else:
            loader = download_loader("SimpleWebPageReader")()

        # User input: Choose LLMS
        llms_option = st.selectbox("Choose an LLMS:", ["zephyr-7b-Model", "Gemini","OpenAI"])

        if llms_option == "zephyr-7b-Model":
          hf_token = st.text_input("Enter your Hugging Face token:")
          llm = HuggingFaceInferenceAPI(model_name="HuggingFaceH4/zephyr-7b-alpha", token=hf_token) 
        elif llms_option == "Gemini":
          google_api_key = st.text_input("Enter your Google API key for Gemini model:")
          os.environ["GOOGLE_API_KEY"] = google_api_key
          llm = Gemini()
        else:
          # Provide OpenAI API key
          openai_api_key = st.text_input("Enter your OpenAI API key:")
          os.environ["OPENAI_API_KEY"] = openai_api_key
          llm = OpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=256)

    # Main content area
    st.markdown("Query your Web page data with using this chatbot")

    # User input: Web page link
    url = st.text_input("Enter the URL of the web page:")

    # Create Service Context
    embed_model_uae = HuggingFaceEmbedding(model_name="WhereIsAI/UAE-Large-V1")
    service_context = ServiceContext.from_defaults(llm=llm, chunk_size=800, chunk_overlap=20, embed_model=embed_model_uae)

    # Load documents
    if url:
        documents = loader.load_data(urls=[url])
        st.success("Documents loaded successfully!")

        # Create Vector Store Index
        index = VectorStoreIndex.from_documents(documents, service_context=service_context, show_progress=True)

        # Persist Storage Context
        index.storage_context.persist()

        # Create Query Engine
        query_engine = index.as_query_engine()

        # User input: Query
        query = st.text_input("Ask a question:")
        if query:
            # Run Query
            response = query_engine.query(query)

            # Display Result
            st.markdown(f"**Response:** {response}")
    else:
        st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
