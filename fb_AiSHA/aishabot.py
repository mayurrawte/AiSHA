from chatterbot import ChatBot

AiSHAbot = ChatBot(
    'AiSHA',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
AiSHAbot.train("chatterbot.corpus.english")

