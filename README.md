TerraNews

TerraNews is a full-stack web application designed to aggregate, analyze, and categorize news articles based on their content and political bias. The platform leverages machine learning, natural language processing, and a robust backend to provide users with insights into the political leanings of various news sources.

Features:
- News Aggregation: Automatically fetches news articles from multiple RSS feeds.
- Bias Detection: Classifies articles into political categories (Left, Center, Right) using a predefined bias map.
- Content Clustering: Groups similar articles into clusters based on content similarity using vector embeddings.
- REST API: Provides endpoints for retrieving articles and their metadata.
- Database Integration: Stores articles, clusters, and metadata in a PostgreSQL database.
- Scalable Architecture: Built with Spring Boot for the backend and Python for data processing.

Tech Stack:
- Backend: Java (Spring Boot), PostgreSQL
- Machine Learning: Python, Sentence Transformers, BeautifulSoup
- Frontend: REST API

Future Enhancements:
- Add a frontend for better user interaction.
- Implement real-time article updates.
- Expand the bias map to include more sources.

Author:
Mendelson8
GitHub: https://github.com/mendelson8
