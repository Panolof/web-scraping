## Author
**Name**: Pano Pouroullis <br/>
**Date**: 4th August 2024

# Overview
This repository contains a modular web scraping framework using Python. The structure is designed to facilitate reusability and maintainability across multiple projects.

# Directory Structure
```
web-scraping/
├── projects/
│   ├── project1/
│   │   ├── main.py
│   │   └── config.py
│   └── project2/
│       ├── main.py
│       └── config.py
├── helpers/
│   ├── __init__.py
│   ├── browser.py
│   ├── proxy.py
│   ├── scraper.py
│   └── utils.py
├── echo_helpers_content.sh
└── README.md
```

# Helpers Module
The `helpers` module provides reusable functions for web scraping, including browser automation, proxy management, HTML parsing, and utility functions.

## `helpers/__init__.py`
```python

from .browser import create_driver, fetch_page_with_selenium
from .proxy import get_proxies, rotate_proxies
from .scraper import fetch_page, parse_html, extract_links
from .utils import setup_logging, delay

__all__ = [
    'create_driver',
    'fetch_page_with_selenium',
    'get_proxies',
    'rotate_proxies',
    'fetch_page',
    'parse_html',
    'extract_links',
    'setup_logging',
    'delay'
]

```

# Project Setup
1. **Set PYTHONPATH**:
   Ensure Python can locate the `helpers` module by setting the `PYTHONPATH`.
   ```bash
   export PYTHONPATH="${PYTHONPATH}:/path/to/web-scraping"
   ```

2. **Project Example (`project1/main.py`)**:
   ```python
   from helpers import (
       create_driver, fetch_page_with_selenium,
       get_proxies, rotate_proxies,
       fetch_page, parse_html, extract_links,
       setup_logging, delay
   )

   def main():
       setup_logging()
       driver = create_driver(headless=True)
       url = "http://example.com"
       html = fetch_page_with_selenium(url, driver)
       print(html)
       delay(2)

   if __name__ == "__main__":
       main()
   ```

3. **Run the Script**:
   Execute the script with the appropriate `PYTHONPATH`.
   ```bash
   PYTHONPATH="${PYTHONPATH}:/path/to/web-scraping" python /path/to/web-scraping/projects/project1/main.py
   ```

# Usage
- **Browser Automation**: Use `create_driver` and `fetch_page_with_selenium` for scraping using Selenium.
- **Proxy Management**: Use `get_proxies` and `rotate_proxies` to handle proxies.
- **HTML Parsing**: Use `fetch_page`, `parse_html`, and `extract_links` for requests-based scraping and parsing.
- **Utilities**: Use `setup_logging` and `delay` for logging and managing delays.


## Echo Helpers Content Script
The `echo_content_for_llm.sh` script can be used to output the contents of each file. This is useful for generating context for an LLM.

## Running the Script

1. **Change Permissions**:
   ```bash
   chmod +x echo_content_for_llm.sh
   ```

2. **Run the Script**:
   ```bash
   ./echo_content_for_llm.sh > LLM_helper_file_context.txt
   ```

# Contributing
Feel free to submit issues or pull requests. Ensure your code adheres to the project's coding standards.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# .gitignore
```
# Ignore data files
*.csv
*.json
*.xml

# Ignore images
*.png
*.jpg
*.jpeg
*.gif

# Ignore LLM context file
LLM_helper_file_context.txt

# Ignore OS files
.DS_Store

# Ignore IDE files
.idea/
.vscode/

# Ignore log files
*.log

```