# 第1段:导入需要的库
import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 并取出 Key
load_dotenv()   # 作用：找到当前文件夹下的 .env 文件，把里面写的变量加载到环境变量里

api_key = os.getenv("DEEPSEEK_API_KEY")  # 使用放在环境变量里的关键变量


# 连接 DeepSeek，发请求
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


#添加循环
while True: 
    user_input = input("请输入要学习的英文单词:")

    if user_input.lower() == "quit":
        break
    # 另一种写法：
    # if user_input.lower() in ["quit","exit","q"]:
    #   break
    
    if not (user_input.isascii() and user_input.isalpha()):
        print("请输入英语单词！")
        print(end="\n")
        continue

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"system",
             "content":"""你是一位英语老师。对每个单词给出：
                    中文释义、词性、英文例句、例句中文翻译
                    如果不是真实英文单词，只回复"无此单词"。"""},
            {"role":"user","content":f"请讲解单词：{user_input}"}
        ]
    )
    # 打印 AI 的回答
    print("AI 回答：", response.choices[0].message.content)
    print(end="\n")