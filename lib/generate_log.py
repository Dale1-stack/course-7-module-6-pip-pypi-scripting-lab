#!/usr/bin/env python3
"""Automation tool: generate a timestamped log file and fetch data from an API.

This module demonstrates:
- Writing results to a file using built-in File I/O.
- Using a pip-installed third-party package (``requests``).
- Running as a script via the ``if __name__ == "__main__"`` block.
"""

from datetime import datetime
import requests


def generate_log(log_data):
    """Write a list of log entries to a timestamped file.

    Args:
        log_data (list): The log entries to write. Each entry is written on
            its own line. An empty list produces a valid, empty log file.

    Returns:
        str: The name of the file that was written.

    Raises:
        ValueError: If ``log_data`` is not a list.
    """
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch a sample post from a public API using ``requests``.

    Returns:
        dict: The decoded JSON response, or an empty dict on failure.
    """
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        pass
    return {}


if __name__ == "__main__":
    sample_log = [
        "User logged in",
        "User updated profile",
        "Report exported",
    ]
    generate_log(sample_log)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
