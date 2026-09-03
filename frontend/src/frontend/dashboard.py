import streamlit as st
import httpx
import os
import matplotlib.pyplot as plt
import pandas as pd

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

def main():
    st.markdown("# Solar Data Dashboard")

    stats = httpx.get(f"{BASE_URL}/solar-data/csv", timeout=30).json() # Fetch solar data from the backend API endpoint and store it in the variable 'stats'
    st.dataframe(stats) # Display the fetched solar data in a table format using Streamlit's dataframe component

    df = pd.DataFrame(stats) # Create a pandas DataFrame from the fetched solar data for further analysis and visualization

    st.subheader("Antal solförmörkelser per typ")

    # Create a bar chart to visualize the count of solar eclipses by type using matplotlib
    fig, ax = plt.subplots(figsize=(8, 5))
    df["Eclipse Type"].value_counts().plot(kind="bar", ax=ax, color="steelblue")
    ax.set_title("Antal solförmörkelser per typ")
    ax.set_xlabel("Typ")
    ax.set_ylabel("Antal")
    plt.tight_layout()

    st.pyplot(fig)



if __name__ == "__main__":
    main()