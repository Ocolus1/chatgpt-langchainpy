from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    note = """"
    <div>
        <h1>To send a request to the API</h1>
        <p>Send a POST request to <code>/api/v1</code> with the following JSON payload:</p>
        <pre> 
            { "prompt" : "Hi there!" }
        </pre>
        <p> Where "Hi there" can be the prompt you want to send</p>
        <h5>Use this curl request</h5>
        <p> curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Hi there!"}' http://localhost:5000/api/v1 </p>
        <h2>You will get a response like this. Though it might not be exact cause it is AI</h2>
        <pre> 
            { "response": " Hi there! It's nice to talk to you. How are you today?" }
        </pre>
    </div>
    """
    return f'{note}'


@app.route('/api/v1', methods=['POST'])
def api_v1():
    try:
        # get the prompt from the JSON payload
        prompt = request.json['prompt']
        print("Received prompt: " + prompt)

        # Set the level of randomness of response from 0 - 1
        # 0 being the most deterministic and 1 being the most random
        llm = OpenAI(temperature=0.9)

        # Instantiate the BufferMemory and ConversationChain
        # passing the memory key for storing state
        conversation = ConversationChain(
            llm=llm, verbose=True, memory=ConversationBufferMemory())

        # gets the response from the AI
        response = conversation.predict(input=f"{prompt}")

        # return the response as JSON
        return jsonify({"response": response})

    except Exception as e:
       
        print("Error: ", e)
        response = "Connection error, please try again later."

        # return the response as JSON
        return jsonify({"Error": response})


if __name__ == '__main__':
    app.run()
