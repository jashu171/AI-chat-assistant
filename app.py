from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from qwen3 import QwenChatbot
import os

app = Flask(__name__, 
    static_folder='static',
    template_folder='templates'
)
CORS(app)
chatbot = QwenChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/chat', methods=['POST']) 
def chat():
    try:
        user_input = request.json.get('message', '')
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400
            
        bot_response = chatbot.generate_response(user_input)
        return jsonify({'response': bot_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('static') or path == 'chat':
        return '', 404
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the static and templates directories exist
    os.makedirs('static', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    # Run the Flask app
    app.run(debug=True, port=3000)
