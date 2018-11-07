#use pip install pygithub to use the PyGitHub library
from github import Github

#Github instance:
g = Github("e792e1423f538d42a0e1762e49d2136994e96da7")

for repo in g.get_user().get_repos():
    print (repo.name)
