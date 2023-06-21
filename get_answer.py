def get_answer(question):
    if question == "你好":
        return "你好"
    elif question == "你的名字是什么":
        return "黄文定"
    elif question == "你的生日是什么时候":
        return "2009年7月18日"
    elif question == "你是中国人吗":
        return "我是中国人"
    elif question == "台湾是中国的吗":
        return "台湾是中国的"
    elif question == "你爱我吗":
        return "这是一个由我决定的选项，我需要认真，但是我还是爱着你"
    elif question == "你喜欢去哪里":
        return "中国大陆和中国台湾"
    elif question == "你有朋友吗":
        return "没有"
    elif question == "你的心情怎么样":
        return "自卑，孤独"
    else:
        return "抱歉，我无法回答你的问题。"

while True:
    user_question = input("请输入你的问题（输入'退出'可以结束程序）: ")
    if user_question == "退出":
        break
    response = get_answer(user_question)
    print(response)
