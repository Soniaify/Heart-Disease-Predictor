Heart Disease Prediction App

This is a very simple web app that helps you know if someone might have **heart disease**.

You just enter a few health details (like age, chest pain, blood pressure, etc.), and it will say:
No heart disease
Mild heart disease
Moderate heart disease
Severe heart disease
very severe heart disease

It’s like a friendly robot that checks your heart! 

        What You Need

Before you run the app, make sure these are installed:

- Python 3
- Flask → `pip install flask`
- Joblib → `pip install joblib`
- Scikit-learn → `pip install scikit-learn`
- A trained model file → `heart_model.pkl`

        What Each Feature Means

These are the things you’ll type into the form. Here's what they mean:

| Feature Name    | **What It Means (Like you're 5 years old) |
|----------------------|----------------------------------------------|
| `age`                | How old the person is |
| `sex`                | Male, Female |
| `(chest pain)`       | Type of chest pain |
| `trestbps`           | Resting blood pressure  (when sitting still) |
| `chol`               | Cholesterol level  (fat in blood) |
| `fbs`                | Is blood sugar > 120?  (True, False) |
| `restecg`            | Heart’s electrical signal test 0 = Normal, ST-T Wave Abnormality |
| `thalach`            | Highest heart rate while exercising  |
| `exang`              | Chest pain from exercise?  (Yes, No) |
| `oldpeak`            | Difference between rest and exercise ECG test  |
| `slope`              | The slope of heart line in test graph :Upsloping, Flat, Downsloping |
| `ca`                 | Number of colored blood vessels (0–3) seen in scan  |
| `thal`               | Type of heart scan result: Normal, Fixed Defect, Reversible Defect |

            Project Structure

Heart_disease/
│
├── app.py  
├── heart_disease_multiclass.csv
├── heart_disease.ipynb             
├── heart_model.pkl     
├── templates/
│   └── index.html     
│   └── guide.html
└── README.md          

