# GitHub User Activity

**GitHub User Activity** is a simple command-line interface (CLI) tool that fetches and displays the latest public activity of a GitHub user.

## Features

- Shows recent events like:
  - Pushes
  - Stars
  - Forks
  - Pull requests
  - Comments and reviews
- Optional flag to show messages and comments
- Clean and readable output
- Built with Python 3

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/github-user-activity.git
cd github-user-activity
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install requests
```

Or, if you're using `pyproject.toml`:

```bash
pip install .
```

## Usage

You can run the CLI like this:

```bash
python -m github_user_activity --help
```

Or, if the project is installed via `pyproject.toml`, you can use the command directly:

```bash
github-activity username
```

### Example

```bash
github-activity Gabberpal --show-messages
```

This will show the recent public events of user `Gabberpal`, including review and comment text.



## Requirements

* Python 3.10 or higher
* `requests` (install via pip)

