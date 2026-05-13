# 第1段:导入需要的库
import os
from dotenv import load_dotenv
from openai import OpenAI

# 第2段：加载 .env 并取出 Key
load_dotenv()   # 作用：找到当前文件夹下的 .env 文件，把里面写的变量加载到环境变量里

api_key = os.getenv("DEEPSEEK_API_KEY")


# 第3段：连接 DeepSeek，发请求
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

user_input = input("请输入要学习的英文单词:")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role":"system","content":"你是一位英语老师。对每个单词给出：中文释义、词性、英文例句、例句中文翻译。"},
        {"role":"user","content":f"请讲解单词：{user_input}"}
    ]
)

# 第4段：打印 AI 的回答
print("AI 回答：", response.choices[0].message.content)