# Document Query Chatbot

This is a Streamlit application that functions as a chatbot to query documents stored in the `data` directory.

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
