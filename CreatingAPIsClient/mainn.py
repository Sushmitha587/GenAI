from pagination import list_all_issues  # replace with file name

issues = list_all_issues("octocat", "Spoon-Knife")

print("Total issues:", len(issues))

for issue in issues:
    print(issue["title"])
