# 🌙 Student Wellbeing Lab

Explore how daily habits and digital lifestyle relate to a model-estimated student wellbeing score. **Student Wellbeing Lab** is a machine learning web application built with Python and Streamlit that lets users enter lifestyle information and visualize a predicted score on a scale of 0–10.

## 🚀 Live Demo

🔗 **[Try Student Wellbeing Lab](https://student-wellbeing-score.streamlit.app/)**


## 📸 Screenshots

### 1. Student Wellbeing Dashboard

![Student Wellbeing Dashboard](https://github.com/user-attachments/assets/359a443d-ba1d-4113-96ad-480db498127a)

![Student Wellbeing Dashboard - Full Form](https://github.com/user-attachments/assets/cb2f6e5d-04bb-43b9-95dd-abc5525ba722)

### 2. Wellbeing Score Prediction

![Wellbeing Score Prediction](https://github.com/user-attachments/assets/80498969-ebc1-45bd-8be0-d4983810e4c6)

## ✨ Features

- 👤 **Personal Information:** Enter age, gender, country, and academic level.
- 🌿 **Daily Routine:** Provide sleep duration, study hours, physical activity, and stress level.
- 📱 **Digital Habits:** Enter social media usage, daily phone unlocks, preferred platform, and main purpose of use.
- 🤖 **Machine Learning Prediction:** Generate a wellbeing score using a trained model.
- 📊 **Interactive Gauge:** Visualize the predicted score using a semi-circular style gauge.
- 🎨 **Modern UI:** Dark navy background, purple accents, and a compact side-by-side layout.
- ☁️ **Web Deployment:** Access the application through Streamlit Community Cloud.

## 🛠️ Tech Stack

- **Python** — Application logic
- **Streamlit** — Web application framework
- **Pandas** — Input data preparation
- **Scikit-learn** — Machine learning model
- **Joblib** — Loading the trained model
- **Plotly** — Interactive gauge visualization

## ⚙️ How It Works

1. The user enters personal, academic, lifestyle, and digital habit information.
2. The application organizes the inputs into a Pandas DataFrame.
3. The trained machine learning model generates a prediction.
4. The predicted value is constrained to the 0–10 range.
5. Plotly displays the result in a gauge.

**Note:** The score is a model estimate, not a clinical mental health assessment or diagnosis.

## 📂 Project Structure

```text
student-wellbeing/
│
├── app.py
├── Mental_Health_Model.pkl
├── requirements.txt
├── Mental_Health_Model.ipynb
├── Student Social Media And Mental Health Impact.csv
├── README.md
└── Screenshots/
    ├── student-wellbeing-1.png
    └── student-wellbeing-2.png
```

## 📋 Requirements

Install the dependencies listed in `requirements.txt`. The deployed application uses the trained model file `Mental_Health_Model.pkl`.

Example dependencies:

```text
streamlit
pandas
joblib
plotly
numpy
scipy
scikit-learn
```

Use the compatible package versions configured for your trained model and deployment environment.

## 💻 Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/libta018/student-wellbeing.git
cd student-wellbeing
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the Streamlit application**

```bash
streamlit run app.py
```

The application will display a local URL in your terminal.

## 🔮 Future Improvements

- Add more lifestyle insights and visualizations.
- Improve model evaluation and validation.
- Add input validation and user-friendly error messages.
- Enhance mobile responsiveness and accessibility.
- Document model performance using appropriate evaluation metrics.

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes. Its predictions should not be used as a substitute for professional mental health advice, diagnosis, or treatment.

## 👨‍💻 Author

**Mohammed Talib**

- GitHub: [libta018](https://github.com/libta018)
- LinkedIn: [Mohammed Talib](https://www.linkedin.com/in/mohammed-talib-analytics-ds)
- Live Demo: [Student Wellbeing Lab](https://student-wellbeing-score.streamlit.app/)

---

⭐ If you find this project useful, consider starring the repository!

