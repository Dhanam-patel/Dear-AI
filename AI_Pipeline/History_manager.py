from Chat_Repositories.Chat_Context import Retrieve_Chat_History
import json
from AI_Pipeline.System_Prompt import System_prompt
def Chat_History(data: dict):
        Cdata = data["Chat_id"]
        chat_history_tuples = Retrieve_Chat_History(Cdata)  
        chat_history = [{"role": content[1], "content": content[2]} for content in chat_history_tuples]

        system_message = {"role": "system", "content": System_prompt()}
        
        User_Input = data["User_Input"]
        User_Input = {"role": "User", "Content": f"{User_Input}"}
        full_history = [system_message] + chat_history + [User_Input]

        return json.dumps(full_history)