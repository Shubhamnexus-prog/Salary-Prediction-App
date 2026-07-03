# Salary Prediction App

A Machine Learning web application that predicts salary based on years of experience using Linear Regression.

## Project Overview

This project uses a Linear Regression model trained on the Salary Dataset to estimate a person's salary from their years of professional experience.

## Features

* Predict salary based on years of experience
* Interactive web interface using Streamlit
* Trained using Scikit-learn Linear Regression
* Simple and user-friendly design

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

## Project Structure

```text
Salary-Prediction-App/
│
├── app.py
├── linear_regression_model.pkl
├── Salary_Data.csv
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/salary-prediction-app.git
```

2. Navigate to the project folder:

```bash
cd salary-prediction-app
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will start and open in your browser.

## Dataset

The dataset contains:

* YearsExperience
* Salary

The model learns the relationship between experience and salary using Linear Regression.

## Sample Prediction

| Years of Experience | Predicted Salary |
| ------------------- | ---------------- |
| 2                   | ₹45,000          |
| 5                   | ₹75,000          |
| 10                  | ₹1,20,000        |

*Values are examples and may vary depending on the trained model.*

## Future Improvements

* Deploy on Streamlit Cloud
* Add advanced salary prediction models
* Improve UI/UX
* Support multiple input features

## Author

Shubham Gupta

## License

This project is open source and available under the MIT License.
