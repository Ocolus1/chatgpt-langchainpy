ChatGPT & langchain example for flask app
=======================================

This repository contains code from [this tutorial](https://langchain.readthedocs.io/en/latest/getting_started/getting_started.html) modified to use the ChatGPT language model, trained by OpenAI, in a flask project using langchain an API for language models. The prompt is also slightly modified from the original. 😉

Getting started
To use this code, you will need to have a OpenAI API key. If you don't have one yet, you can get one by signing up at https://platform.openai.com

Once you have your API key, clone this repository and add the following with your key to `config/env`:

```
OPENAI_API_KEY={YOUR_API_KEY}
```


```
git clone https://github.com/Ocolus1/chatgpt-langchainpy.git
cd chatgpt-langchainpy
```

Then create a virtual environment

```
python -m venv env
source env/scripts/activate
```

Install Dependencies

```
pip install -r requirements.txt
```
To run the app

```
flask --app app run
```
