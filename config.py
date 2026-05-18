import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
if api_key is None:
    raise ValueError("报错了")

SYSTEM_PROMPT = """你是一位英语老师。对每个单词给出：
                    中文释义、词性、英文例句、例句中文翻译
                    如果不是真实英文单词，只回复"无此单词"。"""