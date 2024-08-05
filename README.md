## RAG-based Quiz Generator
[![Model](https://img.shields.io/badge/-Gemini%20Pro-8E75B2?logo=google-gemini&logoColor=white)](https://developers.google.com/generative/models/gemini)
[![Python](https://img.shields.io/badge/-Python%203.10-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Database](https://img.shields.io/badge/database-Chroma%20DB-blue.svg)](https://docs.chromadb.com/)
[![UI](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

This project leverages a Retrieval-Augmented-Generation(RAG) approach to create quizzes from PDFs. It takes a PDF document as input and generates multiple-choice questions based on the provided topic and desired number of questions. The topic can either be explicitly specified or extracted from the PDF content itself.

This project serves as a foundational building block for the Kai bot's multi-file quiz generation feature (https://github.com/oddblaster/kai-ai-backend).

**Key Features:**

- **PDF Input:** Accepts PDFs as the source material for quiz generation.
- **Topic-Driven:** Enables specifying a topic for the quiz or automatically extracts it from the PDF.
- **Multiple Choice:** Generates quizzes in the multiple-choice format, promoting interactive learning.
- **Customizable:** Allows adjusting the number of questions based on your requirements.

**Technology Stack:**

- **Language:** Python 3.10
- **Cloud Platform:** Vertex AI from Google Cloud
- **Natural Language Processing Model:** Gemini 1.0 Pro
- **Vector Database:** Chroma DB (for efficient retrieval and storage)

**Future Enhancements:**

- **Answer Verification:** Implementing logic to verify the accuracy of generated quiz answers based on the source PDF.
- **Difficulty Levels:** Incorporating the ability to adjust question difficulty for different learning purposes.
- **Scalability:** Optimizing for handling larger PDFs and generating a higher volume of quizzes.

**License:**

This project is licensed under the MIT License - see the `LICENSE` file for details.
