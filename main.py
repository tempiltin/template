import os
import json
import random
import datetime
import subprocess

def generate_random_json(file_name):
    data = {
        "id": random.randint(1, 1000),
        "name": "RandomData",
        "value": random.random()
    }
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def get_random_dates(year, month, count=10):
    days = list(range(1, 29))  # Max 28 to avoid February issues
    random.shuffle(days)
    return [datetime.date(year, month, day) for day in days[:count]]

def run_git_commands(date):
    os.system("git add .")
    commit_date = date.strftime("%Y-%m-%dT01:08:00")
    os.system(f'git commit --date="{commit_date}" -m "Old commit"')
    os.system("git push")

def main():
    year = 2022
    for month in range(1, 13):
        dates = get_random_dates(year, month, count=25)
        for date in dates:
            file_name = f"random_data_{date}.json"
            generate_random_json(file_name)
            run_git_commands(date)
            print(f"Committed and pushed for {date}")

if __name__ == "__main__":
    main()
