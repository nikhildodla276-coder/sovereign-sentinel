"""Practicing this project from scratch with absolute basics"""

def check_internship(title, company, stipend):
    if "AI" in title and stipend >= 5000:
        return(f"New Internship Found!\ntitle: {title}\ncompany: {company}\nstipend: {stipend}")
    else:
        return(f"Skipping: {title}")

result_1 = check_internship("AI Engineer", "Google", 8000)
result_2 = check_internship("Web Developer", "Amazon", 6000)
result_3 = check_internship("AI Automation", "Microsoft", 3000)

print(result_1)
print(result_2)
print(result_3)