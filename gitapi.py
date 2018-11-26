#use pip install pygithub to use the PyGitHub library
from github import Github
import getpass
import sys

#print ("Please enter your username: ")
#user = input()

#print ("Please enter your password: ")
#p = input()

#Github instance:
g = Github("hurleyd4","githubpass1")


repo = g.get_repo("PyGithub/PyGithub")
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)
#for commit in g.get_user().get_commits():
#    print (commit.name)
