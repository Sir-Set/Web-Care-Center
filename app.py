from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(_name_)

client = genai.Client(api_key="AIzaSyCgh27HsU_qTlYo6r3ZKhgX6MekNfzsSn0")

@app.route('/')
def index():
    return render_template('OG.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form.get('message')

    try:
        if "name" in user_message.lower() or "who am i" in user_message.lower():
            bot_response = "I'm Chloe, WebCare Assistant."
        elif "exit" in user_message.lower():
            bot_response = "Goodbye! Have a great day!"
        else:
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=user_message
            )
            
            bot_response = response.text

    except Exception as e:
        bot_response = f"Error: {str(e)}"
    
    return jsonify(answer=bot_response)

if _name_ == '_main_':
    app.run(debug=True)