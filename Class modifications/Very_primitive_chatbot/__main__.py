import random
from difflib import SequenceMatcher
from itertools import product as it_product

class Log(list):
    def __getitem__(self, index):
        """Extend allow draw various indexes of data with tuples."""
        if isinstance(index, tuple):
            return [self[i] for i in index]
        return super().__getitem__(index)

    def fit(self, division):
        """Extend allow to fit heading part of contained data"""
        self = self[len(logged)//division:]

class Sentence(object):
    def __init__(self, string):
        self.sentence = string
    
    def __str__(self):
        return str(self.sentence)
    
    def input_(self, msg):
        """Extend allow to hold one changing object for various strings."""
        self.sentence = input(msg)
        
    def simplify(self):
        #Bot rules to simplify analyse
        self.sentence = self.sentence.lower()
        self.sentence.strip()
        self.sentence.replace("'re", " are")
        self.sentence.replace("'s", " is")
        self.sentence.replace("'m", " am")
    
    def is_empty(self):
        return not bool(self.sentence)
        
    def select_most_similar(self, schema_user, schema_bot, tolerance="Medium"):
        """Returns tuple with `(value, answer)`.
        Value precise how strong sentence was similar to schema."""
        tolerancies = { "High": (0.5, 0.8),
                        "Medium": (0.3, 0.7),
                        "Low": (0.1, 0.5)}
        low_tolerance, med_tolerance = tolerancies.get(tolerance)
        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()
        similarity = []
        for quest_schema in schema_user:
            similarity.append(similar(quest_schema, self.sentence))
        max_similary = max(similarity)
        
        if max_similary < low_tolerance:
            return 0.0, None
        elif max_similary < med_tolerance:
            return max_similary, "Do you mean ,,"+schema_user[similarity.index(max_similary)]+"'' ?"
        else:
            if len(schema_bot) > 1: 
                return max_similary, schema_bot[similarity.index(max_similary)]
            else:
                return max_similary, schema_bot[0]
            
    def calculate_similarity(self, schema_user):
        """Returns similarity. Value precise how strong sentence is similar to schema."""
        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()
        similarity = []
        for quest_schema in schema_user:
            similarity.append(similar(quest_schema, self.sentence))
        return max(similarity)
        
class Bot_remember:
    def __init__(self):
        self.data = {}
        
    def get_data(self, attr):
        return self.data.get(attr, "I don't know.")
        
    def set_data(self, attr, value):
        self.data[attr] = value
        
    def is_exist(self, attr):
        if self.data.get(attr, False):
            return True
        return False
        
class Bot_data:
    def search_question(self, arg):
        if arg in self.get_greetings():
            return self.get_greet_resp()[self.get_greetings().index(arg)]
        if arg in self.get_questions():
            return self.get_quest_answ()[self.get_questions().index(arg)]
        if arg in self.get_complements():
            return self.get_greet_resp()[self.get_complements().index(arg)]
        return "I totally don't know, to what are you talking about."
    
    @staticmethod
    def get_greetings():
        return ("hello", "hi", "greetings", "hey", "wassup", "welcome")
    @staticmethod
    def get_greet_resp():
        return ("Hey.", "Hello.", "Wassup.")
        
    @staticmethod
    def get_questions():
        return ("how are you?", "what are you doing?", "how is weather today?")
    @staticmethod
    def get_quest_answ():
        return ("I'm tine, thank you.", "Nothing interesting.", "The weather is nice.")
    
    @staticmethod
    def get_complements():
        return ("you are look nice.", "you changed hair?", "you looks fit.")
    @staticmethod
    def get_compl_answ():
        return ("Thanks mate!", "No, i wasn't.", "Thank you, but i don't have body lier :D.")

    @staticmethod
    def get_congratulations():
        return ("gratz", "congratulations bro.", "so nice")
    @staticmethod
    def get_cngrt_answ():
        return ("For what?", "Thanks mate!", "It's just me. ;)")

    @staticmethod
    def get_responds_yes():
        return ("yea", "yes", "exactly", "sure", "yes i am")
        
    @staticmethod
    def get_name():
        return ("i am NAME", "my name is NAME", "hi, my name is NAME", "hi, i am NAME")
        
    @staticmethod
    def get_own_name_ask():
        return ("What is my name?", "How i named?", "My name is?")

class ChatBot:
    bot_data = Bot_data()
    log_user = Log()
    log_bot = Log()
    memory_bot = Bot_remember()
    
    def __init__(self):
        """Initialize necessary data and methods for bot."""
        self.sentence = Sentence("")
        self.dialog = Dialog_manager()
        
    def mainloop(self):
        while True:
            self.sentence.input_("You: ")
            self.sentence.simplify()
            if self.sentence.is_empty():
                continue
            self.log_user.append(self.sentence)
            if str(self.sentence).startswith("bye"):
                print("Your Bot: Farewell!")
                break
            response = self.dialog.select_response(self.dialog, self.sentence)
            print("Your Bot:", response)
            self.log_bot.append(response)
        print("Your Bot: Bye mate!")
        return 0

class Dialog_manager(ChatBot):
    def __new__(self):
        return self
    
    def __init__(self):
        pass
    
    def select_response(self, sentence):
        ### Methods prepared for iteration in closure dialog mechanism ###
        def check_for_greetings(sentence):
            greeting_words = self.bot_data.get_greetings()
            greeting_response = self.bot_data.get_greet_resp()
            for word, greet in it_product(str(sentence).split(" ")[:2], greeting_words):
                if word.startswith(greet):
                    if len(str(sentence).split(" ")) < 2:
                        return 1.0, random.choice(greeting_response)
                    else:
                        return 0.6, random.choice(greeting_response)
            return 0.0, None
                    
        def check_for_question(sentence):
            questions = self.bot_data.get_questions()
            answers = self.bot_data.get_quest_answ()
            try:
                return 1.0, answers[questions.index(str(sentence))]
            except ValueError:
                return sentence.select_most_similar(questions, answers)

        def check_for_complements(sentence):
            complements = self.bot_data.get_complements()
            answers = self.bot_data.get_compl_answ()
            try:
                return 1.0, answers[complements.index(str(sentence))]
            except ValueError:
                return sentence.select_most_similar(complements, answers)
        
        def check_for_respond_yes(sentence):
            responds = self.bot_data.get_responds_yes()
            if sentence.calculate_similarity(responds) > 0.6:
                for answ in self.log_bot[::-1]:
                    if answ.startswith("Do you mean") and answ.endswith(" ?"):
                        answ = answ.split(",,")[1].split("''")[0]
                        return 0.8, self.bot_data.search_question(answ)
                return 0.0, None
            else:
                return 0.0, None
        
        def check_for_congratulations(sentence):
            congratulations = self.bot_data.get_congratulations()
            answers = self.bot_data.get_cngrt_answ()
            try:
                return 1.0, answers[congratulations.index(str(sentence))]
            except ValueError:
                return sentence.select_most_similar(congratulations, answers)
        
        def check_for_name(sentence):
            user_name = self.bot_data.get_name()
            if sentence in user_name:
                self.memory_bot.set_data("Name", sentence.split()[-1])
                return 1.0, "I am ChatBot, nice to meet you."
            else:
                value, answer = sentence.select_most_similar(user_name, ("I am ChatBot, nice to meet you."), tolerance="High")
                if value > 0.8:
                    self.memory_bot.set_data("Name", sentence.split()[-1])
                    return value, answer
                else:
                    return value, answer
        
        def check_for_memory_name(sentence):
            user_ask_possibility = self.bot_data.get_own_name_ask()
            if self.memory_bot.is_exist("Name"):
                if sentence in user_ask_possibility:
                    return 1.0, "Yea, I remember, you are "+self.memory_bot.get("Name")
                else:
                    return sentence.select_most_similar(user_ask_possibility, ("Yea, I remember, you are "+self.memory_bot.get("Name")))
            else:
                if sentence in user_ask_possibility:
                    return 1.0, "No, you didn't tell me yet. What's your name?"
                else:
                    return sentence.select_most_similar(user_ask_possibility, ("No, you didn't tell me yet. What's your name?"))
        
        ### Selection of return ###
        closures = [func for name, func in locals().items()]
        closures.remove(sentence)
        closures.remove(self)
        
        results = []
        similar = []
        for function in closures:
            similarity, answer = function(sentence)
            if similarity > 0:
                results.append(similarity)
                similar.append(answer)
        
        if results and max(results) < 0.4:
            return "I don't know what do you mean."
        else:
            if similar:
                answer = similar[results.index(max(results))]
                if answer == None:
                    return "I don't know what do you mean."
                return answer
            return "I don't know what do you mean."
                

if __name__ == "__main__":
    M = ChatBot()
    M.mainloop()
