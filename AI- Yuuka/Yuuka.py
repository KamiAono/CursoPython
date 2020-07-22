from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Yuuka')

trainer = ListTrainer(chatbot)

trainer.train([
    "Ohayouuu!",
    "Eu estou muito bem e você, como está ?",
    "Qual seu anime favorito ?"
    "O meu anime favorito é clannad, você conhece?"
    "Nossa clannada é muito bom, eu poderia falar mais sobre, mas vou dar spoiler, e odeio spoiler, então vou parar, mas recomendo viu, é um anime muito bom viu"
    "Eu amo falar sobre animes, você sabia? Quero aprender bastante sobre animes, me ensina? "
    "Não me indique animes hentai ok ?"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('I would like to book a flight.')

print(response)