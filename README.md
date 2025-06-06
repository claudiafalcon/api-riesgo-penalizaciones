# Merchant Penalty Risk API (Flask + MongoDB)

This project is a Flask-based API designed to support the development of machine learning models that predict financial penalties imposed by credit card brands (such as Visa or Mastercard) on affiliated merchants.

## 🔍 Purpose

Enable structured access to historical transaction data to:

- Explore merchant activity over time
- Analyze patterns associated with chargebacks, fraud, and declines
- Prepare training data for machine learning models
- Simulate risk scores for merchant penalization

## 🧱 Project Structure

```
api-riesgo-penalizaciones/
│
├── app/
│   ├── __init__.py          # Flask app configuration
│   ├── routes.py            # API endpoints
│   └── mongo.py             # MongoDB connection (pending real data)
│
├── run.py                   # Script to launch the app
├── requirements.txt         # Required libraries
├── .gitignore               # Git exclusions
└── README.md                # This file
```

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Launch the Flask server:
   ```bash
   python run.py
   ```

3. Test the API:
   - Home: `GET /`
   - Transactions placeholder: `GET /transacciones`

## ⚙️ Dependencies

- Flask
- PyMongo

## 📌 Project Status

✅ Ready for MongoDB Atlas connection  
⏳ Waiting on real data access  
🧪 Endpoints will evolve as analysis progresses

## 👩‍💻 Author

This project is part of the professional portfolio of [Your Name], a former BSS Systems Architect transitioning into AI and data-driven risk solutions for financial and retail sectors.
