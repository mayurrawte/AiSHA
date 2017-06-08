from chatterbot import ChatBot

AiSHABot = ChatBot('AiSHA', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
AiSHABot.train("chatterbot.corpus.english")
