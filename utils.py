import datetime

def log(user, bot):
    with open("chat_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} | USER: {user} | BOT: {bot}\n")