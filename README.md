
CommitsTime.py

The program create CSV file with dates of a GitHub user's last 60 commits and displays the mean time between them.
The program can be used with any public GitHub repositories. 

Launching the program 

	1.	Download CommitsTime.py
	2.	Install Python v.3.6 or later (download here https://www.python.org/downloads/)
	3.	Use pip install requests if you have pip installed and Pip.exe added to the Path Environment Variable. If pip is installed but not in your path you can use python -m pip install requests.
	4.	Open the terminal (more info is here https://www.cs.utexas.edu/~mitra/bytes/start.html )
	5.	Navigate to the folder with CommitsTime.py 
	6.	Run the script - type Python CommitsTime.py, click Enter
		a.	Enter GitHub username
		b.	Enter Authentication token (see here how create a personal token https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
		c.	Enter GitHub repository name
		d.	Enter repository’s owner name (can be the same GitHub username). Click “Enter”

						-OR-
						
		-	Open CommitsTime.py in any IDE with Python interpreter 3.6+.
		-	Click “Run the script”.
		-	Repeat steps from a to d from the previous section. 


Results

-	The program will create  Commits_list.csv file in the same directory with the CommitsTime.py file. This CSV file will have up to 60 records/lines with dates and time of the last commits. The records format is  [YYYY-MM-DD HH:MM:SS] 
-	Also the program will display on the console the number of last commits (60 max) and the mean time between them. The format is [DD (if any), HH:MM:SS]


Libraries used

		requests – for API requests
		csv – for writing to *.csv file
		datetime – to get time between two commitments 


	Testing and Examples:

		To test the program you can use the following credentials:
	o	Enter GitHub username: <<your GitHub username >>
	o	Enter Authentication token: <<your access token>> 
	o	Enter GitHub repository name:bootstrap
	o	Enter repositorys owner name (can be the same GitHub username):twbs
	
	Expected result – option 1: 
	Number of processed commits (max 60) is: 60
	The mean time between the last commits [Days (if any), HH:MM:SS] is: 9:03:45 

	Expected result – option 2:
	Number of processed commits (max 60) is: 13
	The mean time between the last commits [Days (if any), HH:MM:SS] is: 12:09:04
