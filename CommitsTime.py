import requests as r
import csv
from datetime import datetime
from datetime import date
from datetime import timedelta

username = input("Enter GitHub username:")
token = input("Enter Authentication token:")
github = "https://api.github.com/"

rep = input('Enter GitHub repository name:')
uname = input('Enter repositorys owner name (can be the same GitHub username):')

def strToDateTime(dt):                            # get date/time from GitHub API, convert to Date/Time
    date1 = dt.replace('Z', '')
    (y, m, d) = date1.split('T')[0].split('-')
    (h, min, s) = date1.split('T')[1].split(':')
    y = int(y)
    m = int(m)
    d = int(d)
    h = int(h)
    min = int(min)
    s = int(s)
    return datetime(y,m,d, h, min, s)

def timeBetween(d1, d2):                           # Returns time (in seconds) between two commits
    return abs(d2-d1).total_seconds()

class GitUser:                                     # GitHub user class
    def __init__(self, u, t):                      # Recieves username and token
        self.username = u
        self.token = t

    def writeToColumn(self, name, arr):            # write arr to .csv file (column)
        with open(name+'.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for line in arr:
                writer.writerow([line]);
        f.close()

    def apiRequest(self,req):                       # API requests
        params = {'per_page':'65'}                  # TMP - gets 65 records per one request/page
        return r.get(github + req, auth=(self.username, self.token),params=params) # Sends request with parametrs

    def searchCommits(self, uname, repo):           # returns JSON will all commits
        return self.apiRequest('repos/'+uname+'/'+repo+'/commits').json()

    def getCommitsDates(self,uname,repo):           # returns array with commits dates/time 60 max
        commits = self.searchCommits(uname,repo)
        dates = []
        if(len(commits)>60):
            for i in range(60):
                dates.append(strToDateTime(commits[i]['commit']['author']['date']))
        else:
            for commit in commits:
                dates.append(strToDateTime(commit['commit']['author']['date']))
        return dates

user = GitUser(username, token)


averageSecs = 0

dates =user.getCommitsDates(uname, rep)

for i in range(len(dates)-1):                          # total time between commits
    averageSecs += (timeBetween(dates[i], dates[i+1]))

averageSecs /= len(dates)-1                             # mean time between commits

print("Number of processed commits (max 60) is:"+str(len(dates)))
print("The mean time between the last commits [Days (if any), HH:MM:SS] is : " + str(timedelta(seconds=averageSecs)).replace('days', 'days').split('.')[0])

user.writeToColumn('Commits_list',dates)                  # write commits' date/time to Commits_list.csv
