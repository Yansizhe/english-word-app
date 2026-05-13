# === 第 1 段：导入需要的库 ===
import os                                # 标准库，用来读环境变量
from dotenv import load_dotenv           # 第三方库，用来读取 .env 文件并注入环境变量
from openai import OpenAI                # 第三方库，DeepSeek 兼容 OpenAI 接口规范，用它来调

# === 第 2 段：加载 API Key（配置和代码分离）===
load_dotenv()                            # 把 .env 文件里的变量加载到当前程序的环境变量中
api_key = os.getenv("DEEPSEEK_API_KEY")  # 从环境变量取出 Key，避免 Key 写死在代码里

# === 第 3 段：创建 DeepSeek 客户端 ===
# 用 OpenAI 类创建一个客户端对象 client，相当于"打电话的手机"
# base_url 指定打给谁（DeepSeek 服务器），api_key 标识用谁的账户扣钱
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

# === 第 4 段：主循环 - 反复接收用户输入 ===
while True:                              # 无限循环，直到用户主动退出
    user_input = input("请输入要学习的英文单词:")

    # 退出条件：输入 quit 跳出循环（.lower() 让大小写都能识别）
    if user_input.lower() == "quit":
        break

    # 输入校验：必须是纯英文字母
    # isascii() 排除中文，isalpha() 排除数字和符号，两个都要满足才合法
    # 不合法时打印提示并 continue（跳过 API 调用，回到循环顶部）
    if not (user_input.isascii() and user_input.isalpha()):
        print("请输入英语单词！")
        print()
        continue

    # === 调用 DeepSeek，发请求 ===
    # messages 是对话历史列表：
    #   - system：给 AI 设定角色和输出规则（这是 prompt 工程的核心）
    #   - user：用户的具体提问（用 f-string 把单词拼进去）
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

    # === 打印 AI 的回答 ===
    # response 是一个嵌套对象：
    #   choices[0]  → 第一个候选回答（默认只有一个）
    #   .message    → 这条回答的消息体
    #   .content    → 消息正文，就是真正的文字
    print("AI 回答：", response.choices[0].message.content)
    print()