from playwright.sync_api import sync_playwright
import schedule
import time
import requests
from datetime import datetime

f = open(r"secret.txt", "r")
# Discord Webhook URL
DISCORD_WEBHOOK_URL = f.read()

#Search Keywords
SEARCH_QUERY = "スヌーピー オラフ"
notified_links = set()

def send_discord_embed(title, price, link, image_url):
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
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    print("Discord 發送狀態:", response.status_code)

def scrape_mercari():
    global notified_links
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        search_url = f"https://jp.mercari.com/search?keyword={SEARCH_QUERY}&sort=created_time&order=desc"
        page.goto(search_url)
        try:
            page.wait_for_selector("li[data-testid='item-cell']", timeout=60000)

        except Exception as e:
            print("⚠️ 無法載入商品清單，可能被廣告擋住或網路過慢")
            browser.close()
            return
    
        items = page.query_selector_all("li[data-testid='item-cell']")
        new_items = []

        for item in items:
            try:
                link_tag = item.query_selector("a")
                img_tag = item.query_selector("img")
                price_tag = item.query_selector("span.number__6b270ca7")

                # 資訊不完整則跳過
                if not link_tag or not img_tag or not price_tag:
                    continue

                # 取得資料
                link = link_tag.get_attribute("href")
                full_link = f"https://jp.mercari.com{link}"

                image_url = img_tag.get_attribute("src")
                title = img_tag.get_attribute("alt")
                price = price_tag.text_content()

                if full_link in notified_links:
                    continue
                
                new_items.append({
                    "title": title,
                    "price": price,
                    "link": full_link,
                    "image": image_url
                })
                notified_links.add(full_link)

                print(new_items)
            except Exception as e:
                print("錯誤：", e)
                continue

        if new_items:
            for item in new_items:
                send_discord_embed(item['title'], item['price'], item['link'], item['image'])
            print(f"[{datetime.now()}] 發送 {len(new_items)} 筆通知")
        else:
            print(f"[{datetime.now()}] 無新商品")

        browser.close()

# 每 10 分鐘執行一次
schedule.every(1).minutes.do(scrape_mercari)

print(f"開始搜尋『{SEARCH_QUERY}』商品並推送到 Discord...")
while True:
    schedule.run_pending()
    time.sleep(1)

