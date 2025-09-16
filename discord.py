import requests

class discord_notify():
    def __init__(self):
        with open("secret.txt", "r") as f:
            self.DISCORD_WEBHOOK_URL = f.read().strip()

    def send_discord_embed(self, title, price, link, image_url):
        embed = {
            "title": title,
            "url": link,
            "description": f"💰 NT{price}",
            "image": {"url": image_url},
            "color": 15844367  # 金黃色
        }
        payload = {
            "embeds": [embed]
        }
        response = requests.post(self.DISCORD_WEBHOOK_URL, json=payload)
        print("Discord 發送狀態:", response.status_code)