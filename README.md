![Build Status](https://github.com/acewu1014/Mercari_crawler/actions/workflows/devops-ci.yaml/badge.svg)
## Project Name: Python Crawler
## Descriptions
Automated Mercari Scraper & Discord Notifier
A robust web scraping solution built with Python and Playwright to monitor Japanese e-commerce listings in real-time.

Key DevOps Features:

1, Containerization: Fully dockerized environment for consistent deployment across different infrastructures.

2, CI/CD Pipeline: Integrated GitHub Actions for automated linting (Flake8), dependency management, and build verification.

3, Cloud-Native Security: Implemented secret management using environment variables to ensure secure handling of sensitive Webhook URLs.

4, Infrastructure as Code (IaC) Ready: Designed with a modular architecture suitable for deployment on Kubernetes or cloud-based runners.

## Environment Setup
1. **Create a virtual environment:**
    ```bash
    conda create -n crawler python=3.7
    conda activate crawler
    ```   

2. **Install dependecy:**
    ```bash
    pip install -r requirements.txt
    ```
    
    ```txt
    playwright == 1.51.0
    requests == 2.32.3
    schedule == 1.2.2
    ```
3. **Add Secret.txt:**
Your foler should look like
```Python
📂Mercari_crawler/
    ├── discord.py
    ├── main.py
    ├── requirements.txt
    └── secret.txt
```
**secret.txt** is actually a webhook of chat in discord which can be founded in your discord setup. [reference](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

## Start
CMD:
```
python main.py //if there is secret.txt in same directory
python 
```