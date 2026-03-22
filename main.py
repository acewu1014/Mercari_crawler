from playwright.sync_api import sync_playwright
import schedule
import time
from datetime import datetime
from urllib.parse import quote_plus
from discord import discord_notify
# 搜尋關鍵字
# "フーパ ポケモンカード"
# "アクア団のカイオーガEX", "マグマ団のグラードンEX"
SEARCH_QUERIES = ["フーパ　プロモ", "レックウザ",  "ゴッホピカチュウ", "ポンチョを着たピカチュウ", "ムンク展", "バンデットリング", "日本代表のピカチュウ", "メガトウキョーのピカチュウ", "ピッチのピカチュウ"]
notified_links = set()
dc = discord_notify()


def scrape_mercari(search_query):
    global notified_links
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        encoded_query = quote_plus(search_query)
        search_url = f"https://jp.mercari.com/search?keyword={encoded_query}&sort=created_time&order=desc"

        try:
            page.goto(search_url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_selector("li[data-testid='item-cell']", timeout=60000)
        except Exception as e:
            print(f"⚠️ 無法載入商品清單（關鍵字：{search_query}），錯誤: {e}")
            browser.close()
            return

        items = page.query_selector_all("li[data-testid='item-cell']")
        new_items = []

        for item in items:
            try:
                link_tag = item.query_selector("a")
                img_tag = item.query_selector("img")
                price_tag = item.query_selector("span.number__6b270ca7")

                if not link_tag or not img_tag or not price_tag:
                    continue

                link = link_tag.get_attribute("href")
                full_link = f"https://jp.mercari.com{link}"
                if full_link in notified_links:
                    continue

                image_url = img_tag.get_attribute("src")
                title = img_tag.get_attribute("alt")
                price = price_tag.text_content()

                new_items.append({
                    "title": title,
                    "price": price,
                    "link": full_link,
                    "image": image_url
                })
                notified_links.add(full_link)

            except Exception as e:
                print("❌ 資料處理錯誤:", e)
                continue

        if new_items:
            for item in new_items:
                dc.send_discord_embed(item['title'], item['price'], item['link'], item['image'])
            print(f"[{datetime.now()}] ✅ 發送 {len(new_items)} 筆通知")
        else:
            print(f"[{datetime.now()}] 💤 無新商品")

        browser.close()


def search():
    for keyword in SEARCH_QUERIES:
        print(f"\n🔍 開始搜尋關鍵字：『{keyword}』")
        scrape_mercari(keyword)


# 每 1 分鐘執行一次
schedule.every(1).minutes.do(search)

if __name__ == "__main__":
    print("📦 Mercari 爬蟲啟動中...")
    while True:
        # schedule.run_pending()
        # time.sleep(1)
        search()
