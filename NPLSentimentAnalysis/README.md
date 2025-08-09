# NPLSentimentAnalysis

A sentiment analysis application built with natural language processing (NLP) techniques and powered by Flask. This project evaluates the emotional tone of Spanish-language text, with potential applications in social media monitoring, customer feedback, and ethical AI research.

---

## Features

- Classifies text into sentiment categories: positive, negative, neutral
- Web interface built with Flask for input and visualization
- Modular NLP components for easy extension and customization
- Supports multiple input sources (manual text, files, APIs)
- Scalable structure for training and deploying custom models

---

## Technologies Used

- Python 3.10+
- Flask
- NLTK / spaCy / TextBlob (depending on configuration)
- HTML/CSS for frontend templates
- Git & GitHub for version control



## Installation

1. Clone the repository:

```bash
git clone https://github.com/Rojasoterom/ia-prototype-collection.git
cd ia-prototype-collection/NPLSentimentAnalysis

## Create a virtual Enviroment

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

## Install dependencies:

pip install -r requirements.txt

## Run Locally

python server.py
(Then open your browser at http://localhost:5000)

## Licence

This project is licensed under the MIT License. See the LICENSE file for details
