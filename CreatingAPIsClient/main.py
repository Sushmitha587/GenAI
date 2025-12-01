from github_client import GitHubClient

client = GitHubClient()  # uses GITHUB_TOKEN from environment

user = client.get_user("octocat")
print("User:", user["login"], "| public repos:", user["public_repos"])

# repo = client.create_repo("demo-repo-from-code")
# print("Created:", repo["full_name"])