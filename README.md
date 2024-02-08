# Simple GitHub Gists Fetcher

A straightforward script to retrieve a GitHub user's latest public gists.

## Requirements

- Python 3
- No external libraries required (uses standard library only)

## Setup and Run

1. Ensure you have Python 3 installed on your machine.
2. Save the `simple_github_gists.py` script to your local machine.
3. Run the script from the command line by passing a GitHub username:

   ```
   python simple_github_gists.py <username>
   ```

## Functionality

- On the first run, lists all publicly available gists for the specified user.
- On subsequent runs, lists only the gists that have been published since the last run.
- Utilizes a simple file (`last_run.txt`) to track the timestamp of the last fetched gist.

## Example

```
python simple_github_gists.py octocat
```

This will list all public gists for the user "octocat". On subsequent runs, it will only show new gists published after the last run.