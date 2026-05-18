import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

while True:
    user_input = input("请输入要学习的英文单词:")

    if user_input.lower() == "quit":
        break

    if not (user_input.isascii() and user_input.isalpha()):
        print("请输入英语单词！")
        print()
        continue

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system",
             "content": """你是一位英语老师。对每个单词给出：
                    中文释义、词性、英文例句、例句中文翻译
                    如果不是真实英文单词，只回复"无此单词"。"""},
            {"role": "user", "content": f"请讲解单词：{user_input}"}
        ]
    )

    print("AI 回答：", response.choices[0].message.content)
    print()