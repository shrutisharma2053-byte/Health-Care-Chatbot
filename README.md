# Health-Care-Chatbot

# 🏥 Healthcare Assistant

## 📌 Project Overview

The **Healthcare Assistant** is a simple web-based application developed using Python and Streamlit. It collects basic user information, including age, gender, height, weight, and symptoms, to calculate Body Mass Index (BMI) and provide general self-care suggestions for common health complaints.

The application aims to make basic health information easily accessible through a simple and user-friendly interface.

## ✨ Features

- **User Information:** Collects age, gender, height, and weight.
- **BMI Calculator:** Calculates BMI based on the user's height and weight.
- **BMI Classification:** Categorizes BMI as underweight, healthy weight, overweight, or obese.
- **Symptom Analysis:** Identifies supported symptoms from the user's description.
- **Self-Care Suggestions:** Provides general self-care information for common complaints.
- **Age-Based Guidance:** Displays additional cautionary advice for users above 50.
- **Interactive Interface:** Built with Streamlit for easy use.

## 🩺 Supported Symptoms

The application currently supports the following symptoms:

- Cold
- Fever
- Headache
- Cough
- Stomach pain
- Sore throat
- Fatigue
- Body pain

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **BMI Calculation:** Python mathematical operations
- **Data Storage:** Python dictionary for predefined self-care suggestions

```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.9 or later
- pip package manager
- Git (optional, for cloning the repository)

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

### Step 2: Navigate to the project directory

```bash
cd Healthcare-Assistant
```

### Step 3: Install the dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install Streamlit directly:

```bash
pip install streamlit
```

### Step 4: Run the application

```bash
python -m streamlit run app.py
```

### Step 5: Open the application

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 📊 How It Works

1. The user enters their age, gender, height, and weight.
2. The user describes their symptoms in the text area.
3. The application searches for supported symptom keywords.
4. It calculates the user's BMI using height and weight.
5. It displays the BMI category and corresponding self-care suggestion when a supported symptom is found.
6. If no supported symptom is identified, the application recommends consulting a healthcare professional.

## 🧮 BMI Formula

BMI is calculated using the following formula:

**BMI = Weight (kg) / [Height (m)]²**

For example, if the weight is 60 kg and the height is 1.65 m:

```text
BMI = 60 / (1.65 × 1.65)
BMI = 22.0
```

The application uses standard adult BMI categories. BMI interpretation for children and teenagers requires age- and sex-specific assessment, so the current adult classification should not be applied to them.

## 🚀 Future Enhancements

- Integrate Natural Language Processing (NLP) for improved symptom understanding.
- Add a larger and medically reviewed self-care knowledge base.
- Improve input validation and error handling.
- Add multilingual support.
- Develop a responsive user interface.
- Integrate secure user authentication if user accounts become necessary.
- Add links to trusted healthcare resources.

## ⚠️ Disclaimer

This application is intended for educational purposes and provides general health information only. It does not diagnose diseases, replace professional medical advice, or prescribe treatment. Self-care suggestions may not be suitable for every individual. Consult a qualified healthcare professional for medical concerns, and seek urgent care for severe or worsening symptoms.

## 👨‍💻 Author

**Shruti Sharma**



## 📄 License

This project is available for educational and learning purposes. Add an appropriate open-source license, such as the MIT License, if you intend to permit others to reuse and modify the code.
