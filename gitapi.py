#use pip install pygithub to use the PyGitHub library
from github import Github
import getpass
import sys
import json

print ("Please enter your username: ")
user = input()

password = getpass.getpass("Please enter your password: ")

#Github instance:
g = Github(user,password)



repo_count = 0
list = list()
data = {}
data['info'] = []

repo_info ={}
repo_info['info'] = []

max_contributors = 0
repo_with_most_contributors = "";

for repo in g.get_user().get_repos():
    contributors2 = [ j for j in repo.get_contributors()]
    repo_info['info'].append({
        'repo': repo.name,
        'contributors': len(contributors2)
    })
    if (len(contributors2) > max_contributors):
        max_contributors = len(contributors2)
        repo_with_most_contributors = repo.name;


for repo in g.get_user().get_repos():
    if (repo.name == repo_with_most_contributors):
        contributors = repo.get_contributors()
        i = 0;
        for collaborator in contributors:
            print(collaborator.login)
            count = 0
            for commit in repo.get_commits():
                if (commit.author == collaborator):
                    count += 1
            list.insert(i,count)
            data['info'].append({
                'name': collaborator.login,
                'commits': count
            })
            print (list[i])
            i = i+1


with open('info.json', 'w') as outfile:
    json.dump(data, outfile)

with open('repos.json', 'w') as outfile:
    json.dump(repo_info, outfile)


#contributors2 = [ j for j in repo.get_stats_commit_activity()]
#print("\n", contributors.login)

#my_stats = []
#for r in repo.get_contributors():
#     my_stats.append(r.c)

#print (my_stats)
#contributors()
#contents = repo.get_contents("")
#for content_file in contents:
#    print(content_file)
