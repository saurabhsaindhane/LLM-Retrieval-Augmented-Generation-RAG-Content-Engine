# Content Engine: Document Query Chatbot by Saurabh Saindhane

This is a Streamlit application that functions as a chatbot to query documents stored in the `data` directory.

LangChain is a powerful framework designed to facilitate the development of applications using large language models (LLMs). LLMs, such as OpenAI's GPT-4, are advanced AI models trained on vast amounts of text data, enabling them to understand and generate human-like text. These models have revolutionized the field of NLP by providing the ability to perform a wide range of language tasks with high accuracy. Retrieval-Augmented Generation (RAG) is an innovative approach that combines the strengths of LLMs with information retrieval techniques. In RAG, a retrieval component fetches relevant documents or pieces of information from a large corpus, which are then used to augment the generation process of the LLM, resulting in more accurate and contextually relevant responses. This hybrid method enhances the capabilities of LLMs, especially in tasks requiring up-to-date or domain-specific information. NLP technologies also encompass various other tools and techniques, including named entity recognition (NER), sentiment analysis, machine translation, and text summarization, all of which contribute to the advancement of human-computer interaction by enabling machines to understand and generate natural language efficiently. By leveraging LangChain and related NLP technologies, developers can create sophisticated AI applications that perform complex language tasks, provide intelligent insights, and enhance user experiences.

## Features

- Indexes documents in the `data` directory.
- Allows users to query the documents.
- Displays chat history.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/document-query-chatbot.git
    cd document-query-chatbot
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Dependencies

- streamlit
- llama-index
- PyMuPDF (if working with PDFs)

## Usage

- Place your documents in the `data` directory.
- Run the Streamlit app.
- Enter your query in the text input and click `Send`.

## License

[MIT](LICENSE)
