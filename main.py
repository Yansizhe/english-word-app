import config
import ai_client

if __name__ == "__main__":
    while True:
        user_input = input("请输入要学习的英文单词:")

        if user_input.lower() == "quit":
            break

        if not (user_input.isascii() and user_input.isalpha()):
            print("请输入英语单词！")
            print()
            continue
        
        user_message = f"请讲解单词：{user_input}"
        result = ai_client.ask_ai(config.SYSTEM_PROMPT, user_message)
        print("AI 回答：",result)
        print()