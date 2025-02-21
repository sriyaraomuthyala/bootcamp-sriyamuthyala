import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    conn = sqlite3.connect("store.db")
    df = pd.read_sql_query("SELECT id, price FROM products", conn)
    conn.close()

    X = df[['id']]
    y = df['price']

    model = LinearRegression()
    model.fit(X, y)
    
    return model

model = train_model()
predicted_price = model.predict([[5]])  # Predict price for product ID 5
print("Predicted price:", predicted_price[0])
