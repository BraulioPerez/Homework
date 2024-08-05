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
    def __init__(self, user_input, last_prompt):
        self.initial_prompt = """Act as an assistant for psicology department of the UPY, 
                                you need to gather my name and lastname from me, ask whatever 
                                you want, if you understand start now, once you are done tell 
                                me thats all for today, thank me and a smiley face :) onvr you are done, generate the following json: {Full name, nature of the problem, descriptio }"""
