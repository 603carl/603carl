
# Scribe Spectrum Chatbot

## Overview
The Scribe Spectrum Chatbot is a Python-based interactive chatbot designed to assist users with information about the services offered by Scribe Spectrum Agency. Built with Tkinter, it features a GUI that allows users to select services and receive detailed information instantly.

## Features
- **Service Information:** Provides detailed descriptions of services like Essay Writing, Research Papers, Thesis Writing, and Online Classes.
- **User-Friendly Interface:** Simple and interactive GUI built using Tkinter.
- **Expandable:** Capable of incorporating more advanced NLP techniques and machine learning models.

## Installation

### Prerequisites
- **Python:** Ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/).
- **Virtual Environment (Optional but recommended):** To avoid conflicts with other Python projects, set up a virtual environment.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/scribe-spectrum-chatbot.git
   cd scribe-spectrum-chatbot
   ```

2. **Set Up Virtual Environment (Recommended):**
   - On **Windows**:
     ```bash
     python -m venv chatbot_env
     chatbot_env\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     python3 -m venv chatbot_env
     source chatbot_env/bin/activate
     ```

3. **Install Required Libraries:**
   ```bash
   pip install nltk spacy tensorflow
   ```

4. **Download NLTK and spaCy Data:**
   ```bash
   python
   import nltk
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   exit()
   python -m spacy download en_core_web_sm
   ```

5. **Run the Chatbot:**
   ```bash
   python scribe_spectrum_chatbot.py
   ```

## Usage
Once the chatbot is running, users can select a service from the dropdown menu and interact with the chatbot to get information about Scribe Spectrum's services.

## Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome, especially for expanding the chatbot's functionality with more advanced NLP and machine learning features.

## License
This project is licensed under the MIT License.
