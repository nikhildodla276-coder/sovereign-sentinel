"""Practicing this project from scratch with absolute basics"""

internships = [
    {
        "title": "AI Engineer",
        "company": "Google",
        "stipend": 5000,
        "apply_link": "https://internshala.com/internship/detail/ai-ml-123"
    },
    {
        "title": "AI Automation",
        "company": "Microsoft",
        "stipend": 59000,
        "apply_link": "https://internshala.com/internship/detail/ai-automation-123"
    },
    {
        "title": "ML Engineer",
        "company": "Infosys",
        "stipend": 35000,
        "apply_link": "https://internshala.com/internship/detail/ml-engineer-123"
    }
]

for dictionary in internships:
    if "AI" in dictionary["title"] and dictionary["stipend"] >= 5000:
        print(f"New Internship Found!\nTitle: {dictionary["title"]}\nCompany: {dictionary["company"]}\nStipend: {dictionary["stipend"]}\nApply: {dictionary["apply_link"]}")
    else:
        print(f"Skipping: {dictionary["title"]}")
