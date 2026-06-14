def show_dashboard(data):

    print("\n" + "="*50)
    print("📊 MENTOR BOARD ANALYTICS DASHBOARD")
    print("="*50)

    print("Total Queries:", data["total_queries"])
    print("Admission:", data["stats"]["admission"])
    print("Courses:", data["stats"]["course"])
    print("Fees:", data["stats"]["fee"])
    print("Internships:", data["stats"]["internship"])
    print("Career:", data["stats"]["career"])
    print("Contact:", data["stats"]["contact"])

    print("="*50)