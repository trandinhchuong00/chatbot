from chatterbot import ChatBot
from flask import Flask, render_template, request

app = Flask(__name__)

botname='ChatBot'
chatbot = ChatBot(botname, 
	logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I have not yet learnt how to answer that',
            'maximum_similarity_threshold': 0.8
        }
    ],
 )

@app.route("/")
def home():
    return render_template("index.html", botname=botname)

@app.route("/get")
def get_bot_response():
	userInput=request.args.get('msg')
	return str(chatbot.get_response(userInput))

if __name__ == '__main__':
	app.run(port=5500)
