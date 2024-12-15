# Hackathon

# Automated Python Testing Framework with Streamlit

## Overview

This repository contains a **Streamlit** application that leverages **GPT-4** (via the GPT-4o model) to build an automated Python testing framework for website functionalities. The application integrates popular libraries like **NLTK**, **Playwright**, **Selenium**, and **pytest** to streamline the process of creating and running robust web tests. 

The tool is designed for developers and QA engineers who want to quickly generate and execute test scripts based on AI-generated logic for website automation and functional testing.

---

## Features

- **AI-Driven Test Generation**: Generates Python test scripts using GPT-4o tailored for your website's functionality.
- **Web Automation Support**:
  - **Selenium**: Automates browser interactions.
  - **Playwright**: Offers modern, fast, and reliable cross-browser automation.
- **Natural Language Processing**:
  - Utilizes **NLTK** for processing and tokenizing user inputs and generating meaningful outputs.
- **End-to-End Testing**:
  - Tests are executed with **pytest**, ensuring clean and maintainable test cases.
- **Streamlit UI**:
  - Intuitive interface for generating, reviewing, and running test scripts.

---

## Prerequisites

1. **Python Version**: Python 3.8 or above.
2. **Dependencies**:
   - Streamlit
   - NLTK
   - Selenium
   - Playwright
   - pytest
   - OpenAI's GPT API (configured for GPT-4o)

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### Step 3: Install Dependencies
Install all the required libraries using `pip`:
```bash
pip install -r requirements.txt
```

### Step 4: Configure GPT API Key
Create a `.env` file in the root directory and add your OpenAI GPT API key:
```
OPENAI_API_KEY=your_openai_api_key
```

### Step 5: Install NLTK Data
To avoid errors when running NLTK-based functions, download necessary NLTK datasets:
```python
import nltk
nltk.download('punkt')
```

### Step 6: Install Playwright Drivers
Initialize Playwright to download required browser drivers:
```bash
playwright install
```

---

## Running the Application

1. Run the **Streamlit** application:
   ```bash
   streamlit run main.py
   ```

2. Open your browser and navigate to the URL provided by Streamlit (e.g., `http://localhost:8501`).

---

## Usage

### Key Functionalities:
- **Input Functional Requirements**: Provide website functionalities as input.
- **Generate Test Scripts**: AI generates Selenium/Playwright test scripts.
- **Run Tests**: Execute tests directly from the UI using pytest.
- **Review Logs**: Analyze test results and logs within the app.

---

## Running Tests Manually

To run the generated test scripts outside the Streamlit app, use the following command:
```bash
pytest path/to/your/tests --html=report.html
```
---

## Contributing

Contributions are welcome! If you’d like to add new features or fix bugs:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **OpenAI** for the GPT-4 model.
- **Streamlit** for the interactive UI framework.
- **Selenium & Playwright** for browser automation.
- **pytest** for testing capabilities.
- **NLTK** for text processing. 

---
