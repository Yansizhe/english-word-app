from openai import OpenAI
import config

client = OpenAI(
    api_key=config.api_key,
    base_url="https://api.deepseek.com"
)

def ask_ai(system_prompt, user_message):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system","content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
    except Exception as e:
        return f"😵 调用 AI 失败：{e}"
    
    return response.choices[0].message.content