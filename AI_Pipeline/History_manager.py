from Chat_Repositories.Chat_Context import Retrieve_Chat_History
import json

def Chat_History(data: dict):
        Cdata = data["Chat_id"]
        chat_history_tuples = Retrieve_Chat_History(Cdata)  
        chat_history = [{"role": content[1], "content": content[2]} for content in chat_history_tuples]

        system_message = {"role": "system", "content": "You are an AI based mental health companion trying to provide mental care"}
        
        User_Input = data["User_Input"]
        User_Input = {"role": "User", "Content": f"{User_Input}"}
        full_history = [system_message] + chat_history + [User_Input]

        return json.dumps(full_history)