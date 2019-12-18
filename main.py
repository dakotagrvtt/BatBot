from chatterbot import ChatBot

chatbot = ChatBot("Batman", read_only=False)

while True:
    request = input('You: ')
    response = chatbot.get_response(request)

    print('Batman: ', response)
