from github import Github

#Github instance:
g = Github("6ce726b4f5cc4f5777a3bfe32c91b507b7bf6a16")

for repo in g.get_user().get_repos():
    print (repo.name)
