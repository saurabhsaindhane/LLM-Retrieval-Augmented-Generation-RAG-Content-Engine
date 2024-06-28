import os
import streamlit as st
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# Function to initialize or load the index
def initialize_index():
    PERSIST_DIR = "./storage"
    if not os.path.exists(PERSIST_DIR):
        # Load the documents and create the index
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        # Store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # Load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    return index

# Streamlit app
def main():
    st.title("Content Engine ")

    index = initialize_index()
    query_engine = index.as_query_engine()

    st.write("Ask any question about the documents in the data folder.")

    if "history" not in st.session_state:
        st.session_state.history = []

    query = st.text_input("You:", "")
    
    if st.button("Send"):
        if query:
            response = query_engine.query(query)
            st.session_state.history.append({"user": query, "bot": response.response})

    st.write("Chat History:")
    for chat in st.session_state.history:
        st.write(f"You: {chat['user']}")
        st.write(f"Bot: {chat['bot']}")

if __name__ == "__main__":
    main()
