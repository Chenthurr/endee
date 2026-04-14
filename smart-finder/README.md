# Smart AI Product Finder (Built on Endee)

## Project Overview
This project is a **Semantic Search & RAG-ready application** that allows users to find products based on intent rather than just keywords. It uses **Endee** as the high-performance vector database to store and retrieve product embeddings.

## Key Features
* **Semantic Search:** Understands context (e.g., "warm clothes" matches "jacket").
* **Vector Storage:** Powered by [Endee](https://github.com/endee-io/endee).
* **Metadata Filtering:** Hybrid search capabilities using product categories.

## System Design
1. **Data Layer:** CSV dataset is converted into 384-dimensional vectors using `all-MiniLM-L6-v2`.
2. **Database Layer:** Vectors are stored in **Endee** for fast similarity retrieval.
3. **Application Layer:** Streamlit frontend takes user input and queries the Endee API.

## Setup Instructions
1. **Start Endee Server:**
   ```bash
   chmod +x ./install.sh ./run.sh
   ./install.sh --release
   ./run.sh
