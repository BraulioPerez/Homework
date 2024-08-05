from meta_ai_api import MetaAI

ai = MetaAI()
response = ai.prompt(message="Act as an assistant for psicology department of the UPY, you need to gather my name and lastname from me, ask whatever you want, if you understand start now, once you are done tell me thats all for today, thank me and a smiley face :) una vez acabes entrega los datos en forma de json con lo siguiente {nombre completo, indole del probelma (profesores, ), descripcion del probema, }")

while True:
    print(response)
    user_input = input()
    response = ai.prompt(message=user_input)
    if user_input == "break":
        break

class psyc_assistant:
    def __init__(self, user_input="N/A"):
        self.initial_prompt = """
                                Act as an assistant for psicology department of the UPY, 
                                you need to gather my name and lastname from me, ask whatever 
                                you want, if you understand start now, once you are done tell 
                                me thats all for today, thank me and a smiley face :) once you are done
                            """
        self.user_input = user_input
    
    def get_response(self):
        return ai.prompt(message=self.user_input)

    def last_response(self):
        return ai.prompt(message="generate the following json: {Full name, problem title, description }")
    
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
        