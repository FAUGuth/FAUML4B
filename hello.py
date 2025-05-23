import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="F1 World Champions", layout="centered")
st.title("🏁 F1 World Champions – Interactive Visualization")

# Sample data
data = {
    "Driver": [
        "Lewis Hamilton",
        "Michael Schumacher",
        "Sebastian Vettel",
        "Ayrton Senna",
        "Fernando Alonso",
        "Max Verstappen",
        "Niki Lauda",
        "Alain Prost"
    ],
    "Titles": [7, 7, 4, 3, 2, 3, 3, 4]
}
df = pd.DataFrame(data)

# --- Sidebar filters ---
st.sidebar.header("🔧 Filters")

# Driver filter
driver_filter = st.sidebar.multiselect(
    "Select Drivers:",
    options=df["Driver"],
    default=df["Driver"]
)

# Minimum titles filter
min_titles = st.sidebar.slider(
    "Minimum Number of Titles:",
    min_value=1, max_value=7, value=1
)

# Apply filters
filtered_df = df[
    (df["Driver"].isin(driver_filter)) &
    (df["Titles"] >= min_titles)
].sort_values("Titles", ascending=True)

# Show warning if nothing matches
if filtered_df.empty:
    st.warning("No drivers match your filter criteria.")
else:
    # Plot with Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        data=filtered_df,
        x="Titles", y="Driver",
        hue="Driver", legend=False,
        palette="coolwarm", ax=ax
    )

    # Add value labels
    for i, val in enumerate(filtered_df["Titles"]):
        ax.text(val + 0.1, i, str(val), color='black', va='center')

    # Styling
    ax.set_title("F1 World Championships by Driver")
    ax.set_xlabel("Number of Titles")
    ax.set_ylabel("Driver")
    st.pyplot(fig)
