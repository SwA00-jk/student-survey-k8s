from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        data = {
            'firstName': request.form.get('firstName'),
            'lastName': request.form.get('lastName'),
            'street': request.form.get('street'),
            'city': request.form.get('city'),
            'state': request.form.get('state'),
            'zip': request.form.get('zip'),
            'telephone': request.form.get('telephone'),
            'email': request.form.get('email'),
            'surveyDate': request.form.get('surveyDate'),
            'likes': ', '.join(request.form.getlist('likes')),
            'source': request.form.get('source'),
            'comments': request.form.get('comments')
        }

        # Save to CSV file
        file_exists = os.path.isfile('survey_responses.csv')
        with open('survey_responses.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

        return f"<h3>Thank you, {data['firstName']}! Your response has been saved.</h3>"

    return render_template('survey.html')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')


