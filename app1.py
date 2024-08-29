from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model, label encoders, scaler, and data
model = pickle.load(open('randomforest_without.pkl', 'rb'))
label_encoders = pickle.load(open('sample_encoders.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
df = pickle.load(open('test_values.pkl', 'rb'))  # Load the pickled dataframe

@app.route('/')
def home():
    # Extract unique values for the selection boxes
    unique_values = {
        'country_code': df['country_code'].unique(),
        'city': df['city'].unique(),
        'region': df['region'].unique(),
        'state_code': df['state_code'].unique(),
        'category_list': df['category_list'].unique(),
    }
    return render_template('sample.html', unique_values=unique_values)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    form_data = request.form.to_dict()

    # Prepare the data for prediction
    data = [
        form_data['category_list'],
        form_data['funding_total_usd'],
        form_data['country_code'],
        form_data['state_code'],
        form_data['region'],
        form_data['city'],
        form_data['funding_rounds'],
        form_data['age_of_company'],
        form_data['years_since_last_funding'],
        form_data['years_since_first_funding']
    ]

    # Convert to DataFrame with the specified column order
    input_df = pd.DataFrame([data], columns=[
        'category_list', 'funding_total_usd', 'country_code', 'state_code',
        'region', 'city', 'funding_rounds', 'age_of_company',
        'years_since_last_funding', 'years_since_first_funding'
    ])

    # Apply label encoding
    for column in ['country_code', 'state_code', 'region', 'category_list', 'city']:
        input_df[column] = label_encoders[column].transform(input_df[column])
    print(input_df)
    # Apply scaling
    scaled_data = scaler.transform(input_df)
    print(scaled_data)
    # Predict the outcome
    prediction = model.predict(scaled_data)
    output=prediction[0]
    print(output)
    # Map prediction to a readable output

    # Re-render the form with the prediction result
    unique_values = {
        'country_code': df['country_code'].unique(),
        'city': df['city'].unique(),
        'region': df['region'].unique(),
        'state_code': df['state_code'].unique(),
        'category_list': df['category_list'].unique(),
    }
    return render_template('sample.html', unique_values=unique_values, prediction_text=f'The predicted outcome is: {output}')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
