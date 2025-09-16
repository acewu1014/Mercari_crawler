## Project Name: Python Crawler
## Descriptions
When dealing with long videos, precisely annotating their content becomes challenging. Therefore, existing methods typically use off the shelf shot detection modules, such as Shot Detector or other AI-based models, to segment long videos into smaller shots for annotation. However, there is currently no well-suited annotation tool for handling such segmented data. To address this issue, we propose this project to facilitate the rapid annotation of videos.

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
python main.py
```