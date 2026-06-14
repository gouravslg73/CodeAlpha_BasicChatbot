import random

def get_response(user, data):

    text = user.lower().strip()
    data["total_queries"] += 1

    # GREETING SYSTEM
    if any(x in text for x in ["hi", "hello", "hey"]):
        return random.choice([
            "Hello 👋 Welcome to Mentor Board AI System",
            "Hi! How can I help you today?",
            "Hey! Ask me about courses or career"
        ])

    # ADMISSION
    elif "admission" in text:
        data["stats"]["admission"] += 1
        return """
📌 ADMISSION PROCESS:
1. Online registration
2. Fill application form
3. Upload documents
4. Verification
5. Confirmation

Status: OPEN
"""

    # COURSES
    elif "course" in text:
        data["stats"]["course"] += 1
        return """
📚 COURSES AVAILABLE:
- Python Programming
- Web Development
- Data Science
- AI Basics
- DSA Fundamentals
"""

    # FEES
    elif "fee" in text:
        data["stats"]["fee"] += 1
        return """
💰 FEE STRUCTURE:
- Python: ₹3000-₹5000
- Web Dev: ₹5000-₹8000
- Data Science: ₹8000-₹12000
- AI: ₹10000-₹15000
"""

    # INTERNSHIP
    elif "internship" in text:
        data["stats"]["internship"] += 1
        return """
💼 INTERNSHIPS:
- Python Developer
- Web Developer
- Data Analyst
- AI Intern

Duration: 30-90 Days
Certificate Provided
"""

    # CAREER
    elif "career" in text:
        data["stats"]["career"] += 1
        return """
🚀 CAREER ROADMAP:
Step 1: Learn Programming
Step 2: Build Projects
Step 3: Learn DSA
Step 4: GitHub Profile
Step 5: Internship
Step 6: Job Placement
"""

    # CONTACT
    elif "contact" in text:
        data["stats"]["contact"] += 1
        return """
📞 CONTACT:
Email: support@mentorboard.com
WhatsApp: +91-XXXXXXXXXX
Time: 10AM - 6PM
"""

    # PYTHON INFO
    elif "python" in text:
        return "🐍 Python is used in AI, Web Dev, Data Science, Automation"

    # AI INFO
    elif "ai" in text:
        return "🤖 AI is Artificial Intelligence used for smart systems"

    # EXIT
    elif text == "exit":
        return "EXIT"

    else:
        return "⚠ Invalid input. Type help or ask admission/course/fee"