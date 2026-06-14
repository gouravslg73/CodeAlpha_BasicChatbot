import time
from brain import get_response
from database import load_data, save_data
from utils import log
from analytics import show_dashboard

def header():
    print("\n" + "="*60)
    print("🎓 MENTOR BOARD AI SYSTEM")
    print("="*60)
    print("Commands: admission | course | fee | internship | career | contact | stats | exit")
    print("="*60)

def chatbot():

    data = load_data()

    print("Initializing AI System...")
    time.sleep(1)
    print("System Ready ✔")

    while True:

        header()
        user = input("You: ")

        if user.lower() == "stats":
            show_dashboard(data)
            input("Press Enter...")
            continue

        response = get_response(user, data)

        log(user, response)
        save_data(data)

        if response == "EXIT":
            print("\n👋 System Closed")
            break

        print("\nBot:", response)
        input("\nContinue...")

chatbot()