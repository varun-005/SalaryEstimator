from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load data (you can change the file path to your local file if needed)
df = pd.read_csv("Salary_Data.csv")

# Prepare the data (split into X for years of experience and y for salary)
X = df["YearsExperience"].values.reshape(-1, 1)  # Convert to a column
y = df["Salary"].values

# Create a model and train it using the data
model = LinearRegression()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():
    predicted_salary = None  # This will hold the salary prediction

    if request.method == "POST":
        # Get the user input (years of experience)
        years_experience = float(request.form.get("years_experience"))
        
        # Use the model to predict salary based on input
        predicted_salary = model.predict([[years_experience]])[0]
        predicted_salary = round(predicted_salary, 2)  # Round the result

    # Generate the plot of salary vs experience
    fig, ax = plt.subplots()
    ax.scatter(df["YearsExperience"], df["Salary"], color="blue", label="Data Points")
    ax.plot(df["YearsExperience"], model.predict(X), color="red", label="Regression Line")
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary")
    ax.set_title("Salary vs Experience")
    ax.legend()

    # Convert the plot to an image to show on the webpage
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plot_data = base64.b64encode(buf.getvalue()).decode()
    buf.close()

    # Render the HTML template with the plot and prediction
    return render_template("index.html", predicted_salary=predicted_salary, plot_url=plot_data)

if __name__ == "__main__":
    app.run(debug=True)
