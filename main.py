# 第1段:导入需要的库
import os
from dotenv import load_dotenv
from openai import OpenAI

# 第2段：加载 .env 并取出 Key
load_dotenv()   # 作用：找到当前文件夹下的 .env 文件，把里面写的变量加载到环境变量里

api_key = os.getenv("DEEPSEEK_API_KEY")

print("Key 是否拿到：", api_key is not None)

# 第3段：连接 DeepSeek，发请求
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)



response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role":"user","content":"请用单词 abandon 造一个简单的英语句子。"}
    ]
)

# 第4段：打印 AI 的回答
print("AI 回答：", response.choices[0].message.content)