import requests
import os

class discord_notify():
    def __init__(self):
        self.DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
        
        if not self.DISCORD_WEBHOOK_URL:
            try:
                with open("secret.txt", "r") as f:
                    self.DISCORD_WEBHOOK_URL = f.read().strip()
            except FileNotFoundError:
                print("❌ 錯誤: 找不到 DISCORD_WEBHOOK_URL 環境變數或 secret.txt")

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