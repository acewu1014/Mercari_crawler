![Build Status](https://github.com/acewu1014/Mercari_crawler/actions/workflows/devops-ci.yaml/badge.svg)
## Project Name: Automatic Mercari Crawler& Discord Notifier
## Descriptions
A robust web scraping solution built with Python and Playwright to monitor Japanese e-commerce listings in real-time.

Key DevOps Features:

1. Containerization: Fully dockerized environment for consistent deployment across different infrastructures. -->

2. CI/CD Pipeline: Integrated GitHub Actions for automated linting (Flake8), dependency management, and build verification.

3. Cloud-Native Security: Implemented secret management using environment variables to ensure secure handling of sensitive Webhook URLs.

4. Infrastructure as Code (IaC) Ready: Designed with a modular architecture suitable for deployment on Kubernetes or cloud-based runners.
## Quick Start (Recommended: Docker)
The easiest way to run the scraper without worrying about local Python environments or Playwright dependencies.

1. Build the Image
```Bash
docker build -t mercari-scraper .
```
2. Run the Container
Pass your Discord Webhook URL as an environment variable:

```Bash
docker run --rm -e DISCORD_WEBHOOK_URL="YOUR_WEBHOOK_URL" mercari-scraper
```
## Local Development Setup
1. **Create a virtual environment:**
    ```bash
    conda create -n crawler python=3.7
    conda activate crawler
    ```   

2. **Install dependecy:**
    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```
    
    ```txt
    playwright == 1.51.0
    requests == 2.32.3
    schedule == 1.2.2
    ```
3. **Add Secret.txt:**
You can either use a secret.txt file or set an environment variable:

* Option A: Create secret.txt in the root folder and paste your Webhook URL.

* Option B: export DISCORD_WEBHOOK_URL="YOUR_URL"

```Python
📂Mercari_crawler/
    ├── discord.py
    ├── main.py
    ├── requirements.txt
    └── secret.txt
```
**secret.txt** is actually a webhook of chat in discord which can be founded in your discord setup. [reference](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

## Execution
```Bash
python main.py
```

## Project Struture
```Plaintext
📂 Mercari_crawler/
├── .github/workflows/   # CI/CD Pipeline configurations
├── discord.py           # Discord notification logic
├── main.py              # Scraper core engine
├── Dockerfile           # Containerization configuration
├── requirements.txt     # Python dependencies
└── secret.txt           # Local secret (ignored by git)
```