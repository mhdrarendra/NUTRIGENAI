import pandas as pd
import sqlite3

# load CSV
df = pd.read_csv("data/nutrition_clean.csv")

# koneksi DB
conn = sqlite3.connect("nutrition.db")

# simpan ke tabel
df.to_sql("foods", conn, if_exists="replace", index=False)

print(" Data berhasil masuk database")