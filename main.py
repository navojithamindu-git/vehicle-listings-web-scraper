from scraper.vehicle_scraper import scrape_vehicle_listings
from storage.data_store import save_to_excel, save_to_mongodb


def main():
    brand = input("Enter vehicle brand (e.g., toyota-aqua): ").strip()
    pages = int(input("Enter number of pages to scrape: "))

    data = scrape_vehicle_listings(brand, pages)

    if not data:
        print("No data found.")
        return

    save_to_excel(data)
    save_to_mongodb(data)

    print(f"Saved {len(data)} vehicle listings successfully.")


if __name__ == "__main__":
    main()
