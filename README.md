# Salary Prediction using Linear Regression

This web application predicts salaries based on years of experience using Linear Regression. It is built with Python, Flask, and scikit-learn. Users can input their years of experience into the interactive interface to get a salary prediction.

## Features

- **Predict Salary:** Users can input their years of experience, and the app will predict the corresponding salary using a linear regression model.
- **Interactive Visualization:** The app also displays a scatter plot of the salary vs. years of experience, with a regression line showing the trend.
- **Model Evaluation:** The app uses a simple linear regression model to predict salaries and evaluates it based on the R² score, which is displayed on the web page.

## Technologies Used

- **Flask:** Web framework to create the application.
- **Pandas:** Data handling and manipulation.
- **NumPy:** Numerical computations.
- **scikit-learn:** Machine learning library for linear regression and model evaluation.
- **Matplotlib:** For plotting graphs.
- **HTML/CSS:** For building the front-end of the app.

## Project Setup

### Prerequisites

Before running the app, make sure you have the following installed:

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/varun-005/SalaryEstimator.git
cd SalaryEstimator
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the necessary libraries:

```
Flask==2.1.2
pandas==1.4.2
scikit-learn==1.0.2
matplotlib==3.5.1
```

3. Place the `Salary_Data.csv` file in the project directory (or change the path in the code to match your file location).

4. Run the Flask application:

```bash
python app.py
```

This will start a local server (typically on `http://127.0.0.1:5000/`), where you can interact with the application.

## How to Use

1. Open the application in a web browser.
2. Enter the number of years of experience in the input box.
3. Click the "Predict Salary" button.
4. The predicted salary will be displayed, and the regression plot will be shown.

## Model Evaluation

- The app uses the R² score to evaluate the performance of the linear regression model. The R² score indicates how well the model explains the variance of the data.

## Contribution

Feel free to fork the repository, contribute, or create an issue if you find any bugs or want to suggest improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
