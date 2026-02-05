# article-news-summarize-using-streamlit

a beginner-friendly streamlit app for text summarization. Its a web application to summarize long news articles into 3–5 key sentences using a T5-based NLP model. 

The application work best with English news or article. But you are very welcome to experiment with other languages.

---

## Features
- Paste long news articles or texts
- Quick demo with sample news
- Adjustable minimum and maximum summary length
- user-friendly interface
- Abstractive text summarization using T5

---

## Model
This application uses a **T5 (Text-To-Text Transfer Transformer)** model for abstractive summarization.

The model is capable of:
- Condensing long articles into concise summaries
- Preserving key information and meaning

---

## Tech Stack
- Python
- Streamlit
- Hugging Face Transformers (T5)
- Custom CSS (embedded in Python)

---

## How to Run the App

### 1️. Clone the repository
```bash
git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer
```

### 2️. Install dependencies
```bash
pip install -r requirements.txt
```

### 3️. Run the application
```bash
streamlit run app.py
```

---

## Project Structure
```text
├── app.py
├── src/
│   └── summarizer.py
├── requirements.txt
└── README.md
```

---

## User Interface
The interface is designed with:
1. Indie Flower font for a friendly and casual look
2. Soft pastel color palette for visual comfort
3. Card-based layout for clarity and readability
The design aims to be:
1. Easy on the eyes
2. Simple and intuitive
3. Suitable for academic and demo purposes

---

## NOTES
1. Best results are obtained with 200–1000 words input text
2. This project is intended for educational and demonstration purposes
3. Optimized for English text. Other languages may work with limited accuracy

---

## Acknowledgements
1. Hugging Face for providing the T5 model
2. Streamlit for the rapid application framework
