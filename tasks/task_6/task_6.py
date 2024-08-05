import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator

if __name__ == "__main__":

    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "quizzify-gemini-424014",
        "location": "us-central1"
    }
    
    screen = st.empty() # Screen 1, ingest documents
    with screen.container():
        st.header("Quizzify")
        doc_processor = DocumentProcessor()
        doc_processor.ingest_documents()
        embeddings = EmbeddingClient(**embed_config)
        chroma_collector = ChromaCollectionCreator(doc_processor,embeddings)
        ####### YOUR CODE HERE #######
        # 1) Initalize DocumentProcessor and Ingest Documents from Task 3
        # 2) Initalize the EmbeddingClient from Task 4 with embed config
        # 3) Initialize the ChromaCollectionCreator from Task 5
        ####### YOUR CODE HERE #######

        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            topic_input = st.text_input("Topic for Generative Quiz",placeholder="Enter the topic of the document")
            questions = st.slider("Number of Questions", 0, 10, 5)
            ####### YOUR CODE HERE #######
            # 4) Use streamlit widgets to capture the user's input
            # 4) for the quiz topic and the desired number of questions
            ####### YOUR CODE HERE #######
            
            document = None
            
            submitted = st.form_submit_button("Generate a Quiz!")
            if submitted:
                chroma_collector.create_chroma_collection()
                ####### YOUR CODE HERE #######
                # 5) Use the create_chroma_collection() method to create a Chroma collection from the processed documents
                ####### YOUR CODE HERE #######
                    
                # Uncomment the following lines to test the query_chroma_collection() method
                document = chroma_collector.query_chroma_collection(topic_input) 
                
    if document:
        screen.empty() # Screen 2
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)