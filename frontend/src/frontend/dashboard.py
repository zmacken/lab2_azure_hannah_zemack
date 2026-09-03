import streamlit as st
import httpx
import os
import matplotlib.pyplot as plt
import pandas as pd

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

def main():
    st.markdown("# Solar Data Dashboard")

    stats = httpx.get(f"{BASE_URL}/solar-data/csv", timeout=30).json()
    st.dataframe(stats)

    df = pd.DataFrame(stats)

    st.subheader("Antal solförmörkelser per typ")

    fig, ax = plt.subplots(figsize=(8, 5))
    df["Eclipse Type"].value_counts().plot(kind="bar", ax=ax, color="steelblue")
    ax.set_title("Antal solförmörkelser per typ")
    ax.set_xlabel("Typ")
    ax.set_ylabel("Antal")
    plt.tight_layout()

    st.pyplot(fig)



if __name__ == "__main__":
    main()