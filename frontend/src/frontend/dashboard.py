import streamlit as st
import httpx
import os

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

def main():
    st.markdown("# Solar Data Dashboard")
    st.write(BASE_URL)

    stats = httpx.get(f"{BASE_URL}/solar-data/csv", timeout=30).json()
    st.dataframe(stats)

if __name__ == "__main__":
    main()