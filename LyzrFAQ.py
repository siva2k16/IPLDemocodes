import os
os.environ['OPENAI_API_KEY'] = 'ABC' #userdata.get('OPENAI_API_KEY')
from lyzr import ChatBot

my_chatbot = ChatBot.pdf_chat(input_files=["/content/sample_data/CS_Support_FAQ.pdf"])
response = my_chatbot.chat("What is cancellation process?")
print(response)
