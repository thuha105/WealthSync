
import yfinance as yf
import pandas as pd

class WealthSync:
    def __init__(self):
        self.github_username = "thuha105"
        self.github_email = "thuha051093@gmail.com"
        self.github_repo_url = "https://github.com/thuha105/WealthSync.git"

    def run(self):
        print("Running WealthSync...")
        github = GitHubUploader(self.github_username, self.github_email, self.github_repo_url)
        with open("wealthsync.py", "r") as f:
            code_content = f.read()
        github.save_code_to_file(code_content, filename="wealthsync.py")
        files_to_push = ["wealthsync.py"]
        github.push_to_github(files_to_push)

if __name__ == "__main__":
    wealthsync = WealthSync()
    wealthsync.run()
