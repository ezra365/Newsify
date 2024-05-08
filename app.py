from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Connect to the PostgreSQL database using the Heroku DATABASE_URL
DATABASE_URL = 'postgres://ohmzvcmsviurnx:948bb8a0626aeffadf223a3e27b5aead9ffea52bc5f981cd8a110cf6087ef98c@ec2-52-72-109-141.compute-1.amazonaws.com:5432/d20q4tjrv08pk3'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

# Create the feedback table if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS feedback
                (id SERIAL PRIMARY KEY, url TEXT, summary TEXT, rating TEXT, comment TEXT)''')
conn.commit()

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    url = data['url']
    summary = data['summary']
    rating = data['rating']
    comment = data.get('comment', '')

    # Store feedback in the database
    cur.execute("INSERT INTO feedback (url, summary, rating, comment) VALUES (%s, %s, %s, %s)", (url, summary, rating, comment))
    conn.commit()

    return jsonify({"message": "Feedback submitted successfully!"})

@app.route('/view_feedback', methods=['GET'])
def view_feedback():
    cur.execute("SELECT * FROM feedback")
    feedback_data = cur.fetchall()

    feedback_list = []
    for feedback in feedback_data:
        feedback_dict = {
            "id": feedback[0],
            "url": feedback[1],
            "summary": feedback[2],
            "rating": feedback[3],
            "comment": feedback[4]
        }
        feedback_list.append(feedback_dict)

    return jsonify({"feedback": feedback_list})

@app.route('/sync_feedback', methods=['POST'])
def sync_feedback():
    data = request.get_json()
    feedback_data = [(f['url'], f['summary'], f['rating'], f['comment']) for f in data['feedback']]

    cur.executemany("INSERT INTO feedback (url, summary, rating, comment) VALUES (%s, %s, %s, %s)", feedback_data)
    conn.commit()

    return jsonify({"message": "Feedback synchronized successfully!"})

if __name__ == '__main__':
    app.run(debug=True)