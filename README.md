# 🚗 Vehicle Listings Web Scraper & Data Pipeline

A Python-based web scraping and data ingestion pipeline built to extract vehicle listing data from a dynamic online marketplace. This project demonstrates end-to-end automation — from browser-based scraping to structured storage in MongoDB and Excel — using a clean, modular, and production-style project structure.

---

## 📌 Features

- Scrapes vehicle listings from a dynamic website using **Selenium**
- Accepts vehicle brand and number of pages as user input
- Handles pagination and dynamic content loading
- Extracts structured data including:
  - Vehicle name
  - Location
  - Price
  - Mileage
  - Posted time
  - Listing URL
- Stores scraped data in:
  - **MongoDB** for persistent storage
  - **Excel (.xlsx)** for easy analysis
- Modular and readable codebase suitable for real-world automation tasks

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Web Automation:** Selenium, WebDriver Manager
- **Database:** MongoDB
- **File Export:** openpyxl
- **Environment:** Python Virtual Environment (venv)

---

## 📂 Project Structure

```
vehicle-listings-web-scraper/
│
├── scraper/
│   └── vehicle_scraper.py      # Web scraping logic
│
├── storage/
│   └── data_store.py           # MongoDB and Excel storage
│
├── main.py                     # Application entry point
├── config.py                   # Optional configuration file
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignored files
└── README.md                   # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/navojithamindu-git/vehicle-listings-web-scraper.git
cd vehicle-listings-web-scraper
```

---

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4️⃣ Ensure MongoDB is running

MongoDB should be available at:

```
mongodb://localhost:27017
```

You can modify this connection string inside `data_store.py` if required.

---

## ▶️ How to Run the Project

```bash
python main.py
```

You will be prompted to enter:

```text
Enter vehicle brand (e.g., toyota-aqua):
Enter number of pages to scrape:
```

Example input:
```
toyota-aqua
5
```

---

## 📊 Output

- **Excel File:** `scraped_vehicles.xlsx`
- **MongoDB Database:** `VehicleData`
- **Collection:** `details`

Each record contains structured vehicle information along with the source listing URL.

---

## ⚠️ Disclaimer

This project is intended for **educational and portfolio purposes only**.  
Please review and comply with the target website’s **terms of service** before scraping. Use responsibly.

---

## 🚀 Future Enhancements

- Add `.env` support for configuration
- Enable headless scraping for improved performance
- Implement logging and retry mechanisms
- Dockerize the application
- Add unit tests

---

## 👩‍💻 Author

**Navojith**  
Business Analyst | Data & Automation Enthusiast  
Python • Web Scraping • Data Engineering
