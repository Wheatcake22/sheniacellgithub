import os
import subprocess
from datetime import datetime, timedelta
import random

# Конфигурация
author_name = "Your Name"
author_email = "your.email@example.com"
num_days = 10
min_commits_per_day = 1
max_commits_per_day = 5

repo_path = os.path.dirname(os.path.abspath(__file__))

def make_commit(commit_date, message):
    with open(os.path.join(repo_path, "log.txt"), "a") as f:
        f.write(f"{commit_date} — {message}\n")
    subprocess.run(["git", "add", "log.txt"])
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = commit_date
    env["GIT_COMMITTER_DATE"] = commit_date
    env["GIT_AUTHOR_NAME"] = author_name
    env["GIT_AUTHOR_EMAIL"] = author_email
    subprocess.run(["git", "commit", "-m", message], env=env)

today = datetime.now()

for i in range(num_days):
    date = today - timedelta(days=i)
    commits_today = random.randint(min_commits_per_day, max_commits_per_day)
    for j in range(commits_today):
        time_offset = timedelta(minutes=random.randint(1, 720))
        commit_time = date + time_offset
        commit_date_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        message = f"Commit on {commit_date_str}"
        make_commit(commit_date_str, message)

# subprocess.run(["git", "push"])
