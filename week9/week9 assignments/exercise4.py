# challenge

# Write a Python script that generates a README template
# for a GitHub project
project = "AI Text Summariser"
desc = "A Python tool that summarises long text using the OpenAI API."
tech = ["Python", "OpenAI API", "Flask"]

print(f"# {project}")
print(f"\n{desc}\n")
print("## Tech Stack")
for t in tech:
    print(f"- {t}")