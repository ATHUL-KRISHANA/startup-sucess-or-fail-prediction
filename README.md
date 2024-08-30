# Startup Success or Fail
The objective of the project is to predict whether a startup which is currently operating turn into a success or a failure. The success of a company is defined as the event that gives the company's founders a large sum of money through the process of M&A (Merger and Acquisition) or an IPO (Initial Public Offering). A company would be considered as failed if it had to be shutdown.

This problem will be solved through a Supervised Machine Learning approach by training a model based on the history of startups which were either acquired or closed. The trained model will then be used to make predictions on startups which are currently operating to determine their success/failure.

## Dataset
The dataset used for this project is sourced from Kaggle [https://www.kaggle.com/datasets/yanmaksi/big-startup-secsees-fail-dataset-from-crunchbase]. 
The dataset consists of 66,368 rows and 14 columns. The objective is to predict whether a currently operating startup will be successful or fail in the future. Success is defined as an event like a merger, acquisition (M&A), or initial public offering (IPO), while failure is defined as the startup shutting down. By analyzing various features within the dataset, we aim to develop a predictive model that can assess the likelihood of a startup's success or failure.

* Permalink: Unique link identifier for each startup.
* Name: The official name of the company.
* Homepage URL: The startup's official website.
* Category List: The industry or field in which the company operates.
* Funding Total USD: The total amount of funding the company has received, in USD.
* Status: The current operating status of the company (e.g., operating, closed).
* Country Code: The two-letter country code representing the location of the company.
* State Code: The state code indicating the company's location within a country.
* Region: The broader geographical region where the company is located.
* City: The city where the company is based.
* Funding Rounds: The number of funding rounds the company has undergone.
* first_founding_at: The data contain the date of the startup thodangale polenm
* Last Funding At: The date of the company's most recent funding round
## EDAVisualize the data using plots and graphs to identify trends, patterns, and correlations between features.
Perform EDA to gain insights into the dataset. This includes understanding the distribution, central tendencies, and relationships between different features.Visualize the data using plots and graphs to identify trends, patterns, and correlations between features.
## Feature Engineering
* Handle missing values:Identify missing values in the dataset.Decide on an appropriate strategy to handle missing data (e.g., imputation, removal).
* Feature Encoding:use Use encoding techniques (e.g., Label Encoding) to convert categorical features to numeric.
* Create new features: Interaction Features: Create features that are combinations of two or more existing features to capture interactions.Date/Time Features: Extract features like year, month, or day from date-time fields.
* Feature Scaling:Normalize or standardize features, especially if using algorithms sensitive to feature scales (e.g., SVM, KNN).I choose Standardization techniques.
## Model creation
* Train-Test Split:Split your data into training and test sets, ensuring that the split is stratified if necessary.
* Modeling with Success and Fail Data:Train your model using only the data labeled as success and fail.Evaluate the model performance using accuracy score and classification report
* Testing with Operating Data:Once the model is trained, use the operating data as a test set.Predict whether currently operating startups are more likely to succeed or fail.
I have tested a total of four algorithms on the model to determine the most effective accuracy score
* k-nearest neighbors
* Naive Bayes
* Support Vector Machine (SVM)
* Decision Tree
* Random Forest
After that test, i choose  Random Forest algorithm give more accuracy 
## Hyperparameter Tunning
I employed RandomizedSearchCV to fine-tune the hyperparameters of the random forest
## Model deployment 
* Set Up Flask Application:Import the necessary libraries, including Flask and any other dependencies (e.g., pickle, numpy, pandas, sklearn).
Initialize a Flask app using Flask(__name__).
* Load the Model:Load the trained model using pickle .Also load any preprocessing objects (e.g., encoders, scalers) that are required to prepare the input data.
Define Routes:Create an endpoint for predictions, typically using a POST method where users can send input data.
Define additional routes if needed for the homepage, documentation, etc.
* Handle Input Data:Display the categorical features in dropdown boxes within the Flask app's UI, then encode the selected values and scale the input data before passing it to the model for prediction.
* Run the Flask Server:Execute the app.py file to start the Flask server.Test the server locally by sending HTTP requests (e.g., via Postman or curl) to the prediction endpoint.

