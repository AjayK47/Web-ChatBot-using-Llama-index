# Web-Page-ChatBot-using-Llama-index
Q&A Chatbot for Webpages utilizing Llama-Index with various LLms and Hugging Face embeddings

## Overview
Web Page Q&A Chatbot is a Streamlit web application designed to interactively answer questions based on web page data. The chatbot utilizes different Language Models (LLMS) such as Hugging Face Gemini or OpenAI to provide accurate and context-aware responses.

### Preview

https://github.com/AjayK47/Web-ChatBot-using-Llama-index/assets/88961945/0bc92889-1ffb-46b4-89bc-06649b4ea7ba

### Features

- **Dynamic Customization:**
  - Choose between different web page loaders, including BeautifulSoupWebReader and SimpleWebPageReader.
  - Select from various LLMS, such as zephyr-7b-Model, Gemini, and OpenAI.

- **User-Friendly Interface:**
  - Input the web page URL to extract information.
  - Ask questions interactively using the provided chat interface.

- **Flexible Model Integration:**
  - Seamlessly integrate Hugging Face, Gemini, or OpenAI models for diverse language processing capabilities.

### Prerequisites

- Python 3.10
- [Streamlit](https://streamlit.io/)
- Additional dependencies (specified in requirements.txt)

Strongly Recommend running this code while connected to GPU

### Installation

1. Clone the repository:

  ```bash
   git clone https://github.com/AjayK47/Web-ChatBot-using-Llama-index.git
   ```

2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### API requirements

We are currently exploring the Gemini-Pro model from Google, the GPT-3.5 model from OpenAI, and open-source Hugging Face models in this Project. You can choose to use only one model along with its corresponding API key for your specific use case. There's no requirement to use all API keys if it's not necessary for your experimentation.

Get the API keys Here:

- [Google API Key](https://ai.google.dev/)
- [Open AI API key](https://openai.com/)
- [Hugging Face Token](https://huggingface.co/settings/tokens)

### Usage

- Run the Streamlit app:
  
  ```bash
  streamlit run app.py
  ```
- Customize settings using the sidebar options.
- Enter the web page URL and ask questions interactively.

### Customization

- Loader Options:
    - Choose between BeautifulSoupWebReader and SimpleWebPageReader to load web page data.

- LLMS Options:
    - Select from zephyr-7b-Model, Gemini, or OpenAI for language processing.

You can customize the embedding model used for document indexing. Edit the 'app.py' file and modify the 'HuggingFaceEmbedding' instantiation:

```bash
# Example using a different Hugging Face embedding model
embed_model_uae = HuggingFaceEmbedding(model_name="your/own-model-name")
```
you can find best text embedding model for you with help of 
[MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

Like Wise you can also Customize the Large language model with other Open source models from Hugging Face

```bash
# Example using a different Hugging Face model
llm = HuggingFaceInferenceAPI(model_name="your/own-model-name", token=hf_token)
```

### Future improvements

- Enabling customization of embedding models for user on WebUI

- Loading More dynamic Data from Websites rather than only html code , improved data loading mechanism

- User Authentication: Implement user authentication to allow users to save preferences, access personalized features, or keep a history of their queries.

- Advanced Settings: Provide advanced settings for users who want more control over language models, query parameters, or other customization options.

- Model Switching: Allow users to dynamically switch between different language models during runtime without restarting the application.

- Multi-Language Support: Extend language support to accommodate multiple languages, allowing users to interact with the chatbot in their preferred language.

### Contributing

Contributions are always welcome!

Feel Free to Contribute!

### License

[MIT](https://choosealicense.com/licenses/mit/)

### Authors

- [Ajay K](https://www.github.com/AjayK47)

### Acknowledgements

- [LlamaHub](https://llamahub.ai/)
