import argparse
import json
import requests
import os

def fetch_gists(username):
    """Fetches and displays public gists for a given GitHub username."""
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url)
    gists = response.json()

    return gists

def save_last_run(gists):
    """Saves the timestamp of the last fetched gist."""
    if gists:
        last_gist_created_at = gists[0]['created_at']
        with open("last_run.txt", "w") as file:
            file.write(last_gist_created_at)

def read_last_run():
    """Reads the last run timestamp."""
    if os.path.exists("last_run.txt"):
        with open("last_run.txt", "r") as file:
            return file.read()
    return None

def filter_new_gists(gists, last_run):
    """Filters gists to return only those newer than the last run."""
    return [gist for gist in gists if gist['created_at'] > last_run] if last_run else gists

def main():
    parser = argparse.ArgumentParser(description="Fetches a user's public GitHub gists.")
    parser.add_argument("username", help="GitHub username to fetch gists for")
    args = parser.parse_args()

    gists = fetch_gists(args.username)
    last_run = read_last_run()

    new_gists = filter_new_gists(gists, last_run)
    if new_gists:
        print(f"New gists for {args.username}:")
        for gist in new_gists:
            print(f"- {gist['html_url']}")
        save_last_run(gists)
    else:
        print("No new gists since the last run.")

if __name__ == "__main__":
    main()