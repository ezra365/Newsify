from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Database initialization
conn = sqlite3.connect('feedback.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS feedback
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              url TEXT,
              summary TEXT,
              rating TEXT,
              comment TEXT)''')
conn.commit()
conn.close()

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    url = data['url']
    summary = data['summary']
    rating = data['rating']
    comment = data.get('comment', '')

    # Store feedback in the database
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("INSERT INTO feedback (url, summary, rating, comment) VALUES (?, ?, ?, ?)",
              (url, summary, rating, comment))
    conn.commit()
    conn.close()

    return jsonify({"message": "Feedback submitted successfully!"})

@app.route('/view_feedback', methods=['GET'])
def view_feedback():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("SELECT * FROM feedback")
    feedback_data = c.fetchall()
    conn.close()

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

if __name__ == '__main__':
    app.run(debug=True)
