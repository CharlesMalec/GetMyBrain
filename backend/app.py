from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import json
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

def init_db():
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS conversations
                     (id TEXT PRIMARY KEY, parent_id TEXT, question TEXT, response TEXT, timestamp TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS wiki
                     (id TEXT PRIMARY KEY, content TEXT, timestamp TEXT)''')
        conn.commit()

init_db()

def generate_followup_question(response, last_question):
    if last_question == "Which function shall we start with?":
        return "In which country do you perform this function?"
    elif last_question == "In which country do you perform this function?":
        return "What are the main workflows in your role?"
    else:
        return "Can you provide more details about the process?"

def update_wiki(function, country, details):
    content = f"# {function} Knowledge Base\n\n"
    content += f"## Country: {country}\n\n"
    content += f"### Details\n{details}\n"
    wiki_id = str(uuid.uuid4())
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO wiki (id, content, timestamp) VALUES (?, ?, ?)",
                  (wiki_id, content, datetime.now().isoformat()))
        conn.commit()
    return wiki_id, content

@app.route('/start', methods=['POST'])
def start_conversation():
    conversation_id = str(uuid.uuid4())
    question = "Which function shall we start with?"
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO conversations (id, question, timestamp) VALUES (?, ?, ?)",
                  (conversation_id, question, datetime.now().isoformat()))
        conn.commit()
    return jsonify({"conversation_id": conversation_id, "question": question})

@app.route('/respond', methods=['POST'])
def respond():
    data = request.json
    response = data.get('response')
    last_question = data.get('last_question')
    parent_id = data.get('parent_id')
    new_conversation_id = str(uuid.uuid4())
    next_question = generate_followup_question(response, last_question)
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO conversations (id, parent_id, question, response, timestamp) VALUES (?, ?, ?, ?, ?)",
                  (new_conversation_id, parent_id, next_question, response, datetime.now().isoformat()))
        conn.commit()
    wiki_update = None
    if last_question == "Can you provide more details about the process?":
        c.execute("SELECT response FROM conversations WHERE id = ?", (parent_id,))
        country = c.fetchone()[0]
        c.execute("SELECT response FROM conversations WHERE parent_id = ?", (parent_id,))
        function = c.fetchone()[0]
        wiki_id, wiki_content = update_wiki(function, country, response)
        wiki_update = {"wiki_id": wiki_id, "content": wiki_content}
    return jsonify({
        "conversation_id": new_conversation_id,
        "question": next_question,
        "wiki_update": wiki_update
    })

if __name__ == '__main__':
    app.run(debug=True)