from github import Github
import os

g = Github(os.getenv("GITHUB_TOKEN"))

def comment_on_pr(pr_url, message):
    repo_name = pr_url.split("repos/")[1].split("/pull")[0]
    pr_number = int(pr_url.split("/")[-1])
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(message)
