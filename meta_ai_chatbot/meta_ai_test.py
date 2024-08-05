from meta_ai_api import MetaAI

ai = MetaAI()

class psyc_assistant:
    def __init__(self, user_input="N/A"):
        self.initial_prompt = """
                                Act as an assistant for the psychology department of the UPY, 
                                you need to gather my name and lastname from me, ask whatever 
                                you want, if you understand start now, once you are done tell 
                                me thats all for today, thank me and a smiley face :) once you are done
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
        