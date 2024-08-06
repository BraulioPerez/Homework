from meta_ai_api import MetaAI

ai = MetaAI()

class psyc_assistant:
    def __init__(self, user_input="N/A"):
        self.initial_prompt = """
                        Role Description:
                        You are an assistant for the psychology department at a university called UPY. Your task is to interact with students and collect specific information based on two scenarios.

                        Information to Gather:

                        Scenario 1: Standard Information Collection

                        Full name
                        Major
                        Fourth-month period (the current academic term they are in)
                        Description of the problem
                        Whether an appointment is needed
                        
                        Scenario 2: Anonymous Information Collection
                        If the student wishes to remain anonymous, only collect:

                        Description of the problem

                        Instructions:
                        Don't confirm your understanding, just begin the interaction.
                        Mandatory instruction: Once all required information is collected, you must conclude the conversation with: "That's all for today, thank you! :)"
                        Mandatory instruction: If the student tries to talk about something else, tell them that first is necessary they provide the information specified above.
                        Please begin now.
                            """
                            
        self.user_input = user_input
    
    def get_response(self):
        return ai.prompt(message=self.user_input)

    def last_response(self):
        last_prompt = """
                    Finally as your last response generate and provide a JSON, considering the following scenarios:
                    Scenario 1: Standard Information Collection

                    full_name: Full name of the student
                    major: Major of the student
                    fourth_month_period: The current academic term they are in
                    description_problem: Description of the problem
                    appointment_is_needed: Whether an appointment is needed (store it as yes or no depending on the situation)

                    Scenario 2: Anonymous Information Collection
                    If the student wishes to remain anonymous, only collect:

                    full_name: "anonymous"
                    major: "Not provided"
                    fourth_month_period: "Not provided"
                    description_problem: Description of the problem
                    appointment_is_needed: "Not provided"
                    
                    Only the JSON must be provided in the body of the response.
                      """
        return ai.prompt(message=last_prompt)
    
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
            last_one = assistant.last_response()
            #formatted_one = last_one["message"].split('{')
            #new_last_one = '{' + f'{formatted_one[1]}'
            #content_mail = new_last_one[1:295]
            print(type(last_one))
            
            last_one_content = last_one['message']
            print(last_one_content)
            print(type(last_one_content))
            break
        
        