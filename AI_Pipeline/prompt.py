from Chat_Repositories.User_prompt_data import User_prompt_data
from langchain_core.prompts import load_prompt

def Prompt(history, chat_id, user_id):
    if user_id == "False":
        user_data = User_prompt_data(chat_id)
        age = [user[0] if isinstance(user, tuple) else user for user in user_data]
        gender = [user[1] if isinstance(user, tuple) else user for user in user_data]

        prompt = load_prompt("AI_Pipeline/Prompt_Template.json")

        Final_prompt = prompt.invoke({
            "gender": gender,
            "age": age,
            "history": history
        })
        return Final_prompt
    prompt = load_prompt("AI_Pipeline/Title_Prompt_Template.json")

    Final_prompt = prompt.invoke({
        "First_Message": history
    })
    return Final_prompt