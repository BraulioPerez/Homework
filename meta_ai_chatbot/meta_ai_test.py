from meta_ai_api import MetaAI

ai = MetaAI()

class psyc_assistant:
    def __init__(self, user_input="N/A"):
        self.initial_prompt = """
                                Act as an assistant for psicologyst department of the UPY, 
                                you'll need to gather information from the situation the 
                                alumni is having, ask for their full name, the situation description,
                                and people involved, finally determine if it is a report or a petition
                                for an appointment with the psychologist, once you have all this info
                                answer with "thats all we need, thank you for your colaboration :)"
                            """
        self.user_input = user_input
    
    def get_response(self):
        return ai.prompt(message=self.user_input)

    def last_response(self):
        return ai.prompt(message="generate the following json: {Full name, problem title, description } , if it is a report write [REPORT] at the begining of the title, else write [APPOINTMENT]")
    
    def first_response(self):
        return ai.prompt(message=self.initial_prompt)

if __name__ == "__main__":
    assistant = psyc_assistant()
    print(assistant.first_response())
    while True:
        assistant.user_input = input()
        response = assistant.get_response()
        print(response)
        print(type(response))
        if ":)" in response["message"]:
            break
        